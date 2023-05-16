from sourceCode.androidTests.checksAndroidManifest import *
from sourceCode.androidTests.checksResValuesStrings import *
from sourceCode.androidTests.checksFilesNames import *
from sourceCode.androidTests.checksJavaFiles import *
from sourceCode.androidTests.checksReportFile import *

import os
from termcolor import colored

ANDROID_MANIFEST_RELATIVE_FILE_PATH = ""
ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH = ""

def runAndroidTests(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME):
    
    outputDirectoryApplicationPackageNames = OUTPUT_DIRECTORY_PATH + "/" + APPLICATION_PACKAGE_NAME

    # if outputDirectoryApplicationPackageNames:
    #     first_folder = outputDirectoryApplicationPackageNames[0]
    resources_folder = os.path.join(outputDirectoryApplicationPackageNames, "resources")
    sources_folder = os.path.join(outputDirectoryApplicationPackageNames, "sources")

    # Application was decompiled with Jadx
    if os.path.isdir(resources_folder) and os.path.isdir(sources_folder):
        ANDROID_MANIFEST_RELATIVE_FILE_PATH = "/resources/AndroidManifest.xml"
        ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH = "/resources/res/values/strings.xml"
    
    # Application was decompiled with apktools
    else:
        ANDROID_MANIFEST_RELATIVE_FILE_PATH = "/AndroidManifest.xml"
        ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH = "/res/values/strings.xml"


    # for APPLICATION_PACKAGE_NAME in outputDirectoryApplicationPackageNames:
    print("Analyzing application: " + colored(APPLICATION_PACKAGE_NAME, 'cyan'))

    checksAndroidManifestDebuggable(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH)
    checksAndroidManifestAllowBackup(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH)
    checksAndroidManifestExported(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH)
    checksAndroidManifestCloudinary(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_MANIFEST_RELATIVE_FILE_PATH)
    
    checksResValuesStringsAwsLongTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringsAwsShortTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringsAwSecretAccessKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringsAwsBucket(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringsPushIoApplicationIdentifier(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringsFirebaseUrl(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringsAwsBucket(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringGoogleApiKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringGoogleCloudPlatformGoogleUserContent(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringGoogleOAuthAccessToken(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)
    checksResValuesStringGoogleAppSpot(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH)

    searchFilesWithSqliteExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)
    searchFilesWithDbExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)
    searchConfigFilesWithAnyExtensions(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)

    checksExportedActivityWithJavaScriptEnabled(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME)