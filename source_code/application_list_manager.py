import re
import requests
import source_code.config_file_manager

GOOGLE_PLAY_DEVELOPER_BASE_URL_REGEX=r"(.+?)\?"
GOOGLE_PLAY_ID_VALUE_REGEX=r"id=(.+)"
GOOGLE_PLAY_APPLICATION_PACKAGE_NAME_FILE_REGEX=r"\/store\/apps\/details\?id=([^&\"]+)"

GOOGLE_PLAY_URL_REGEX="https://play.google.com/"

IS_APP_STORE_APPLICATION_URL=False
IS_APP_STORE_DEVELOPER_URL=False
APP_STORE_URL_REGEX="https://apps.apple.com/"


def retrieve_application_package_name_from_google_play_application_url(google_play_application_url):

    # Retrieve application package name from "https://play.google.com/store/apps/details?id=com.some.application" as "com.some.application"
    application_package_nameMatch = re.search(GOOGLE_PLAY_ID_VALUE_REGEX, google_play_application_url)
    application_package_name = str(application_package_nameMatch.group(1))
    
    print("[Google Play][Application] Retrieved name: " + application_package_name)
    
    source_code.config_file_manager.append_to_android_application_package_name_list(application_package_name)


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
            source_code.config_file_manager.append_to_android_application_package_name_list(application_package_name)
            summary_retrieved_applications_package_name = summary_retrieved_applications_package_name + " " + application_package_name
        

        print("Retrieved: " + summary_retrieved_applications_package_name)
    else :
        print(google_play_developer_url + ": http response code: " + google_play_http_response_code)


def retrieve_application_package_name_from_appstore_application_url(appstore_application_url):
    
    print("TODO: retrieve_application_package_name_from_appstore_application_url")

def retrieve_application_package_name_from_appstore_developer_url(appstore_developer_url):
     print("TODO: retrieve_application_package_name_from_appstore_developer_url")


# Check if URL leads to Developer profile or directcly to application
def retrieve_application_package_name_from_url_to_file_list(url):

    if "https://play.google.com/store/apps/details" in url:
        retrieve_application_package_name_from_google_play_application_url(url)

    elif "https://play.google.com/store/apps/dev" in url:
        retrieve_application_package_names_from_google_play_developer_url(url)

    elif "https://apps.apple.com/pl/app/app-store-connect/id" in url: 
        retrieve_application_package_name_from_appstore_application_url(url)

    elif "https://apps.apple.com/pl/developer/apple/id" in url: 
        retrieve_application_package_name_from_appstore_developer_url(url)


def retrieve_all_application_package_names_from_store_file_list_to_application_file_list():

    store_urls_list_relative_path = source_code.config_file_manager.get_store_urls_list_relative_path

    with open(store_urls_list_relative_path) as store_urls_list_file:
        store_urls_list_file_contents = store_urls_list_file.read()
    
    for store_url in store_urls_list_file_contents:
        retrieve_application_package_name_from_url_to_file_list(store_url)
