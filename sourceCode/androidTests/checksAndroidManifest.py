from termcolor import colored
import re
from sourceCode.reporting import report
from sourceCode.reporting import reportEnums

# Interesting things in AndroidManifest:
# - Exported components
# - Api keys
# - Custom deep link schemas
# - http deep link scheme
# - Deep link hosts
# - Schema endpoints
# - Deep link pathPatterns

def checksAndroidManifestDebuggable(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH):
    
    debuggableActivityTrueRegex='.*debuggable="true".*'
    debuggableActivityTypeValue=""
    debuggableActivityTypeRegex='(?:<)(.*?) (?=android)'
    debuggableActivityNameValue=""
    debuggableActivityNameRegex='(?:(name="))(.*?)(?=")'
    isDebuggableFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()

    for line in androidManifestFileContent:
        if re.search(debuggableActivityTrueRegex, line):
            if re.search(debuggableActivityNameRegex, line):
                debuggableActivityNameValue = str(re.search(debuggableActivityNameRegex, line).group(2))

            debuggableActivityTypeValue = str(re.search(debuggableActivityTypeRegex, line).group(1))

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "Debug", debuggableActivityTypeValue + ":" + debuggableActivityNameValue)
            
            isDebuggableFlag = True

        else:
            isDebuggableFlag = isDebuggableFlag or False

    if not isDebuggableFlag:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "Debug")


def checksAndroidManifestAllowBackup(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH):
    
    allowBackupActivityTrueRegex='.*allowBackup="true".*'
    allowBackupActivityTypeValue=""
    allowBackupActivityTypeRegex='(?:<)(.*?) (?=android)'
    allowBackupActivityNameValue=""
    allowBackupActivityNameRegex='(?:(name="))(.*?)(?=")'
    isAllowBackupFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()
   
    for line in androidManifestFileContent:
        if re.search(allowBackupActivityTrueRegex, line):
            if re.search(allowBackupActivityNameRegex, line):
                allowBackupActivityNameValue = str(re.search(allowBackupActivityNameRegex, line).group(2))
            
            allowBackupActivityTypeValue = str(re.search(allowBackupActivityTypeRegex, line).group(1))
            
            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "allowBackup", allowBackupActivityTypeValue + ":" + allowBackupActivityNameValue)
            
            isAllowBackupFlag = True
            
        else:
            isAllowBackupFlag= isAllowBackupFlag or False

    if not isAllowBackupFlag:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "allowBackup")

def checksAndroidManifestExported(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH):
    
    exportedActivityTrueRegex='.*exported="true".*'
    exportedActivityTypeValue=""
    exportedActivityTypeRegex='(?:<)(.*?) (?=android)'
    exportedActivityNameValue=""
    exportedActivityNameRegex='(?:(name="))(.*?)(?=")'
    isExportedFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in androidManifestFileContent:
        if re.search(exportedActivityTrueRegex, line):
            if re.search(exportedActivityNameRegex, line):
                exportedActivityNameValue = str(re.search(exportedActivityNameRegex, line).group(2))
            
            exportedActivityTypeValue = str(re.search(exportedActivityTypeRegex, line).group(1))

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "exported", exportedActivityTypeValue + ":" + exportedActivityNameValue)

            isExportedFlag = True
        
        else:
            isExportedFlag= isExportedFlag or False

    if not isExportedFlag:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "exported")


def checksAndroidManifestCloudinary(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH):
    
    cloudinaryRegex='cloudinary:\/\/.*(?="|\')'
    cloudinaryValue=""
    isCloudinaryFlag=False

    androidManifestFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_MANIFEST_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in androidManifestFileContent:
        if re.search(cloudinaryRegex, line):
            cloudinaryValue = re.search(cloudinaryRegex, line).group(0)

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "Cloudinary", str(cloudinaryValue))

            isCloudinaryFlag = True
        
        else:
            isCloudinaryFlag= isCloudinaryFlag or False

    if not isCloudinaryFlag:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "AndroidManifest", "Cloudinary")