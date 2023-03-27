from termcolor import colored
import re

def checksResValuesStringsAwsAkid(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsAkidRegex=r'>(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])<'
    awsAkidFalseText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS AKID: " + awsAkidValue)

    if len(awsAkidValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS AKID: ", colored(awsAkidValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS AKID: ", colored(awsAkidFalseText, 'blue'))

    resultFile.close()


def checksResValuesStringsAwSecretKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsSecretKeyRegex=r'>(?<![A-Za-z0-9+=])[A-Za-z0-9+=]{40}(?![A-Za-z0-9+=])<'
    awsSecretKeyFalseText='Not found'
    awsSecretKeyValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsSecretKeyRegex, line):
            awsSecretKeyMatch =  re.search(awsSecretKeyRegex, line)
            awsSecretKeyValue = awsSecretKeyMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Secret Key: " + awsSecretKeyValue)

    if len(awsSecretKeyValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Secret Key: ", colored(awsSecretKeyValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Secret Key: ", colored(awsSecretKeyFalseText, 'blue'))

    resultFile.close()


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


def checksResValuesStringsPushIoApplicationIdentifier(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    pushIoApplicationIdentifierRegex=r'"pio-.*"'
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

def checksResValuesStringsFirebaseUrl(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    # firebaseUrlRegex = r'https.*firebaseio.com'
    firebaseUrlRegex = r'https.*firebaseio.com'
    firebaseFalseText='Not found'
    firebaseValue=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    resultFile = open(RESULT_FILE_PATH, "a")

    for line in resValuesStringsFileContent:
        if re.search(firebaseUrlRegex, line):
            firebaseMatch =  re.search(firebaseUrlRegex, line)
            firebaseValue = firebaseMatch.group()
            resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + firebaseValue)

    if len(firebaseValue) > 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: ", colored(firebaseValue, 'red'))
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: ", colored(firebaseFalseText, 'blue'))

    resultFile.close()