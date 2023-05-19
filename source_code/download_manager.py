import os
import source_code.config_file_manager

def download_android_application_package_name_from_google_play_to_input_directory(application_package_name):
    android_input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path
    print("Start downloading: " + application_package_name + " to " + android_input_directory_relative_path)
    os.system("apkeep -a " + application_package_name + " " + android_input_directory_relative_path)


def download_ios_application_package_name_from_appstore_to_input_directory(application_package_name):
    print("download_ios_application_package_name_from_appstore_to_input_directory: To be implemented.")


def download_application_package_name_from_package_name_to_input_directory(application_package_name):
    if application_package_name.startswith('id'):
        download_ios_application_package_name_from_appstore_to_input_directory(application_package_name)
    else:
        download_android_application_package_name_from_google_play_to_input_directory(application_package_name)


def download_applications():
    application_package_name_list_relative_path = source_code.config_file_manager.get_application_package_name_list_relative_path

    with open(application_package_name_list_relative_path) as application_package_name_list_file:
        application_package_name_list_file_contents = application_package_name_list_file.read()
    
    # Google Play: https://play.google.com/store/apps/details?id=com.some.application -> com.some.application
    # App Store: https://apps.apple.com/pl/app/pyszne-pl/id1234567890?l=pl -> id1234567890
    for application_package_name in application_package_name_list_file_contents:
        download_application_package_name_from_package_name_to_input_directory(application_package_name)
