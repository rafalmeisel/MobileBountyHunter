#!/bin/bash

RED='\e[1;31m'
YELLOW='\e[1;33m'
BLUE='\e[1;34m'
NO_COLOR='\e[0m' # No Color
RESULT_FILE="./results.txt"
INPUT_PATH="./input"
OUTPUT_PATH="./output"
INPUT_ANALYZED_PATH="./input_analyzed"
OUTPUT_ANALYZED_PATH="./output_analyzed"
APKS_LIST_DEFAULT_PATH="./apksList-default.txt"
GOOGLE_PLAY_DEVELOPER_URLS_PATH="./googlePlayDeveloperUrls.txt"

# Worth to check
# - google_api_key
# - google_app_id
# - google_crash_reporting_api_key
# - google_storage_bucket
# - MAPS_API_KEY

# TODO:
# SMILES_API_KEY / strings.xml

# https://book.hacktricks.xyz/mobile-pentesting/android-app-pentesting

checksAndroidManifestDebuggable () {
    filename=$1

    debuggableRegex='debuggable="true"'
    if grep --silent -i "$debuggableRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml"; then
        printf "$filename: AndroidManifest: ${RED}debuggable=true${NO_COLOR}\n"

        echo -e "$filename : $debuggableRegex : $OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        grep -n -i "$debuggableRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AndroidManifest: ${BLUE}debuggable=false${NO_COLOR}\n"
    fi
}

# Application store additional data as backup as it's running or closed
checksAndroidManifestAllowBackup () {
    filename=$1

    allowBackupRegex='allowBackup="true"'
    if grep --silent -i "$allowBackupRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml"; then
        printf "$filename: AndroidManifest: ${RED}allowBackup=true${NO_COLOR}\n"

        echo -e "$filename : $allowBackupRegex : $OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        grep -n -i "$allowBackupRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AndroidManifest: ${BLUE}allowBackup=false${NO_COLOR}\n"
    fi
}

# Activity can be accessed from outside the application
checksAndroidManifestExported () {
    filename=$1

    exportedRegex='exported="true"'
    if grep --silent -i "$exportedRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml"; then
        printf "$filename: AndroidManifest: ${RED}exported=true${NO_COLOR}\n"

        echo -e "$filename : "$exportedRegex" : $OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        grep -n -i "$exportedRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AndroidManifest: ${BLUE}exported=false${NO_COLOR}\n"
    fi
}

checksStringsAwsAkid () {
    filename=$1
    awsAkidRegex=">(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])<"
    
    if grep --silent -oP "$awsAkidRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml"; then
        
        AWS_AKID="$(grep -oP "$awsAkidRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml")"
        AWS_AKID="${AWS_AKID:1:-1}"

        printf "$filename: AWS_AKID: ${RED}$AWS_AKID${NO_COLOR}\n"

        echo -e "$filename : AWS_AKID: $AWS_AKID : $OUTPUT_PATH/$filename/res/values/strings.xml" >> "$RESULT_FILE"
        grep -n -oP "$awsAkidRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AWS_AKID: ${BLUE}Not found${NO_COLOR}\n"
    fi
}

checksStringsAwsSecretKey () {
    filename=$1
    awsSecretKeyRegex=">(?<![A-Za-z0-9+=])[A-Za-z0-9+=]{40}(?![A-Za-z0-9+=])<"

    if grep --silent -oP "$awsSecretKeyRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml"; then
        
        AWS_SECRET_KEY="$(grep -oP "$awsSecretKeyRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml")"
        AWS_SECRET_KEY="${AWS_SECRET_KEY:1:-1}"

        printf "$filename: AWS_SECRET_KEY: ${RED}$AWS_SECRET_KEY${NO_COLOR}\n"

        echo -e "$filename : AWS_SECRET_KEY: $AWS_SECRET_KEY : $OUTPUT_PATH/$filename/res/values/strings.xml" >> "$RESULT_FILE"
        grep -n -oP "$awsSecretKeyRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AWS_SECRET_KEY: ${BLUE}Not found${NO_COLOR}\n"
    fi
}

checksStringsAwsUrl () {
    filename=$1
    awsUrlRegex="http.*amazonaws.com"

    if grep --silent -oP "$awsUrlRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml"; then
        
        AWS_URL="$(grep -oP "$awsUrlRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml")"

        printf "$filename: AWS_URL: ${RED}$AWS_URL${NO_COLOR}\n"

        echo -e "$filename : AWS_URL: $AWS_URL : $OUTPUT_PATH/$filename/res/values/strings.xml" >> "$RESULT_FILE"
        grep -n -oP "$awsUrlRegex" "$OUTPUT_PATH/$filename/res/values/strings.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AWS_URL: ${BLUE}Not found${NO_COLOR}\n"
    fi
}


checksAws (){
    filename=$1
    
    local AWS_AKID=""
    local AWS_SECRET_KEY=""
    local AWS_URL=""

    checksStringsAwsAkid $filename
    checksStringsAwsSecretKey $filename
    checksStringsAwsUrl $filename

    # TODO:
    # Add verification for AWS Database
}

