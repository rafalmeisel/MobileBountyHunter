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

    # Decompile all apks in "input" directory and run tests
    for files in ./input/*; do

        filename=$(basename -- "$files")

        echo "Decompiling: $filename"
        apktool d "$(pwd)/input/$filename" -o "$(pwd)/output/$filename" -f

        grep -i "firebase.io" "$(pwd)/output/$filename/res/values/strings.xml"
    done
fi