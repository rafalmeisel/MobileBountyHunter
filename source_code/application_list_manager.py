import sys
import re
import os
import requests 
from source_code.config_file_manager import get_android_application_package_name_list_relative_path
from source_code.config_file_manager import get_ios_application_package_name_list_relative_path
from source_code.config_file_manager import get_android_store_urls_list_relative_path
from source_code.config_file_manager import get_ios_store_urls_list_relative_path

GOOGLE_PLAY_DEVELOPER_BASE_URL_REGEX=r"(.+?)\?"
GOOGLE_PLAY_ID_VALUE_REGEX=r"id=(.+)"
GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_FILE_REGEX=r"\/store\/apps\/details\?id=([^&\"]+)"

GOOGLE_PLAY_URL_REGEX="https://play.google.com/"

IS_APP_STORE_APPLICATION_URL=False
IS_APP_STORE_DEVELOPER_URL=False
APP_STORE_URL_REGEX="https://apps.apple.com/"

def append_to_android_application_package_name_list(application_package_name):

    android_application_package_name_list_relative_path = get_android_application_package_name_list_relative_path()
    android_application_package_name_list_file = open(android_application_package_name_list_relative_path, "a")
    android_application_package_name_list_file.write(application_package_name+"\n")
    android_application_package_name_list_file.close()


def append_to_ios_application_package_name_list(application_package_name):

    ios_application_package_name_list_relative_path = get_ios_application_package_name_list_relative_path()
    ios_application_package_name_list_file = open(ios_application_package_name_list_relative_path, "a")
    ios_application_package_name_list_file.write(application_package_name+"\n")
    ios_application_package_name_list_file.close()


def clear_ios_application_package_name_list():
    ios_application_package_name_list_relative_path = get_ios_application_package_name_list_relative_path()
    ios_application_package_name_list_file = open(ios_application_package_name_list_relative_path, "w").close()


def clear_android_application_package_name_list():
    android_application_package_name_list_relative_path = get_android_application_package_name_list_relative_path()
    android_application_package_name_list_file = open(android_application_package_name_list_relative_path, "w").close()


def retrieve_application_package_name_from_google_play_application_url(google_play_application_url):

    # Retrieve application package name from "https://play.google.com/store/apps/details?id=com.some.application" as "com.some.application"
    application_package_nameMatch = re.search(GOOGLE_PLAY_ID_VALUE_REGEX, google_play_application_url)
    application_package_name = str(application_package_nameMatch.group(1))
    
    print("[Google Play][Application] Retrieved name: " + application_package_name)
    
    append_to_android_application_package_name_list(application_package_name)


# Function take Url to Google Play, visit developer website, find all application related to this developer and paste them into file
# Example of URLs:
#   - Developer I: https://play.google.com/store/apps/dev?id=0000012345478858866
#   - Developer II: https://play.google.com/store/apps/developer?id=Some+Developer+Corp

# In this case we need to retrieve base url as: "https://play.google.com/store/apps/dev" or "https://play.google.com/store/apps/developer"
# in order to send valid GET request with separated parameters.
# Single GET request to developer profile as https://play.google.com/store/apps/dev?id=0000012345478858866 will not work.

def retrieve_application_package_names_from_google_play_developer_url(google_play_developer_url):
    
    print("\n")
    print("Analyzing: " + google_play_developer_url)

    # Retrieve developer base url as "https://play.google.com/store/apps/dev" or "https://play.google.com/store/apps/developer"
    android_developer_base_url_match = re.search(GOOGLE_PLAY_DEVELOPER_BASE_URL_REGEX, google_play_developer_url)
    android_developer_base_url = str(android_developer_base_url_match.group(1))

    # Retrieve developer name as "Some+Developer+Corp"
    android_developer_name_match = re.search(GOOGLE_PLAY_ID_VALUE_REGEX, google_play_developer_url)
    android_developer_name = str(android_developer_name_match.group(1))
    android_developer_name = android_developer_name.replace("+", " ")

    params = {
    'id': android_developer_name,
    }

    google_play_http_response = requests.get(android_developer_base_url, params=params)
    
    google_play_http_response_code = str(google_play_http_response.status_code)
    google_play_http_response_content = str(google_play_http_response.content)  

    if google_play_http_response_code == "200":
       
        application_package_names_found_on_developer_profile = re.findall(GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_FILE_REGEX, google_play_http_response_content)
        
        summary_retrieved_applications_package_name = ""
        
        for application_package_name in application_package_names_found_on_developer_profile:
            append_to_android_application_package_name_list(application_package_name)
            summary_retrieved_applications_package_name = summary_retrieved_applications_package_name + " " + application_package_name
        

        print("Retrieved: " + summary_retrieved_applications_package_name)
    else :
        print(google_play_developer_url + ": http response code: " + google_play_http_response_code)


def retrieve_application_package_name_from_appstore_application_url(appstore_application_url):
    
    print("TODO: retrieve_application_package_name_from_appstore_application_url")

def retrieve_application_package_name_from_appstore_developer_url(appstore_developer_url):
     print("TODO: retrieve_application_package_name_from_appstore_developer_url")


# Check if URL leads to Developer profile or directcly to application
def retrieve_android_application_package_name_from_store_url_to_applicatione_list_file():

    clear_android_application_package_name_list()
    
    store_urls_list_relative_path = get_android_store_urls_list_relative_path()

    try:
        with open(store_urls_list_relative_path, 'r') as store_urls_list_file:
            store_urls_list_file_contents = store_urls_list_file.readlines()
    
        for store_url in store_urls_list_file_contents:
            if "https://play.google.com/store/apps/details" in store_url:
                retrieve_application_package_name_from_google_play_application_url(store_url)

            elif "https://play.google.com/store/apps/dev" in store_url:
                retrieve_application_package_names_from_google_play_developer_url(store_url)

    except FileNotFoundError:
        try:
            with open(store_urls_list_relative_path, 'w') as store_urls_list_file:
                print("It seems that file 'android_store_urls_list.txt' did not exist. We created it for you. Please update it.")
        except IOError:
            print("An error occurred while creating the file: " + store_urls_list_relative_path)

        sys.exit(1)

    except IOError:
        print("An error occurred while reading the file: " + store_urls_list_relative_path)
        sys.exit(1)


# Check if URL leads to Developer profile or directcly to application
def retrieve_ios_application_package_name_from_store_url_to_applicatione_list_file():

    clear_ios_application_package_name_list()

    store_urls_list_relative_path = get_ios_store_urls_list_relative_path

    try:
        with open(store_urls_list_relative_path) as store_urls_list_file:
            store_urls_list_file_contents = store_urls_list_file.readlines()
    
        for store_url in store_urls_list_file_contents:
            if "https://apps.apple.com/pl/app/app-store-connect/id" in store_url: 
                retrieve_application_package_name_from_appstore_application_url(store_url)

            elif "https://apps.apple.com/pl/developer/apple/id" in store_url: 
                retrieve_application_package_name_from_appstore_developer_url(store_url)

    except FileNotFoundError:
        try:
            with open(store_urls_list_relative_path, 'w') as store_urls_list_file:
                print("It seems that file 'ios_store_urls_list.txt' did not exist. We created it for you. Please update it.")
        except IOError:
            print("An error occurred while creating the file: " + store_urls_list_relative_path)

        sys.exit(1)

    except IOError:
        print("An error occurred while reading the file: " + store_urls_list_relative_path)
        sys.exit(1)