# Oracle Push Cloud Service / Push IO application identifier
# https://us.v-cdn.net/6032259/uploads/jive_attachments/2/7/3/27334154ydoByranib.pdf
checksAndroidManifestPushIoApplicationIdentifier () {
    filename=$1

    pushIoApplicationIdentifierRegex='"pio-.*"'

    if grep --silent -i "$pushIoApplicationIdentifierRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml"; then
        printf "$filename: AndroidManifest: ${RED}PushIO=$pushIoApplicationIdentifierRegex${NO_COLOR}\n"

        echo -e "$filename : "$pushIoApplicationIdentifierRegex" : $OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        grep -n -i "$pushIoApplicationIdentifierRegex" "$OUTPUT_PATH/$filename/AndroidManifest.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AndroidManifest: ${BLUE}PushIO not found.${NO_COLOR}\n"
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
    FIREBASE_DATABASE_URL="$(grep -oP 'https.*firebaseio.com' $OUTPUT_PATH/$filename/res/values/strings.xml)"
    # echo "findFirebaseUrl : FIREBASE_DATABASE_URL : $FIREBASE_DATABASE_URL"
}

prepareFirebaUrlJson (){
    FIREBASE_DATABASE_URL=$1
    FIREBASE_DATABASE_URL_JSON=$FIREBASE_DATABASE_URL"/.json"
    # echo "prepareFirebaUrlJson : FIREBASE_DATABASE_URL_JSON : $FIREBASE_DATABASE_URL_JSON"
}

getFirebaseResponseBodyContent (){
    FIREBASE_DATABASE_JSON=$1
    FIREBASE_DATABASE_RESPONSE="$(curl -s $FIREBASE_DATABASE_JSON)"
    FIREBASE_DATABASE_RESPONSE_BODY=$(echo "$FIREBASE_DATABASE_RESPONSE" | grep -oP '".*"')
}

checksFirebasePermission (){
    filename=$1
    
    local FIREBASE_DATABASE_URL=""
    local FIREBASE_DATABASE_URL_JSON=""
    local FIREBASE_DATABASE_RESPONSE_BODY=""

    findFirebaseUrl $filename
    
    if [[ $FIREBASE_DATABASE_URL == "" ]]; then
        printf "$filename: Strings: No Firebase URL found.\n"
    else
        prepareFirebaUrlJson $FIREBASE_DATABASE_URL 
        getFirebaseResponseBodyContent $FIREBASE_DATABASE_URL_JSON
        
        
        if [[ $FIREBASE_DATABASE_RESPONSE_BODY == *"Permission denied"* ]]; then
            printf "$filename: Strings: $FIREBASE_DATABASE_URL: ${BLUE}Permission denied${NO_COLOR}\n"
            echo -e "$filename: Strings: $FIREBASE_DATABASE_URL: Permission denied" >> "$RESULT_FILE"

        elif [[ $FIREBASE_DATABASE_RESPONSE_BODY == *"has been deactivated"* ]]; then
            printf "$filename: Strings: $FIREBASE_DATABASE_URL: ${YELLOW}Database has been deactivated${NO_COLOR}\n"
            echo -e "$filename: Strings: $FIREBASE_DATABASE_URL: Permission denied" >> "$RESULT_FILE"

        else
            printf "$filename: Strings: $FIREBASE_DATABASE_URL: is POTENTIALLY ${RED}vulnerable${NO_COLOR}: $FIREBASE_DATABASE_RESPONSE_BODY\n"
            echo -e "$filename: Strings: $FIREBASE_DATABASE_URL: is POTENTIALLY vulnerable: $FIREBASE_DATABASE_RESPONSE_BODY" >> "$RESULT_FILE"
        fi
    fi
}

# findAwsData () {
#     filename=$1
    

#     if grep --silent -i 'aws' "$OUTPUT_PATH/$filename/res/values/strings.xml"; then

#         AWS_DATA="$(grep -i 'aws' $OUTPUT_PATH/$filename/res/values/strings.xml)"
#         echo -e "$filename: AWS Data: $AWS_DATA"
#         echo -e "$filename : $AWS_DATA" >> "$RESULT_FILE"
#         echo -e "\n" >> "$RESULT_FILE"
#     else
#         echo -e "$filename: AndroidManifest: ${BLUE}exported=false${NO_COLOR}"
#     fi
# }

# findHttpUrls() {
#     filename=$1
    
#     if grep --silent -inr 'http://' "$OUTPUT_PATH/$filename" --exlude-dir=lib; then

#         httpUrls="$(grep -inr 'http://' $OUTPUT_PATH/$filename --exlude-dir=lib)"
#         echo -e "$filename: HTTP Urls: $httpUrls"
#         echo -e "$filename : $httpUrls" >> "$RESULT_FILE"
#         echo -e "\n" >> "$RESULT_FILE"
#     else
#         echo -e "$filename: HTTP Urls: None"
#     fi
# }

