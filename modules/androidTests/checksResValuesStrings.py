from termcolor import colored
import re
import requests


def checksResValuesStringsAwsLongTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsAkidRegex=r'(?<=>)AK(\S*?)(?=<)'
    awsAkidFalseText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Long Term Access Key: " + awsAkidValue)

    if len(awsAkidValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Long Term Access Key: ", colored(awsAkidValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Long Term Access Key: ", colored(awsAkidFalseText, 'blue'))

    resultFile.close()


def checksResValuesStringsAwsShortTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsAkidRegex=r'(?<=>)AS(\S*?)(?=<)'
    awsAkidFalseText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Short Term Access Key: " + awsAkidValue)

    if len(awsAkidValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Short Term Access Key: ", colored(awsAkidValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Short Term Access Key: ", colored(awsAkidFalseText, 'blue'))

    resultFile.close()


def checksResValuesStringsAwSecretAccessKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsSecretKeyRegex=r'(?:(AWS|aws).*>)(\S*)(?=<)'
    awsSecretKeyFalseText='Not found'
    awsSecretKeyValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsSecretKeyRegex, line):
            awsSecretKeyMatch =  re.search(awsSecretKeyRegex, line)
            awsSecretKeyValue = awsSecretKeyMatch.group(2)

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Secret Key: " + awsSecretKeyValue)

    if len(awsSecretKeyValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Secret Key: ", colored(awsSecretKeyValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Secret Key: ", colored(awsSecretKeyFalseText, 'blue'))

    resultFile.close()

# To check
def checksResValuesStringsAwsUrl(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsUrlRegex=r"http.*amazonaws.com"
    awsUrlFalseText='Not found'
    awsUrlValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsUrlRegex, line):
            awsUrlMatch =  re.search(awsUrlRegex, line)
            awsUrlValue = awsUrlMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS URL: " + awsUrlValue)

    if len(awsUrlValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS URL: ", colored(awsUrlValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS URL: ", colored(awsUrlFalseText, 'blue'))

    resultFile.close()


# https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop-mobile/ios/in-app-msg.htm
def checksResValuesStringsPushIoApplicationIdentifier(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    pushIoApplicationIdentifierRegex=r'pio-([^<]+)'
    pushIoApplicationIdentifierFalseText='Not found'
    pushIoApplicationIdentifierValue=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in resValuesStringsFileContent:
        if re.search(pushIoApplicationIdentifierRegex, line):
            pushIoApplicationIdentifierMatch =  re.search(pushIoApplicationIdentifierRegex, line)
            pushIoApplicationIdentifierValue = pushIoApplicationIdentifierMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: PushIoApplicationIdentifier: " + pushIoApplicationIdentifierValue)

    if len(pushIoApplicationIdentifierValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: PushIoApplicationIdentifier: ", colored(pushIoApplicationIdentifierValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: PushIoApplicationIdentifier: ", colored(pushIoApplicationIdentifierFalseText, 'blue'))

    resultFile.close()


def checkFirabasePermission(APPLICATION_PACKAGE_NAME, firebaseUrl):
    response = requests.get(firebaseUrl + "/.json")
    data = str(response.json())

    if "Permission denied" in data:
        print(APPLICATION_PACKAGE_NAME + ": Firebase: " + colored(data, 'blue'))
    elif len(data) == 0:
        print(APPLICATION_PACKAGE_NAME + ": Firebase: " + colored(data, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": Firebase: " + colored(data, 'yellow'))


def checksResValuesStringsFirebaseUrl(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    firebaseUrlRegex = r'https.*firebaseio.com'
    firebaseFalseText='Not found'
    firebaseUrl=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    resultFile = open(RESULT_FILE_PATH, "a")

    for line in resValuesStringsFileContent:
        if re.search(firebaseUrlRegex, line):
            firebaseMatch =  re.search(firebaseUrlRegex, line)
            firebaseUrl = firebaseMatch.group()
            resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + firebaseUrl)

    if len(firebaseUrl) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: ", colored(firebaseUrl, 'red'))
        checkFirabasePermission(APPLICATION_PACKAGE_NAME, firebaseUrl)
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: ", colored(firebaseFalseText, 'blue'))

    resultFile.close()
