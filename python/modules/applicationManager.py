import os
import re
import requests

IS_GOOGLE_PLAY_APPLICATION_URL=False
IS_GOOGLE_PLAY_DEVELOPER_URL=False
GOOGLE_PLAY_URL_REGEX="https://play.google.com/"
GOOGLE_PLAY_APPLICATION_URL_SCHEMA="https://play.google.com/store/apps/details?id="
GOOGLE_PLAY_DEVELOPER_URL_SCHEMA="https://play.google.com/store/apps/dev?id="
GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_REGEX=r'\"\/store\/apps\/details\?id=(.*?)\"'

IS_APP_STORE_APPLICATION_URL=False
IS_APP_STORE_DEVELOPER_URL=False
APP_STORE_URL_REGEX="https://apps.apple.com/"
APP_STORE_APPLICATION_URL_SCHEMA="https://apps.apple.com/pl/app/app-store-connect/id"
APP_STORE_DEVELOPER_URL_SCHEMA="https://apps.apple.com/pl/developer/apple/id"

def retrieveApplicationPackageNameFromGooglePlayApplication(APPLICATION_LIST_FILE, urlToAnalyze):

    googlePlayUrlApplicationRegexCompiled=re.compile(GOOGLE_PLAY_APPLICATION_URL_REGEX)
    applicationPackageName = re.search(googlePlayUrlApplicationRegexCompiled, urlToAnalyze)

    print("[Google Play][Application] Retrieved name: " + applicationPackageName)
    
    resultFile = open(APPLICATION_LIST_FILE, "a")
    resultFile.write(applicationPackageName)
    resultFile.close()

def retrieveApplicationPackageNameFromGooglePlayDeveloperProfile(APPLICATION_LIST_FILE, urlToAnalyze):
    # os.system("curl --silent "+urlToAnalyze+" --output ./response.txt")

    params = {
    'id': '8352141510294024214',
    }

    googlePlayHttpResponse = requests.get('https://play.google.com/store/apps/dev', params=params)

    # url = "https://play.google.com/store/search" # to jest adres URL Google Play
    # params = {"q": "python", "c": "apps"} # to są parametry zapytania
    # response = requests.get(urlToAnalyze) # to jest żądanie GET do Google Play
    # result = response.text # to jest tekstowa reprezentacja odpowiedzi
    # print(result) # to jest zmienna, która zawiera wynik zapytania

    # response = requests.get(urlToAnalyze)
    
    googlePlayHttpResponseCode = str(googlePlayHttpResponse.status_code)
    googlePlayHttpResponseContent = str(googlePlayHttpResponse.content)  

    if googlePlayHttpResponseCode == "200":
       
        matches = re.findall(GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_REGEX, googlePlayHttpResponseContent)

        resultFile = open(APPLICATION_LIST_FILE, "a")
        for applicationPackageName in matches:
            resultFile.write(applicationPackageName+"\n")
        resultFile.close()
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
    
# Read developersUrlsProfile.txt, retrieve applications package name from GET response, write it to file 
def prepareAppplicationListFileFromDevelopersUrlsProfileFile(APPLICATION_LIST_FILE, DEVELOPERS_URLS_PROFILE_FILE):

    global IS_GOOGLE_PLAY_APPLICATION_URL
    global IS_GOOGLE_PLAY_DEVELOPER_URL
    global IS_APP_STORE_APPLICATION_URL
    global IS_APP_STORE_DEVELOPER_URL


    # Using readlines()
    developerUrlsProfileFile = open(DEVELOPERS_URLS_PROFILE_FILE, 'r')
    developerUrlsProfileFileLines = developerUrlsProfileFile.readlines()

    for urlToAnalyze in developerUrlsProfileFileLines:
        
        checkIfUrlLeadsToDeveloperOrApplication(urlToAnalyze)

        if (IS_GOOGLE_PLAY_APPLICATION_URL):
             retrieveApplicationPackageNameFromGooglePlayApplication(APPLICATION_LIST_FILE, urlToAnalyze)
        elif (IS_GOOGLE_PLAY_DEVELOPER_URL):
            retrieveApplicationPackageNameFromGooglePlayDeveloperProfile(APPLICATION_LIST_FILE, urlToAnalyze)
        elif (IS_APP_STORE_APPLICATION_URL):
            retrieveApplicationPackageNameFromAppStoreApplication(APPLICATION_LIST_FILE, urlToAnalyze)
        elif (IS_APP_STORE_DEVELOPER_URL):
            retrieveApplicationPackageNameFromAppStoreDeveloperProfile(APPLICATION_LIST_FILE, urlToAnalyze)