#!/bin/bash

RED='\e[1;31m'
BLUE='\e[1;34m'
CLEAR_COLOR='\e[0m' # No Color
RESULT_FILE="./results.txt"
INPUT_PATH="./input"
OUTPUT_PATH="./output"

# Worth to check
# - google_api_key
# - google_app_id
# - google_crash_reporting_api_key
# - google_storage_bucket
# - MAPS_API_KEY

# https://book.hacktricks.xyz/mobile-pentesting/android-app-pentesting

checksAndroidManifestDebuggable () {
    filename=$1
    if grep --silent -i 'debuggable="true"' "$OUTPUT_PATH/$filename/AndroidManifest.xml"; then
        echo -e "$filename: AndroidManifest: ${RED}debuggable=true${CLEAR_COLOR}"

        echo -e "$filename : debuggable=\"true\" : $OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        grep -n -i 'debuggable="true"' "$OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        echo -e "$filename: AndroidManifest: ${BLUE}debuggable=false${CLEAR_COLOR}"
    fi
}

checksAndroidManifestAllowBackup () {
    filename=$1
    if grep --silent -i 'allowBackup="true"' "$OUTPUT_PATH/$filename/AndroidManifest.xml"; then
        echo -e "$filename: AndroidManifest: ${RED}allowBackup=true${CLEAR_COLOR}"

        echo -e "$filename : allowBackup=\"true\" : $OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        grep -n -i 'allowBackup="true"' "$OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AndroidManifest: ${BLUE}allowBackup=false${CLEAR_COLOR}"
    fi
}

# checksValuesStringGoogleApiKey () {
#     echo "-> checksValuesStringGoogleApiKey"
#     if grep -silent -i 'google_api_key' "$(pwd)/output/$filename/res/values/strings.xml"; then
#         google_api_key="$(grep --silent -o -i 'google_api_key')"
#         echo "$filename: google_api_key = ${LIGHT_BLUE}$google_api_key${NC}"
#         grep "$filename: ${LIGHT_BLUE}$google_api_key${NC}" >> "$(pwd)/output/results.txt"
#     fi
# }

# checksAPIkeys (){
#     filename=$1
#     # grep -i "apikey" "$(pwd)/output/$filename/res/values/strings.xml"
#     # grep -i "apikey" "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"
# }

findFirebaseUrl (){
    filename=$1

    FIREBASE_DATABASE_URL="$(grep -o https.*firebaseio.com "$OUTPUT_PATH/$filename/res/values/strings.xml")"
}

prepareFirebaUrlJson (){
    FIREBASE_DATABASE_URL=$1
    FIREBASE_DATABASE_URL_JSON=$FIREBASE_DATABASE_URL"/.json"
}

getFirebaseResponseBodyContent (){
    FIREBASE_DATABASE_JSON=$1
    FIREBASE_DATABASE_RESPONSE="$(curl -s $FIREBASE_DATABASE_JSON)"

    # FIX FIREBASE_DATABASE_RESPONSE_BODY GREP with Regex
    # FIREBASE_DATABASE_RESPONSE_BODY="$(echo $FIREBASE_DATABASE_RESPONSE | grep '".*"')"
    FIREBASE_DATABASE_RESPONSE_BODY="$(grep -E '".*"' $FIREBASE_DATABASE_RESPONSE)"

    echo "$filename: FIREBASE_DATABASE_RESPONSE : $FIREBASE_DATABASE_RESPONSE"
    echo "$filename: FIREBASE_DATABASE_RESPONSE_BODY : $FIREBASE_DATABASE_RESPONSE_BODY"
}

checksFirebasePermission (){
    filename=$1
    
    local FIREBASE_DATABASE_URL=""
    local FIREBASE_DATABASE_URL_JSON=""
    local FIREBASE_DATABASE_RESPONSE_BODY=""

    findFirebaseUrl $filename
    prepareFirebaUrlJson $FIREBASE_DATABASE_URL
    getFirebaseResponseBodyContent $FIREBASE_DATABASE_URL_JSON

    if [[ $FIREBASE_DATABASE_RESPONSE_BODY == *"Permission denied"* ]]; then
        echo -e "\n$filename : $FIREBASE_DATABASE_URL: ${BLUE}Permission denied${CLEAR_COLOR}"
        echo -e "$filename : $FIREBASE_DATABASE_URL: Permission denied" >> "$RESULT_FILE"
    else
        echo -e "\n$filename : $FIREBASE_DATABASE_URL: is POTENTIALLY ${RED}vulnerable${CLEAR_COLOR}: $FIREBASE_DATABASE_RESPONSE_BODY"
        echo -e "$filename : $FIREBASE_DATABASE_URL: is POTENTIALLY vulnerable: $FIREBASE_DATABASE_RESPONSE_BODY" >> "$RESULT_FILE"
    fi

}

