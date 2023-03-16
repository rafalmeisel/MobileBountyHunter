#!/bin/bash

checksDebuggable () {
    filename=$1

    # Check if application is debbugeable
    if grep -i 'debuggable="true"' "$(pwd)/output/$filename/AndroidManifest.xml"; then
        echo "$filename: debuggable=true"
        grep -i 'debuggable="true"' "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"
    else
        echo "$filename: debuggable=false"
    fi
}

checksAllowBackup () {
    filename=$1
    #TODO: Check grep output -> Reduce message
    #Check if application make a backup
    if grep -i 'allowBackup="true"' "$(pwd)/output/$filename/AndroidManifest.xml"; then
        echo "$filename: allowBackup=true"
        grep -i 'allowBackup="true"' "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"
    else
        echo "$filename: allowBackup=false"
    fi
}

checksAPIkeys (){
    filename=$1

     # Check if application has Api Keys
    grep -i "apikey" "$(pwd)/output/$filename/AndroidManifest.xml"
    grep -i "apikey" "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"
}

checksFirebasePermission (){
    filename=$1
    
    # Check URL for firebase
    FIREBASE_DATABASE_URL="$(grep -o https.*firebaseio.com "$(pwd)/output/$filename/res/values/strings.xml")"

    echo "FIREBASE_DATABASE_URL=$FIREBASE_DATABASE_URL"

    # Test curl
    FIREBASE_DATABASE_JSON=$FIREBASE_DATABASE_URL"/.json"

    FIREBASE_DATABASE_RESPONSE="$(curl --silent $FIREBASE_DATABASE_JSON)"
    FIREBASE_DATABASE_RESPONSE_BODY="$(grep -o {[\r\n].*[\r\n]+} "$FIREBASE_DATABASE_RESPONSE")"
    
    # echo "$FIREBASE_DATABASE_RESPONSE_BODY"

    if [[ $FIREBASE_DATABASE_RESPONSE_BODY == *"Permission denied"* ]]; then
        echo "$FIREBASE_DATABASE_URL: is not vulnerable..."
        echo "$FIREBASE_DATABASE_URL: is not vulnerable..." >> "$(pwd)/output/results.txt"
    else
        echo "$FIREBASE_DATABASE_URL: is POTENTIALLY vulnerable: $FIREBASE_DATABASE_RESPONSE_BODY"  
        echo "$FIREBASE_DATABASE_URL: is POTENTIALLY vulnerable!!!" >> "$(pwd)/output/results.txt"

        echo "$(pwd)/output/results.txt"
        echo "FIREBASE_DATABASE_RESPONSE: $FIREBASE_DATABASE_RESPONSE_BODY" >> "$(pwd)/output/results.txt"
    fi

}

while getopts 'd' OPTION; do
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

# Create result file
echo "=== Results ===" > "$(pwd)/output/results.txt"
chmod 766 "$(pwd)/output/results.txt"

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

        echo "= $filename =" > "$(pwd)/output/results.txt"
        
        checksDebuggable $filename
        checksAllowBackup $filename
        checksAPIkeys $filename
        checksFirebasePermission $filename
    fi
done