# findHttpsUrls() {
#     filename=$1
    
#     if grep --silent -inr 'https://' "$OUTPUT_PATH/$filename" --exlude-dir=lib; then

#         httpsUrls="$(grep -inr 'https://' $OUTPUT_PATH/$filename --exlude-dir=lib)"
#         echo -e "$filename: HTTPS Urls: $httpsUrls"
#         echo -e "$filename : $httpsUrls" >> "$RESULT_FILE"
#         echo -e "\n" >> "$RESULT_FILE"
#     else
#         echo -e "$filename: HTTPS Urls: None"
#     fi
# }

runTests (){
    filename=$1
    
    checksAndroidManifestDebuggable $filename
    checksAndroidManifestAllowBackup $filename
    checksAndroidManifestExported $filename
    # checksValuesStringGoogleApiKey $filename
    # checksAPIkeys $filename
    checksFirebasePermission $filename
    # findAwsData $filename
    # findHttpUrls $filename
    # findHttpsUrls $filename
    checksAws $filename
    checksAndroidManifestPushIoApplicationIdentifier $filename
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

installAwsCli (){
    if [ ! -f /home/kali/.cargo/bin/apkeep ]; then
        sudo apt install awscli -y
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
    mv -vn "$INPUT_PATH/$filename" "$INPUT_PATH/$filenameWithoutWhiteSpace"
}

checkApkListIsEmpty (){
    PATH_TO_LIST=$1

    # Apks List File is empty. -s return True if FILE exists and has a size greater than zero.
    if [ ! -s $PATH_TO_LIST ]; then    
        echo "Please provide apks names in file: $PATH_TO_LIST"
        exit 0
    fi
}

downloadApks (){
    PATH_TO_LIST=$1

    local filename=""
    local filenameWithoutWhiteSpace=""

    checkApkListIsEmpty $PATH_TO_LIST

    while read apkToDownload; do
        echo "Start downloading: $apkToDownload"
        apkeep -a $apkToDownload "$INPUT_PATH/"
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

retrieveApkNamesfromDeveloperProfileUrl (){
    developerUrl=$1
    
    developerUrlResponseContentFilename="developerUrlResponseContent.txt"
    
    curl $developerUrl > $developerUrlResponseContentFilename

    apkNameRegex='"\/store\/apps\/details\?id=(.*?)"'

    grep -oP $apkNameRegex $developerUrlResponseContentFilename >> $APKS_LIST_DEFAULT_PATH

    sed -i 's@/store/apps/details?id=@@' $APKS_LIST_DEFAULT_PATH
    sed -i 's@"@@' $APKS_LIST_DEFAULT_PATH
    sed -i 's@"@@' $APKS_LIST_DEFAULT_PATH

}

readUrlFromGooglePlayDeveloperUrlFile (){

    while read googlePlayDeveloperUrl; do
        
        developerUrl="$(echo $googlePlayDeveloperUrl | cut -f1 -d"#")"
        retrieveApkNamesfromDeveloperProfileUrl $developerUrl

    done < "$GOOGLE_PLAY_DEVELOPER_URLS_PATH"
}

main (){   

    pathToApksList=$1

    apksListExtension=".txt"
    pathToApksListWithoutExtention=${pathToApksList::-4} 
    pathToApksListAnalyzed="$pathToApksListWithoutExtention"_analyzed"$apksListExtension"

    downloadApkMode=$2
   
    local filename=""
    local extension=""

    installApkTools
    installRust
    installApkeep
    createInputDirectory
    createOutputDirectory
    createResultFile
    readUrlFromGooglePlayDeveloperUrlFile
    
    if [[ "$downloadApkMode" == true ]] ; then
        downloadApks $pathToApksList
    fi

    # Decompile all apks in "input" directory and run tests
    for files in "$INPUT_PATH"/*; do
    

        getFilename $files
        getExtension $files
                
        if [ "$extension" == "xapk" ]; then
            echo "$filename: File has XAPK format. Skip analyze."
        else         
            echo "Decompiling: $filename"

            runApkTool $filename
            runTests $filename

            mv "$INPUT_PATH/$filename" "$INPUT_ANALYZED_PATH/$filename" 1>/dev/null
            mv "$OUTPUT_PATH/$filename" "$OUTPUT_ANALYZED_PATH/$filename" 1>/dev/null
        fi
        
        # New line between application for better readability
        printf "\n"

        # Move current apk line from apksList to apksList_analyzed
        lines=1
        head -n $lines $pathToApksList >> $pathToApksListAnalyzed
        sed -i -e "1,$lines d" $pathToApksList
    
    done
}

profilePath="./apksList-default.txt"

 while getopts "df:" OPTIONS; do
        case "${OPTIONS}" in
            f) 
                profilePath="${OPTARG}" ;;
            d)
                downloadApkMode=true

        esac
    done

main $profilePath $downloadApkMode