runTests (){
    filename=$1
    
    checksAndroidManifestDebuggable $filename
    checksAndroidManifestAllowBackup $filename
    # checksValuesStringGoogleApiKey $filename
    # checksAPIkeys $filename
    checksFirebasePermission $filename
}

installApkTools (){

    if [ ! -f /usr/local/bin/apktool.jar ]; then
        echo "ApkTool is not installed. Start installing..."

        # Download Linux wrapper script (Right click, Save Link As apktool)
        echo "Step 1/6: Download Linux wrapper script"
        curl "https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool" > apktool.sh

        # Download apktool-2 (find newest here)
        echo "Step 2/6: Download apktool-2"
        curl "https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.7.0.jar" > apktool_2.7.0.jar

        # Rename downloaded jar to apktool.jar
        echo "Step 3/6: Rename downloaded jar to apktool.jar"
        mv apktool_2.7.0.jar apktool.jar

        # Move both files (apktool.jar & apktool) to /usr/local/bin (root needed)
        echo "Step 4/6: Move both files (apktool.jar & apktool) to /usr/local/bin"
        sudo mv apktool.sh /usr/local/bin/apktool.sh
        sudo mv apktool.jar /usr/local/bin/apktool.jar

        # Make sure both files are executable (chmod +x)
        echo "Step 5/6: Made apktool.jar and apktool executable (755)"
        sudo chmod 755 /usr/local/bin/apktool.sh
        sudo chmod 755 /usr/local/bin/apktool.jar

        # Try running apktool via cli
        echo "Step 6/6: Check if apktool was successfully installed"
        which apktool

    else
        echo "ApkTool detected."
    fi

}

installRust (){
    if [ ! -f /home/kali/.cargo/bin/rustc ]; then
        curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
        source "$HOME/.cargo/env"
    fi
}

installApkeep (){
    if [ ! -f /home/kali/.cargo/bin/apkeep ]; then
    sudo apt install libssl-dev
    sudo apt install pkg-config -y
    cargo install apkeep --locked
fi
}

createInputDirectory (){
    if [ ! -d "$INPUT_PATH" ]; then
        mkdir "$INPUT_PATH"
        echo "Directory 'input' created. Please provide .apk in $INPUT_PATH or run the script with -d to download .apks from list."

    fi
}

createOutputDirectory (){
    if [ ! -d "$OUTPUT_PATH" ]; then
        mkdir "$OUTPUT_PATH"
        echo "Directory 'output' created."
fi
}

createResultFile (){
    # Create result file
    echo "=== Results ===" > "$RESULT_FILE"
    chmod 766 "$RESULT_FILE"
}

replaceWhitespaceWithDots (){
    file=$1
    filename=$(basename -- "$file")
    filenameWithoutWhiteSpace="${filename// /.}"
}

updateApkFilename (){
    filename=$1
    filenameWithoutWhiteSpace=$2
    mv -vn "$INPUT_PATH/$filename" "$INPUT_PATH$filenameWithoutWhiteSpace"
}


downloadApks (){
    local filename=""
    local filenameWithoutWhiteSpace=""

    PATH_TO_LIST="./apksList.txt"

    while read apkToDownload; do
        echo "Start downloading: $apkToDownload"
        apkeep -a $apkToDownload $INPUT_PATH
    done < "$PATH_TO_LIST"

    for files in "$INPUT_PATH"/*; do
        
        replaceWhitespaceWithDots $files
        getFilename $files
        updateApkFilename $filename $filenameWithoutWhiteSpace
    done
}

getFilename (){
    file=$1
    filename=$(basename -- "$file")
}

getExtension (){
    file=$1
    filename=$(basename -- "$file")
    extension="${filename##*.}"
}

runApkTool (){
    filename=$1
    apktool d "$INPUT_PATH/$filename" -o "$OUTPUT_PATH/$filename" -f --quiet
}

main (){
    ### Main script ###

    while getopts 'df' OPTION; do
        case "$OPTION" in
            d)
            echo "Download apks from file"
            downloadApkMode=true
            ;;
        esac
    done

    local filename=""
    local extension=""

    installApkTools
    installRust
    installApkeep
    createInputDirectory
    createOutputDirectory
    createResultFile
    
    if "$downloadApkMode" = true; then
        downloadApks
    fi



    # Decompile all apks in "input" directory and run tests

    for files in "$INPUT_PATH"/*; do
    

        getFilename $files
        getExtension $files
                
        if [ "$extension" == "xapk" ]; then
            echo "File has XAPK format. Skip analyze."
        else         
            echo "Decompiling: $filename"

            runApkTool $filename
            runTests $filename
        fi

        echo -e "\n"
    done
}

main