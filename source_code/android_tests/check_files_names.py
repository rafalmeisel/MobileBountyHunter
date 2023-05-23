import pathlib
import os
from source_code.report_manager import report_status_to_verify_with_token_value
from source_code.report_manager import report_status_not_found
from source_code.report_manager import copy_file_to_dedicated_report_directory
from source_code.config_file_manager import get_android_output_directory_relative_path
from source_code.config_file_manager import get_dedicated_mobile_bounty_hunter_report_directory_relative_path

# Any file with extension .sqlite or .db

def search_files_with_sqlite_extensions(application_package_name):
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    android_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, application_package_name)
    android_dedicated_report_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, application_package_name, dedicated_mobile_bounty_hunter_report_directory_relative_path)

    sqlite_files_list = [f for f in android_application_directory_relative_path.rglob("*.sqlite") if f.is_file()]

    if len(sqlite_files_list) > 0:

        for sqlite_file_path in sqlite_files_list:

            report_status_to_verify_with_token_value("Android", application_package_name, "", "Sqlite database", sqlite_file_path)
            copy_file_to_dedicated_report_directory(str(sqlite_file_path), str(android_dedicated_report_application_directory_relative_path))

    else:
        report_status_not_found("Android", application_package_name, "", "Sqlite database")
        

def search_files_with_db_extensions(application_package_name):
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    android_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, application_package_name)
    android_dedicated_report_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, application_package_name, dedicated_mobile_bounty_hunter_report_directory_relative_path)

    db_files_list = [f for f in android_application_directory_relative_path.rglob("*.db") if f.is_file()]

    if len(db_files_list) > 0:
        for db_file_path in db_files_list:

            report_status_to_verify_with_token_value("Android", application_package_name, "", "DB database", db_file_path)
            copy_file_to_dedicated_report_directory(str(db_file_path), str(android_dedicated_report_application_directory_relative_path))

    else:
        report_status_not_found("Android", application_package_name, "", "DB database")


def search_config_files_with_any_extensions(application_package_name):
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    android_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, application_package_name)
    

    config_files_list = [f for f in android_application_directory_relative_path.rglob("*config*") if f.is_file()]
    
    if len(config_files_list) > 0:

        for config_file_list in config_files_list:
            
            android_dedicated_report_application_directory_relative_path = pathlib.Path(android_output_directory_relative_path, application_package_name, dedicated_mobile_bounty_hunter_report_directory_relative_path, os.path.basename(config_file_list))
            report_status_to_verify_with_token_value("Android", application_package_name, "", "Config file", str(config_file_list))
            
            copy_file_to_dedicated_report_directory(str(config_file_list), str(android_dedicated_report_application_directory_relative_path))

    else:
        report_status_not_found("Android", application_package_name, "", "Config file")