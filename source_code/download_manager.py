import sys
import os
import source_code.config_file_manager

def download_android_application_package_name_from_google_play_to_input_directory(application_package_name):
    android_input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()

    if not os.path.exists(android_input_directory_relative_path):
        try:
            os.makedirs(android_input_directory_relative_path)
            os.chmod(android_input_directory_relative_path, 0o766)
        except OSError as e:
            print("An error occurred while creating the directory: " + android_input_directory_relative_path)

    print("Start downloading: " + application_package_name + " to " + android_input_directory_relative_path)
    os.system("apkeep -a " + application_package_name + " " + android_input_directory_relative_path)


# TODO: Implement iOS application downloader
def download_ios_application_package_name_from_appstore_to_input_directory(application_package_name):
    print("download_ios_application_package_name_from_appstore_to_input_directory: To be implemented.")

    # ios_input_directory_relative_path = source_code.config_file_manager.get_ios_input_directory_relative_path()
    # if not os.path.exists(ios_input_directory_relative_path):
    #     try:
    #         os.makedirs(ios_input_directory_relative_path)
    #     except OSError as e:
    #         print("An error occurred while creating the directory: " + ios_input_directory_relative_path)
    
    # print("Start downloading: " + application_package_name + " to " + ios_input_directory_relative_path)
    # os.system("apkeep -a " + application_package_name + " " + ios_input_directory_relative_path)


# TODO: Remove this function? Think if this function will be useful...
def download_android_applications(application_package_name):
    application_package_name_list_relative_path = source_code.config_file_manager.get_android_application_package_name_list_relative_path()

    try:
        with open(application_package_name_list_relative_path) as application_package_name_list_file:
            application_package_name_list_file_contents = application_package_name_list_file.readlines()
        
        # Google Play: https://play.google.com/store/apps/details?id=com.some.application -> com.some.application
        for application_package_name in application_package_name_list_file_contents:
            application_package_name = str.strip(application_package_name)
            download_android_application_package_name_from_google_play_to_input_directory(application_package_name)
     
    except FileNotFoundError:
        try:
            with open(application_package_name_list_relative_path, 'w') as application_package_name_list_file:
                print("It seems that file 'android_application_package_name_list.txt' did not exist. We created it for you. Please update it.")
        except IOError:
            print("An error occurred while creating the file: " + application_package_name_list_relative_path)
        
        sys.exit(1)

    except IOError:
        print("An error occurred while reading the file: " + application_package_name_list_relative_path)
        sys.exit(1)

def download_ios_applications():
    application_package_name_list_relative_path = source_code.config_file_manager.get_ios_application_package_name_list_relative_path()

    try:
        with open(application_package_name_list_relative_path) as application_package_name_list_file:
            application_package_name_list_file_contents = application_package_name_list_file.readlines()
        
        # App Store: https://apps.apple.com/pl/app/pyszne-pl/id1234567890?l=pl -> id1234567890
        for application_package_name in application_package_name_list_file_contents:
            application_package_name = str.strip(application_package_name)
            download_ios_application_package_name_from_appstore_to_input_directory(application_package_name)

    except FileNotFoundError:
        try:
            with open(application_package_name_list_relative_path, 'w') as application_package_name_list_file:
                print("It seems that file 'ios_application_package_name_list.txt' did not exist. We created it for you. Please update it.")
        except IOError:
            print("An error occurred while creating the file: " + application_package_name_list_relative_path)
        
        sys.exit(1)
    
    except IOError:
        print("An error occurred while reading the file: " + application_package_name_list_relative_path)
        sys.exit(1)


def find_application_package_name_with_extention(application_package_name_without_extention):
    
    android_input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
    
    for file in os.listdir(android_input_directory_relative_path):
        if application_package_name_without_extention in file:
            return str(os.path.basename(file))