#!/bin/bash

RED='\e[1;31m'
BLUE='\e[1;34m'
CLEAR_COLOR='\e[0m' # No Color

# Worth to check
# - google_api_key
# - google_app_id
# - google_crash_reporting_api_key
# - google_storage_bucket
# - MAPS_API_KEY

checksAndroidManifestDebuggable () {
    filename=$1
    if grep --silent -i 'debuggable="true"' "$(pwd)/output/$filename/AndroidManifest.xml"; then
        echo -e "$filename: AndroidManifest: ${RED}debuggable=true${CLEAR_COLOR}\n"

        echo -e "$filename : debuggable=\"true\" : $(pwd)/output/$filename/AndroidManifest.xml" >> "./results.txt"
        grep -n -i 'debuggable="true"' "$(pwd)/output/$filename/AndroidManifest.xml" >> "./results.txt"
        echo -e "\n" >> "./results.txt"
    else
        echo -e "$filename: AndroidManifest: ${BLUE}debuggable=false${CLEAR_COLOR}\n"
    fi
}

checksAndroidManifestAllowBackup () {
    filename=$1
    if grep --silent -i 'allowBackup="true"' "$(pwd)/output/$filename/AndroidManifest.xml"; then
        echo -e "$filename: AndroidManifest: ${RED}allowBackup=true${CLEAR_COLOR}\n"

        echo -e "$filename : allowBackup=\"true\" : $(pwd)/output/$filename/AndroidManifest.xml" >> "./results.txt"
        grep -n -i 'allowBackup="true"' "$(pwd)/output/$filename/AndroidManifest.xml" >> "./results.txt"
        echo -e "\n" >> "./results.txt"
    else
        printf "$filename: AndroidManifest: ${BLUE}allowBackup=false${CLEAR_COLOR}\n"
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

# checksFirebasePermission (){
#     filename=$1
    
#     # Check URL for firebase
#     FIREBASE_DATABASE_URL="$(grep --silent -o https.*firebaseio.com "$(pwd)/output/$filename/res/values/strings.xml")"

    

#     # Test curl
#     FIREBASE_DATABASE_JSON=$FIREBASE_DATABASE_URL"/.json"

#     echo "echo $filename: $FIREBASE_DATABASE_JSON"

#     FIREBASE_DATABASE_RESPONSE="$(curl --silent $FIREBASE_DATABASE_JSON)"
#     FIREBASE_DATABASE_RESPONSE_BODY="$(grep --silent -o {[\r\n].*[\r\n]+} "$FIREBASE_DATABASE_RESPONSE")"
    
#     # echo "$FIREBASE_DATABASE_RESPONSE_BODY"

#     echo "echo $filename: $FIREBASE_DATABASE_RESPONSE_BODY"

#     if [[ $FIREBASE_DATABASE_RESPONSE_BODY == *"Permission denied"* ]]; then
#         echo "$FIREBASE_DATABASE_URL: is not vulnerable..."
#         echo "$FIREBASE_DATABASE_URL: is not vulnerable..." >> "$(pwd)/output/results.txt"
#     else
#         echo "$FIREBASE_DATABASE_URL: is POTENTIALLY vulnerable: $FIREBASE_DATABASE_RESPONSE_BODY"  
#         echo "$FIREBASE_DATABASE_URL: is POTENTIALLY vulnerable!!!" >> "$(pwd)/output/results.txt"

#         echo "$(pwd)/output/results.txt"
#         echo "FIREBASE_DATABASE_RESPONSE: $FIREBASE_DATABASE_RESPONSE_BODY" >> "$(pwd)/output/results.txt"
#     fi

# }

runTests (){
    filename=$1
    
    checksAndroidManifestDebuggable $filename
    checksAndroidManifestAllowBackup $filename
    # checksValuesStringGoogleApiKey $filename
    # checksAPIkeys $filename
    # checksFirebasePermission $filename
}

while getopts 'df' OPTION; do
  case "$OPTION" in
    d)
      echo "Download apks from file"
      downloadAndDecompileApksFromInput=true
      ;;
  esac
done

if [ ! -f /home/kali/.cargo/bin/rustc ]
then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    source "$HOME/.cargo/env"
fi

if [ ! -f /home/kali/.cargo/bin/apkeep ]
then
    sudo apt install libssl-dev
    sudo apt install pkg-config -y
    cargo install apkeep --locked


fi

if [ ! -f /usr/local/bin/apktool.jar ]
then
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

if [ ! -d ./input ] 
then
    mkdir ./input
    echo "Directory 'input' created. Please provide .apk in ./input or run the script with -d to download .apks from list."

fi
  
if [ ! -d ./output ] 
then
    mkdir ./output
    echo "Directory 'output' created."
fi

PATH_TO_APKS="./input/*"

if [ "$downloadAndDecompileApksFromInput" ] ; then
    if [ ! -d ./newApks ]
    then
        mkdir ./newApks/
    fi

    PATH_TO_APKS="./newApks/*"
    PATH_TO_LIST="./apksList.txt"

    while read apkToDownload; do
        echo "Start downloading: $apkToDownload"
        apkeep -a $apkToDownload ./newApks/
    done < "$PATH_TO_LIST"
    
fi

for files in $PATH_TO_APKS; do
    filename=$(basename -- "$files")
    filenameWithoutWhiteSpace="${filename// /.}"

    mv -vn "$(pwd)/input/$filename" "$(pwd)/input/$filenameWithoutWhiteSpace"
done

# Create result file
echo "=== Results ===" > "$(pwd)/output/results.txt"
chmod 766 "$(pwd)/results.txt"

if [scanSpecificApk]; then
    runTests $filename
else

    # Decompile all apks in "input" directory and run tests
    for files in $PATH_TO_APKS; do

        filename=$(basename -- "$files")
        extension="${filename##*.}"
        echo "Extention is: $extension"
        
        if [ "$extension" == "xapk" ]; then
            echo "File has XAPK format. Skip analyze."
        else
            echo ""
            echo "########################################"
            echo "##### $filename"
            echo "########################################"
            echo ""
            
            echo "Decompiling: $filename"
            
            if [ "$downloadAndDecompileApksFromInput" ]; then
                mv "$(pwd)/newApks/$filename" "$(pwd)/input/$filename"
            fi

            apktool d "$(pwd)/input/$filename" -o "$(pwd)/output/$filename" -f

            # https://book.hacktricks.xyz/mobile-pentesting/android-app-pentesting
            
            runTests $filename
        fi
    done
fi


