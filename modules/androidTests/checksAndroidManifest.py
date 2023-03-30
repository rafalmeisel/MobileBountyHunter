from termcolor import colored
import re

def checksAndroidManifestDebuggable(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    debuggableActivityTrueRegex='.*debuggable="true".*'
    debuggableActivityTypeValue=""
    debuggableActivityTypeRegex='(?:<)(.*?) (?=android)'
    debuggableActivityNameValue=""
    debuggableActivityNameRegex='(?:(name="))(.*?)(?=")'
    isDebuggableFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(debuggableActivityTrueRegex, line):
            if re.search(debuggableActivityNameRegex, line):
                debuggableActivityNameValue = str(re.search(debuggableActivityNameRegex, line).group(2))

            debuggableActivityTypeValue = str(re.search(debuggableActivityTypeRegex, line).group(1))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: debug:" + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: debug:", colored(debuggableActivityTypeValue + ":" + debuggableActivityNameValue, 'red'))
            isDebuggableFlag = True

        else:
            isDebuggableFlag = isDebuggableFlag or False

    if not isDebuggableFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: debug:", colored("False", 'blue'))       

    resultFile.close()


def checksAndroidManifestAllowBackup(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    allowBackupActivityTrueRegex='.*allowBackup="true".*'
    allowBackupActivityTypeValue=""
    allowBackupActivityTypeRegex='(?:<)(.*?) (?=android)'
    allowBackupActivityNameValue=""
    allowBackupActivityNameRegex='(?:(name="))(.*?)(?=")'
    isAllowBackupFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(allowBackupActivityTrueRegex, line):
            if re.search(allowBackupActivityNameRegex, line):
                allowBackupActivityNameValue = str(re.search(allowBackupActivityNameRegex, line).group(2))
            
            allowBackupActivityTypeValue = str(re.search(allowBackupActivityTypeRegex, line).group(1))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: allowBackup:" + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: allowBackup:", colored(allowBackupActivityTypeValue + ":" + allowBackupActivityNameValue, 'red'))
            isAllowBackupFlag = True
            
        else:
            isAllowBackupFlag= isAllowBackupFlag or False

    if not isAllowBackupFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: allowBackup:", colored("False", 'blue'))

    resultFile.close()

def checksAndroidManifestExported(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    exportedActivityTrueRegex='.*exported="true".*'
    exportedActivityTypeValue=""
    exportedActivityTypeRegex='(?:<)(.*?) (?=android)'
    exportedActivityNameValue=""
    exportedActivityNameRegex='(?:(name="))(.*?)(?=")'
    isExportedFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidManifestFileContent:
        if re.search(exportedActivityTrueRegex, line):
            if re.search(exportedActivityNameRegex, line):
                exportedActivityNameValue = str(re.search(exportedActivityNameRegex, line).group(2))
            
            exportedActivityTypeValue = str(re.search(exportedActivityTypeRegex, line).group(1))
            resultFile.write(APPLICATION_PACKAGE_NAME + ": AndroidManifest: exported:" + line)
            print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: exported:", colored(exportedActivityTypeValue + ":" + exportedActivityNameValue, 'red'))
            isExportedFlag = True
        
        else:
            isExportedFlag= isExportedFlag or False

    if not isExportedFlag:
        print(APPLICATION_PACKAGE_NAME + ": AndroidManifest: exported:", colored("False", 'blue'))

    resultFile.close()