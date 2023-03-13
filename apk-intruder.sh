#!/bin/bash

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
    echo "Directory 'input' with apks inside"
else
    if [ ! -d ./output ] 
    then
        mkdir ./output
    fi

    # Create result file
    echo "=== Results ===" > "$(pwd)/output/results.txt"
    chmod 766 "$(pwd)/output/results.txt"

    # Decompile all apks in "input" directory and run tests
    for files in ./input/*; do

        filename=$(basename -- "$files")

        echo ""
        echo "########################################"
        echo "##### $filename"
        echo "########################################"
        echo ""
        
        echo "Decompiling: $filename"

        apktool d "$(pwd)/input/$filename" -o "$(pwd)/output/$filename" -f

        # https://book.hacktricks.xyz/mobile-pentesting/android-app-pentesting

        echo "= $filename =" > "$(pwd)/output/results.txt"
        
        # Check if application is debbugeable
        grep -i 'debuggable="true"' "$(pwd)/output/$filename/AndroidManifest.xml"
        grep -i 'debuggable="true"' "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"

        # Check if application make a backup
        grep -i 'android:allowBackup="true"' "$(pwd)/output/$filename/AndroidManifest.xml"
        grep -i 'android:allowBackup="true"' "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"

        # Check if application has Api Keys
        grep -i "apikey" "$(pwd)/output/$filename/AndroidManifest.xml"
        grep -i "apikey" "$(pwd)/output/$filename/AndroidManifest.xml" >> "$(pwd)/output/results.txt"

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

    done
fi