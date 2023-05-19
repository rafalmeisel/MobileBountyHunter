from source_code.decompiling_manager import decompile_android_input_directory
from source_code.decompiling_manager import decompile_ios_input_directory
from source_code.application_list_manager import retrieve_all_application_package_names_from_store_file_list_to_application_file_list
from source_code.download_manager import download_android_applications
from source_code.download_manager import download_ios_applications
from source_code.application_list_manager import retrieve_all_application_package_names_from_store_file_list_to_application_file_list

def analyze_android_output_directory():
    print("Analyzing from Android Output")
    # Add: Analyzing Android Output


def analyze_android_input_directory():
    print("Analyzing from Android Input Directory")
    decompile_android_input_directory()
    # Add: Analyzing Android Output


def analyze_android_application_package_name_list_file():
    print("Analyzing from Android Package Name List")
    download_android_applications()
    decompile_android_input_directory()
    # Add: Analyzing Android Output


def analyze_store_list_file():
    print("Analyzing from Store List")
    retrieve_all_application_package_names_from_store_file_list_to_application_file_list()
    download_android_applications()
    decompile_android_input_directory()
    # Add: Analyzing Android Output
    

def analyze_ios_output_directory():
    print("iOS is not supprted yet :()")
    # print("Analyzing from iOS Output")
    # Add: Analyzing iOS Output


# def analyze_ios_input_directory():
    print("iOS is not supprted yet :()")
    # print("Analyzing from iOS Input Directory")
    # decompile_ios_input_directory()
    # Add: Analyzing iOS Output


def analyze_ios_application_package_name_list_file():
    print("iOS is not supprted yet :()")
    # print("Analyzing from iOS Package Name List")
    # download_ios_applications()
    # decompile_ios_input_directory()
    # Add: Analyzing iOS Output


def analyze_store_list_file():
    print("iOS is not supprted yet :()")
    # print("Analyzing from Store List")
    # retrieve_all_application_package_names_from_store_file_list_to_application_file_list()
    # download_ios_applications()
    # decompile_ios_input_directory()
    # Add: Analyzing iOS Output