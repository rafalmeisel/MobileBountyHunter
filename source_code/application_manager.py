from source_code.application_list_manager import retrieve_android_application_package_name_from_store_url_to_applicatione_list_file
from source_code.application_list_manager import retrieve_ios_application_package_name_from_store_url_to_applicatione_list_file
from source_code.download_manager import download_android_application_package_name_from_google_play_to_input_directory
from source_code.download_manager import download_ios_applications
from source_code.decompiling_manager import decompile_android_application
from source_code.decompiling_manager import decompile_ios_input_directory
from source_code.android_application_tester import run_android_tests_in_android_output_directory
import source_code.config_file_manager
from source_code.android_application_tester import run_tests_android_application
from source_code.download_manager import find_application_package_name_with_extention
import os
import shutil
import pathlib

def analyze_android_output_directory():
    print("Analyzing from Android Output")
    
    output_directory_relative_path = source_code.config_file_manager.get_android_output_directory_relative_path()
    
    for application_package_name in os.listdir(output_directory_relative_path):
        run_tests_android_application(application_package_name)
        move_android_application_to_output_analyzed_directory(application_package_name)


def analyze_android_input_directory():
    print("Analyzing from Android Input Directory")
    
    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
    decompiling_tool = source_code.config_file_manager.get_android_decompiling_tool()

    for application_package_name in os.listdir(input_directory_relative_path):
        decompile_android_application(application_package_name, decompiling_tool)
        
        # When downloaded and decompiled application is .xapk, script should test .apk 
        application_package_name = application_package_name.replace(".xapk", ".apk")
        
        run_tests_android_application(application_package_name)
        move_android_application_to_input_analyzed_directory(application_package_name)
        move_android_application_to_output_analyzed_directory(application_package_name)


def analyze_android_application_package_name_list_file():
    print("Analyzing from Android Package Name List")
    
    android_application_package_name_list_relative_path = source_code.config_file_manager.get_android_application_package_name_list_relative_path()
    decompiling_tool = source_code.config_file_manager.get_android_decompiling_tool()

    android_application_package_name_list_file_path = pathlib.Path(android_application_package_name_list_relative_path)
    android_application_package_name_list_file_content = open(android_application_package_name_list_file_path, "r").readlines()

    for application_package_name_without_extention in android_application_package_name_list_file_content:

        # Removing newline character from endline
        application_package_name_without_extention = application_package_name_without_extention.strip()
        download_android_application_package_name_from_google_play_to_input_directory(application_package_name_without_extention)
        application_package_name_with_extention = find_application_package_name_with_extention(application_package_name_without_extention)
        decompile_android_application(application_package_name_with_extention, decompiling_tool)
        
        # When downloaded and decompiled application is .xapk, script should test .apk 
        application_package_name_with_extention = application_package_name_with_extention.replace(".xapk", ".apk")
        
        run_tests_android_application(application_package_name_with_extention)
        move_android_application_to_input_analyzed_directory(application_package_name_with_extention)
        move_android_application_to_output_analyzed_directory(application_package_name_with_extention)


def analyze_android_store_list_file():
    print("Analyzing from Android Store List")
    retrieve_android_application_package_name_from_store_url_to_applicatione_list_file()
    
    android_application_package_name_list_relative_path = source_code.config_file_manager.get_android_application_package_name_list_relative_path()
    decompiling_tool = source_code.config_file_manager.get_android_decompiling_tool()

    android_application_package_name_list_file_path = pathlib.Path(android_application_package_name_list_relative_path)
    android_application_package_name_list_file_content = open(android_application_package_name_list_file_path, "r").readlines()

    for application_package_name_without_extention in android_application_package_name_list_file_content:
        
        # Removing newline character from endline
        application_package_name_without_extention = application_package_name_without_extention.strip()
        download_android_application_package_name_from_google_play_to_input_directory(application_package_name_without_extention)
        application_package_name_with_extention = find_application_package_name_with_extention(application_package_name_without_extention)
        decompile_android_application(application_package_name_with_extention, decompiling_tool)

        # When downloaded and decompiled application is .xapk, script should test .apk 
        application_package_name_with_extention = application_package_name_with_extention.replace(".xapk", ".apk")

        run_tests_android_application(application_package_name_with_extention)
        move_android_application_to_input_analyzed_directory(application_package_name_with_extention)
        move_android_application_to_output_analyzed_directory(application_package_name_with_extention)
    

def analyze_ios_output_directory():
    print("iOS is not supprted yet :()")
    # print("Analyzing from iOS Output")
    # Add: Analyzing iOS Output


def analyze_ios_input_directory():
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


def analyze_ios_store_list_file():
    print("iOS is not supprted yet :()")
    # print("Analyzing from Store List")
    # retrieve_all_application_package_names_from_store_file_list_to_application_file_list()
    # download_ios_applications()
    # decompile_ios_input_directory()
    # Add: Analyzing iOS Output


def move_android_application_to_input_analyzed_directory(application_package_name_with_extention):
    
    android_input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
    android_application_in_input_directory_path = str(pathlib.Path(android_input_directory_relative_path, application_package_name_with_extention))

    android_input_analyzed_directory_relative_path = source_code.config_file_manager.get_android_input_analyzed_directory_relative_path()
    android_application_in_input_analyzed_directory_path = str(pathlib.Path(android_input_analyzed_directory_relative_path, application_package_name_with_extention))
    
    # If directory Input Analyzed does not exists - create it
    if not os.path.exists(android_input_analyzed_directory_relative_path):
        os.makedirs(android_input_analyzed_directory_relative_path)

    # If application is already exists in Input Analyzed directory - replace it
    if os.path.exists(android_application_in_input_analyzed_directory_path):
        os.replace(android_application_in_input_directory_path, android_application_in_input_analyzed_directory_path)

    # If application does not exists in Input Analyzed directory - move it
    if os.path.exists(android_application_in_input_analyzed_directory_path):
        shutil.move(android_application_in_input_directory_path, android_application_in_input_analyzed_directory_path)

def move_android_application_to_output_analyzed_directory(application_package_name_with_extention):
    
    android_output_directory_relative_path = source_code.config_file_manager.get_android_output_directory_relative_path()
    android_application_in_output_directory_path = str(pathlib.Path(android_output_directory_relative_path, application_package_name_with_extention))

    android_output_analyzed_directory_relative_path = source_code.config_file_manager.get_android_output_analyzed_directory_relative_path()
    android_application_in_output_analyzed_directory_relative_path = str(pathlib.Path(android_output_analyzed_directory_relative_path, application_package_name_with_extention))

    if not os.path.exists(android_output_analyzed_directory_relative_path):
        os.makedirs(android_output_analyzed_directory_relative_path)
    
    if os.path.exists(android_application_in_output_analyzed_directory_relative_path):
        shutil.rmtree(android_application_in_output_analyzed_directory_relative_path)

    shutil.move(android_application_in_output_directory_path, android_output_analyzed_directory_relative_path)