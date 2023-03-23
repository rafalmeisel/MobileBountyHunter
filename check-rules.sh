#!/bin/bash

RED='\e[1;31m'
BLUE='\e[1;34m'
NO_COLOR='\e[0m' # No Color

checksAndroidManifestDebuggable () {
    filename=$1
    if grep --silent -i 'debuggable="true"' "$filename/AndroidManifest.xml"; then
        echo -e "$filename: AndroidManifest: ${RED}debuggable=true${NO_COLOR}\n"

        echo -e "$filename : debuggable=\"true\" : $filename/AndroidManifest.xml" >> "./results.txt"
        grep -n -i 'debuggable="true"' "$filename/AndroidManifest.xml" >> "./results.txt"
        echo -e "\n" >> "./results.txt"
    else
        echo -e "$filename: AndroidManifest: ${BLUE}debuggable=false${NO_COLOR}\n"
    fi
}

checksAndroidManifestAllowBackup () {
    filename=$1
    if grep --silent -i 'allowBackup="true"' "$filename/AndroidManifest.xml"; then
        echo -e "$filename: AndroidManifest: ${RED}allowBackup=true${NO_COLOR}\n"

        echo -e "$filename : allowBackup=\"true\" : $filename/AndroidManifest.xml" >> "./results.txt"
        grep -n -i 'allowBackup="true"' "$filename/AndroidManifest.xml" >> "./results.txt"
        echo -e "\n" >> "./results.txt"
    else
        printf "$filename: AndroidManifest: ${BLUE}allowBackup=false${NO_COLOR}\n"
    fi
}

# checksValuesStringGoogleApiKey () {
#     echo "-> checksValuesStringGoogleApiKey"
#     if grep --silent -i 'google_api_key' "./strings.xml"; then
#         google_api_key="$(grep --silent -o -i 'google_api_key')"
#         echo "$filename: google_api_key = ${LIGHT_BLUE}$google_api_key${NC}"
#         grep "$filename: ${LIGHT_BLUE}$google_api_key${NC}" >> "results.txt"
#     fi
# }

checksStringsAwsAkid () {
    filename=$1
    awsAkidRegex=">(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])<"
    
    if grep --silent -oP "$awsAkidRegex" "$filename/res/values/strings.xml"; then
        
        AWS_AKID="$(grep -oP "$awsAkidRegex" "$filename/res/values/strings.xml")"
        AWS_AKID="${AWS_AKID:1:-1}"

        printf "$filename: AWS_AKID: ${RED}$AWS_AKID${NO_COLOR}\n"

        echo -e "$filename : AWS_AKID: $AWS_AKID : $filename/res/values/strings.xml" >> "$RESULT_FILE"
        grep -n -oP "$awsAkidRegex" "$filename/res/values/strings.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AWS_AKID: ${BLUE}Not found${NO_COLOR}\n"
    fi
}

checksStringsAwsSecretKey () {
    filename=$1
    awsSecretKeyRegex=">(?<![A-Za-z0-9+=])[A-Za-z0-9+=]{40}(?![A-Za-z0-9+=])<"

    if grep --silent -oP "$awsSecretKeyRegex" "$filename/res/values/strings.xml"; then
        
        AWS_SECRET_KEY="$(grep -oP "$awsSecretKeyRegex" "$filename/res/values/strings.xml")"
        AWS_SECRET_KEY="${AWS_SECRET_KEY:1:-1}"

        printf "$filename: AWS_SECRET_KEY: ${RED}$AWS_SECRET_KEY${NO_COLOR}\n"

        echo -e "$filename : AWS_SECRET_KEY: $AWS_SECRET_KEY : $filename/res/values/strings.xml" >> "$RESULT_FILE"
        grep -n -oP "$awsSecretKeyRegex" "$filename/res/values/strings.xml" >> "$RESULT_FILE"
        echo -e "\n" >> "$RESULT_FILE"
    else
        printf "$filename: AWS_SECRET_KEY: ${BLUE}Not found${NO_COLOR}\n"
    fi
}

filename="check-rules"

checksAndroidManifestDebuggable $filename
checksAndroidManifestAllowBackup $filename
# checksValuesStringGoogleApiKey $filename
# checksAPIkeys $filename
# checksFirebasePermission $filename
checksStringsAwsAkid $filename
checksStringsAwsSecretKey $filename