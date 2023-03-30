from termcolor import colored
import re

def checksAndroidManifestDebuggable(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    debuggableTrueRegex='.*debuggable="true".*'
    debuggableTrueText='debuggable="true"'
    debuggableFalseText='debuggable="false"'
    ifDebuggableFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(debuggableTrueRegex, line):
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: " + debuggableTrueText + " : " + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: ", colored(debuggableTrueText, 'red'))
            ifDebuggableFlag = True

        else:
            ifDebuggableFlag = ifDebuggableFlag or False

    if not ifDebuggableFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: ", colored(debuggableFalseText, 'blue'))       

    resultFile.close()


def checksAndroidManifestAllowBackup(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    allowBackupTrueRegex='.*allowBackup="true".*'
    allowBackupTrueText='allowBackup="true"'
    allowBackupFalseText='allowBackup="false"'
    ifAllowBackupFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(allowBackupTrueRegex, line):
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: " + allowBackupTrueText + " : " + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: ", colored(allowBackupTrueText, 'red'))
            ifAllowBackupFlag = True
            
        else:
            ifAllowBackupFlag= ifAllowBackupFlag or False

    if not ifAllowBackupFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: ", colored(allowBackupFalseText, 'blue'))

    resultFile.close()

def checksAndroidManifestExported(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    exportedTrueRegex='.*exported="true".*'
    exportedTrueText='exported="true"'
    exportedFalseText='exported="false"'
    ifExportedFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(exportedTrueRegex, line):
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: " + exportedTrueText + " : " + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: ", colored(exportedTrueText, 'red'))
            ifExportedFlag = True
        
        else:
            ifExportedFlag= ifExportedFlag or False

    if not ifExportedFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: ", colored(exportedFalseText, 'blue'))

    resultFile.close()