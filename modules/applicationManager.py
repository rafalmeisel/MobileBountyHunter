import os
import re
import requests
from modules.directories import clearApplicationListFile
from modules.androidApplicationTester import runAndroidTests
import zipfile
import shutil

IS_GOOGLE_PLAY_APPLICATION_URL=False
IS_GOOGLE_PLAY_DEVELOPER_URL=False

IS_APK_EXTENSION=False
IS_XAPK_EXTENSION=False
IS_IPA_EXTENSION=False

GOOGLE_PLAY_URL_REGEX="https://play.google.com/"
GOOGLE_PLAY_APPLICATION_URL_SCHEMA="https://play.google.com/store/apps/details"
GOOGLE_PLAY_DEVELOPER_URL_SCHEMA="https://play.google.com/store/apps/dev"
GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_FILE_REGEX=r"\/store\/apps\/details\?id=([^&\"]+)"
GOOGLE_PLAY_DEVELOPER_BASE_URL_REGEX=r"(.+?)\?"
GOOGLE_PLAY_ID_VALUE_REGEX=r"id=(.+)"

IS_APP_STORE_APPLICATION_URL=False
IS_APP_STORE_DEVELOPER_URL=False
APP_STORE_URL_REGEX="https://apps.apple.com/"
APP_STORE_APPLICATION_URL_SCHEMA="https://apps.apple.com/pl/app/app-store-connect/id"
APP_STORE_DEVELOPER_URL_SCHEMA="https://apps.apple.com/pl/developer/apple/id"

def retrieveApplicationPackageNameFromGooglePlayApplication(APPLICATION_LIST_FILE_PATH, urlToAnalyze):

    applicationPackageNameMatch = re.search(GOOGLE_PLAY_ID_VALUE_REGEX, urlToAnalyze)
    applicationPackageName = str(applicationPackageNameMatch.group(1))
    print("Send Request to: " + urlToAnalyze)
    print("[Google Play][Application] Retrieved name: " + applicationPackageName)
    
    applicationListFile = open(APPLICATION_LIST_FILE_PATH, "a")
    applicationListFile.write(applicationPackageName)
    applicationListFile.close()

def retrieveApplicationPackageNameFromGooglePlayDeveloperProfile(APPLICATION_LIST_FILE_PATH, urlToAnalyze):
    # Examples:
    # https://play.google.com/store/apps/dev?id=5360036014478858866
    # https://play.google.com/store/apps/developer?id=Bethesda+Softworks+LLC
    
    # From string 'https://play.google.com/store/apps/developer?id=Developer' retrieve 'Developer'
    print("Analyzing: " + urlToAnalyze)

    androidDeveloperBaseUrlMatch=re.search(GOOGLE_PLAY_DEVELOPER_BASE_URL_REGEX, urlToAnalyze)
    androidDeveloperBaseUrl=str(androidDeveloperBaseUrlMatch.group(1))

    androidDeveloperNameMatch=re.search(GOOGLE_PLAY_ID_VALUE_REGEX, urlToAnalyze)
    androidDeveloperName=str(androidDeveloperNameMatch.group(1))
    androidDeveloperName=androidDeveloperName.replace("+", " ")

    params = {
    'id': androidDeveloperName,
    }

    googlePlayHttpResponse = requests.get(androidDeveloperBaseUrl, params=params)
    
    googlePlayHttpResponseCode = str(googlePlayHttpResponse.status_code)
    googlePlayHttpResponseContent = str(googlePlayHttpResponse.content)  

    if googlePlayHttpResponseCode == "200":
       
        matches = re.findall(GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_FILE_REGEX, googlePlayHttpResponseContent)
        
        retrievedApplicationsPackageNameConcatenation=""

        applicationListFile = open(APPLICATION_LIST_FILE_PATH, "a")
        for applicationPackageName in matches:
            applicationListFile.write(applicationPackageName+"\n")
            retrievedApplicationsPackageNameConcatenation = retrievedApplicationsPackageNameConcatenation + " " + applicationPackageName
        applicationListFile.close()

        print("Retrieved: " + retrievedApplicationsPackageNameConcatenation)
    else :
        print(urlToAnalyze + ": http response code: " + googlePlayHttpResponseCode)


def retrieveApplicationPackageNameFromAppStoreApplication(urlToAnalyze):
    
    print("TODO: retrieveApplicationPackageNameFromAppStoreApplication")

def retrieveApplicationPackageNameFromAppStoreDeveloperProfile():
     print("TODO: retrieveApplicationPackageNameFromAppStoreDeveloperProfile")


