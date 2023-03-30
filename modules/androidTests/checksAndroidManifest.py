from termcolor import colored
import re

def checksAndroidManifestDebuggable(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    debuggableTrueRegex='.*debuggable="true".*'
    debuggableActivityNameRegex='(?:(name="))(.*?)(?=")'
    ifDebuggableFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(debuggableTrueRegex, line):
            debuggableActivityName = str(re.search(debuggableActivityNameRegex, line).group(2))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: debug:" + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: debug:", colored(debuggableActivityName, 'red'))
            ifDebuggableFlag = True

        else:
            ifDebuggableFlag = ifDebuggableFlag or False

    if not ifDebuggableFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: debug:", colored("False", 'blue'))       

    resultFile.close()


def checksAndroidManifestAllowBackup(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    allowBackupTrueRegex='.*allowBackup="true".*'
    allowBackupActivityNameRegex='(?:(name="))(.*?)(?=")'
    ifAllowBackupFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(allowBackupTrueRegex, line):
            allowBackupActivityName = str(re.search(allowBackupActivityNameRegex, line).group(2))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: allowBackup:" + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: allowBackup:", colored(allowBackupActivityName, 'red'))
            ifAllowBackupFlag = True
            
        else:
            ifAllowBackupFlag= ifAllowBackupFlag or False

    if not ifAllowBackupFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: allowBackup:", colored("False", 'blue'))

    resultFile.close()

def checksAndroidManifestExported(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    exportedTrueRegex='.*exported="true".*'
    exportedActivityNameRegex='(?:(name="))(.*?)(?=")'
    ifExportedFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(exportedTrueRegex, line):
            exportedActivityName = str(re.search(exportedActivityNameRegex, line).group(2))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: exported:" + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: exported:", colored(exportedActivityName, 'red'))
            ifExportedFlag = True
        
        else:
            ifExportedFlag= ifExportedFlag or False

    if not ifExportedFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: exported:", colored("False", 'blue'))

    resultFile.close()