# Check if URL leads to Developer profile or directcly to application
def checkIfUrlLeadsToDeveloperOrApplication(USER_URL):
    
    global IS_GOOGLE_PLAY_APPLICATION_URL
    global IS_GOOGLE_PLAY_DEVELOPER_URL
    global IS_APP_STORE_APPLICATION_URL
    global IS_APP_STORE_DEVELOPER_URL

    if GOOGLE_PLAY_APPLICATION_URL_SCHEMA in USER_URL:
        IS_GOOGLE_PLAY_APPLICATION_URL = True

    elif GOOGLE_PLAY_DEVELOPER_URL_SCHEMA in USER_URL:
        IS_GOOGLE_PLAY_DEVELOPER_URL = True

    elif APP_STORE_APPLICATION_URL_SCHEMA in USER_URL: 
        IS_APP_STORE_APPLICATION_URL = True

    elif APP_STORE_DEVELOPER_URL_SCHEMA in USER_URL: 
        IS_APP_STORE_DEVELOPER_URL = True


def downloadApplicationFromStoreToInputDirectory(APPLICATION_PACKAGE_NAME, INPUT_DIRECTORY_PATH):

    print("Start downloading: " + APPLICATION_PACKAGE_NAME + " to directory " + INPUT_DIRECTORY_PATH)
    os.system("apkeep -a " + APPLICATION_PACKAGE_NAME + " " + INPUT_DIRECTORY_PATH)


def replaceWhiteSpaceWithDotsInApplicationPackageName(INPUT_DIRECTORY_PATH):

    filenames = os.listdir(INPUT_DIRECTORY_PATH)
    for filename in filenames:
        os.rename(os.path.join(INPUT_DIRECTORY_PATH, filename), os.path.join(INPUT_DIRECTORY_PATH, filename.replace(' ', '.').lower()))


def changeApplicationNameFromXapkToApk(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE):
    os.rename(INPUT_DIRECTORY_PATH + "XAPK_TEMP/" + APPLICATION_PACKAGE_NAME_FILE, INPUT_DIRECTORY_PATH + "XAPK_TEMP/" + APPLICATION_PACKAGE_NAME_FILE.replace(".xapk", ".apk"))


def unzipXapkFile(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE):
    print("unzipXapkFile: " + INPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME_FILE)

    with zipfile.ZipFile(INPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME_FILE, "r") as zip_ref:
            zip_ref.extractall(INPUT_DIRECTORY_PATH + "XAPK_TEMP/" + APPLICATION_PACKAGE_NAME_FILE)

    changeApplicationNameFromXapkToApk(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE)


def checkIfXapkIsValid(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE):

    if zipfile.is_zipfile (INPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME_FILE):
        return True
    else:
        return False


def decompileApkExtention(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH):
    print("Decompiling: " + APPLICATION_PACKAGE_NAME_FILE )
    os.system("apktool d " + INPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME_FILE + " -o " + OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME_FILE + " -f --quiet")


def decompileXapkExtention(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH):

    if checkIfXapkIsValid(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE):
        os.mkdir(INPUT_DIRECTORY_PATH + "XAPK_TEMP")
        os.chmod(INPUT_DIRECTORY_PATH + "XAPK_TEMP", 0o766)
        unzipXapkFile(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE)
        APPLICATION_PACKAGE_NAME_FILE = APPLICATION_PACKAGE_NAME_FILE.replace(".xapk", ".apk")
        decompileApkExtention(INPUT_DIRECTORY_PATH + "XAPK_TEMP/" + APPLICATION_PACKAGE_NAME_FILE + "/", APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH)
        shutil.rmtree(INPUT_DIRECTORY_PATH + "XAPK_TEMP")
    else :
        print ("File " + APPLICATION_PACKAGE_NAME_FILE + " is not valid ZIP file (or it is corrupted).")


def decompileSingleApplicationPackage(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH): 

    if ".xapk" in APPLICATION_PACKAGE_NAME_FILE:
        decompileXapkExtention(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH)
    elif ".apk" in APPLICATION_PACKAGE_NAME_FILE:
        decompileApkExtention(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH)


def decompileApplicationInInputDirectory(INPUT_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH):
    
    inputDirectoryApplicationPackageNames = os.listdir(INPUT_DIRECTORY_PATH)
    for APPLICATION_PACKAGE_NAME_FILE in inputDirectoryApplicationPackageNames:
        setFlagForApplicationStore(APPLICATION_PACKAGE_NAME_FILE)
        decompileSingleApplicationPackage(INPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME_FILE, OUTPUT_DIRECTORY_PATH)


# Read developersUrlsProfile.txt, retrieve applications package name from GET response, write it to file 
def prepareAppplicationListFileFromDevelopersUrlsProfileFile(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH):

    global IS_GOOGLE_PLAY_APPLICATION_URL
    global IS_GOOGLE_PLAY_DEVELOPER_URL
    global IS_APP_STORE_APPLICATION_URL
    global IS_APP_STORE_DEVELOPER_URL

    developerUrlsProfileFile = open(DEVELOPERS_URLS_PROFILE_FILE, 'r')
    developerUrlsProfileFileLines = developerUrlsProfileFile.readlines()
    
    clearApplicationListFile(APPLICATION_LIST_FILE_PATH)
    
    for urlToAnalyze in developerUrlsProfileFileLines:
        
        checkIfUrlLeadsToDeveloperOrApplication(urlToAnalyze)

        if (IS_GOOGLE_PLAY_APPLICATION_URL):
             retrieveApplicationPackageNameFromGooglePlayApplication(APPLICATION_LIST_FILE_PATH, urlToAnalyze)
        elif (IS_GOOGLE_PLAY_DEVELOPER_URL):
            retrieveApplicationPackageNameFromGooglePlayDeveloperProfile(APPLICATION_LIST_FILE_PATH, urlToAnalyze)
        elif (IS_APP_STORE_APPLICATION_URL):
            retrieveApplicationPackageNameFromAppStoreApplication(APPLICATION_LIST_FILE_PATH, urlToAnalyze)
        elif (IS_APP_STORE_DEVELOPER_URL):
            retrieveApplicationPackageNameFromAppStoreDeveloperProfile(APPLICATION_LIST_FILE_PATH, urlToAnalyze)


def setFlagForApplicationStore(filename):
    global IS_APK_EXTENSION
    global IS_XAPK_EXTENSION
    global IS_IPA_EXTENSION

    if ".apk" in filename:
        IS_APK_EXTENSION = True
    elif ".xapk" in filename: 
        IS_XAPK_EXTENSION = True
    elif ".ipa" in filename:
        IS_IPA_EXTENSION = True
    else:
        print("Unrecognized mobile application extension!")

def runTests(OUTPUT_DIRECTORY_PATH, RESULT_FILE_PATH):

    filenames = os.listdir(OUTPUT_DIRECTORY_PATH)

    for filename in filenames:
        setFlagForApplicationStore(filename)

        if IS_IPA_EXTENSION:
            print("App Store not Supported yet.")
        elif IS_APK_EXTENSION or IS_XAPK_EXTENSION:
            runAndroidTests(OUTPUT_DIRECTORY_PATH, RESULT_FILE_PATH)

def moveApplicationFromInputDirectoryToInputAnalyzedDirectory(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH):
    filenames = os.listdir(INPUT_DIRECTORY_PATH)
    for filename in filenames:
        shutil.move(INPUT_DIRECTORY_PATH + filename, INPUT_ANALYZED_DIRECTORY_PATH + filename)

def moveApplicationFromOutputDirectoryToOutputAnalyzedDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH):
    filenames = os.listdir(OUTPUT_DIRECTORY_PATH)
    for filename in filenames:
        shutil.move(OUTPUT_DIRECTORY_PATH + filename, OUTPUT_ANALYZED_DIRECTORY_PATH + filename)


def analyzeApplication(APPLICATION_PACKAGE_NAME, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH):

    downloadApplicationFromStoreToInputDirectory(APPLICATION_PACKAGE_NAME, INPUT_DIRECTORY_PATH)
    replaceWhiteSpaceWithDotsInApplicationPackageName(INPUT_DIRECTORY_PATH)
    decompileApplicationInInputDirectory(INPUT_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH)
    runTests(OUTPUT_DIRECTORY_PATH, RESULT_FILE_PATH)
    moveApplicationFromInputDirectoryToInputAnalyzedDirectory(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH)
    moveApplicationFromOutputDirectoryToOutputAnalyzedDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)


def analyzeInputDirectory(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH):
    
    decompileApplicationInInputDirectory(INPUT_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH)
    runTests(OUTPUT_DIRECTORY_PATH, RESULT_FILE_PATH)
    moveApplicationFromInputDirectoryToInputAnalyzedDirectory(INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH)
    moveApplicationFromOutputDirectoryToOutputAnalyzedDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)


def analyzeOutputDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH):
    
    runTests(OUTPUT_DIRECTORY_PATH, RESULT_FILE_PATH)
    # moveApplicationFromOutputDirectoryToOutputAnalyzedDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)


def analyzeApplicationFromList(APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH):

    applicationListFile = open(APPLICATION_LIST_FILE_PATH, "r")
    applicationPackageNames = applicationListFile.readlines()
    applicationListFile.close()

    for APPLICATION_PACKAGE_NAME in applicationPackageNames:
        APPLICATION_PACKAGE_NAME = APPLICATION_PACKAGE_NAME.replace("\n", "")
        analyzeApplication(APPLICATION_PACKAGE_NAME, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)


def runAnalyzeApplicationFromDeveloperProfileList(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH):

    prepareAppplicationListFileFromDevelopersUrlsProfileFile(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH)
    analyzeApplicationFromList(APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH, RESULT_FILE_PATH)
