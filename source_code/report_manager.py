from termcolor import colored
import shutil
import os
import hashlib
import pathlib
from random import seed
from random import randint
from enum import Enum
from source_code.config_file_manager import *
from source_code.system_manager import *

class UrlResourceSecurityStatus(Enum):
    SECURED = 1
    VULNERABLE = 2
    TO_VERIFY = 3
    FOUND = 4
    NOT_FOUND = 5


def print_on_console_without_token_value(application_package_name, analyzed_file_name, issue_status, token_name):
    print_on_console_with_token_value(application_package_name, analyzed_file_name, issue_status, token_name, "")


def print_on_console_with_token_value(application_package_name, analyzed_file_name, issue_status, token_name, token_value):

    report_color = ""
    issue_status_comment = ""

    if (UrlResourceSecurityStatus.SECURED == issue_status):
        issue_status_comment = "is secured."
        report_color = "blue"
    elif (UrlResourceSecurityStatus.VULNERABLE == issue_status):
        issue_status_comment = "IS VUNLERABLE!"
        report_color = "red"
    elif (UrlResourceSecurityStatus.TO_VERIFY == issue_status):
        issue_status_comment = "to verify..."
        report_color = "yellow"
    elif (UrlResourceSecurityStatus.NOT_FOUND == issue_status):
        issue_status_comment = "not found."
        report_color = "blue"
    elif (UrlResourceSecurityStatus.FOUND == issue_status):
        issue_status_comment = "FOUND!"
        report_color = "red"
    else:
        issue_status_comment = issue_status
        report_color = "grey"

    if len(token_value) == 0:
        print(application_package_name + ": " + analyzed_file_name + ": " + colored(token_name + ": " + issue_status_comment, report_color))
    
    else:
        print(application_package_name + ": " + analyzed_file_name + ": " + colored(token_name + ": " + token_value + ": " + issue_status_comment, report_color))


def write_to_report_file(report_file_relative_path, application_package_name, analyzed_file_name, issue_status, token_name, token_value):
    
    issue_status_comment = ""

    if (UrlResourceSecurityStatus.SECURED == issue_status):
        issue_status_comment = "is secured."
    elif (UrlResourceSecurityStatus.VULNERABLE == issue_status):
        issue_status_comment = "IS VUNLERABLE!"
    elif (UrlResourceSecurityStatus.TO_VERIFY == issue_status):
        issue_status_comment = "to verify..."
    elif (UrlResourceSecurityStatus.NOT_FOUND == issue_status):
        issue_status_comment = "not found."
    elif (UrlResourceSecurityStatus.FOUND == issue_status):
        issue_status_comment = "FOUND!"
    else:
        issue_status_comment = issue_status


    if not(os.path.exists(report_file_relative_path)):
        os.makedirs(os.path.dirname(report_file_relative_path), exist_ok=True)
    
    report_file = open(report_file_relative_path, "a")

    if len(token_value) == 0:
        report_file.write(application_package_name + ": " + analyzed_file_name + ": " + token_name + ": " + issue_status_comment + "\n")
    
    else:
        report_file.write(application_package_name + ": " + analyzed_file_name + ": " + token_name + ": " + token_value + ": " + issue_status_comment + "\n")

    report_file.close()

def get_android_output_directory_application_package_system_relative_path():

    output_directory_relative_path = get_android_output_directory_relative_path()
    return output_directory_relative_path


def get_ios_output_directory_application_package_system_relative_path():

    output_directory_relative_path = get_ios_output_directory_relative_path()
    return output_directory_relative_path


def write_to_dedicated_report_file_with_token_value(application_package_system, application_package_name, analyzed_file_name, issue_status, token_name, token_value):

    output_directory_relative_path = ""
    
    if "Android" == application_package_system:
        output_directory_relative_path = get_android_output_directory_application_package_system_relative_path()
    elif "iOS" == application_package_system:
        output_directory_relative_path = get_ios_output_directory_application_package_system_relative_path()

    if (output_directory_relative_path == ""):
        print("report_manager: write_to_dedicated_report_file_with_token_value: output_directory_relative_path is empty!")
    else:
        dedicated_report_file_relative_path = pathlib.Path(output_directory_relative_path, application_package_name, get_dedicated_mobile_bounty_hunter_report_directory_relative_path(), get_dedicated_mobile_bounty_hunter_report_file_name())
        write_to_report_file(dedicated_report_file_relative_path, analyzed_file_name, issue_status, token_name, token_value)


def write_to_dedicated_report_file_without_token_value(application_package_system, application_package_name, analyzed_file_name, issue_status, token_name):
    
    output_directory_relative_path = ""
    
    if "Android" == application_package_system:
        output_directory_relative_path = get_android_output_directory_application_package_system_relative_path()
    elif "iOS" == application_package_system:
        output_directory_relative_path = get_ios_output_directory_application_package_system_relative_path()

    if (output_directory_relative_path == ""):
        print("report_manager: write_to_dedicated_report_file_without_token_value: output_directory_relative_path is empty!")
    else:
        dedicated_report_file_relative_path = pathlib.Path(output_directory_relative_path, application_package_name, get_dedicated_mobile_bounty_hunter_report_directory_relative_path(), get_dedicated_mobile_bounty_hunter_report_file_name())
        write_to_report_file(dedicated_report_file_relative_path, analyzed_file_name, issue_status, token_name, "")


def write_to_global_report_file_with_token_value(application_package_name, analyzed_file_name, issue_status, token_name, token_value):
    global_report_file_relative_path = get_global_mobile_bounty_hunter_report_file_relative_path()
    write_to_report_file(global_report_file_relative_path, application_package_name, analyzed_file_name, issue_status, token_name, token_value)


def write_to_global_report_file_without_token_value(application_package_name, analyzed_file_name, issue_status, token_name):
    global_report_file_relative_path = get_global_mobile_bounty_hunter_report_file_relative_path()
    write_to_report_file(global_report_file_relative_path, application_package_name, analyzed_file_name, issue_status, token_name, "")


def report_status_vulnerable_with_token_value(application_package_system, application_package_name, analyzed_file_name, token_name, token_value):
    print_on_console_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.VULNERABLE, token_name, token_value)
    write_to_dedicated_report_file_with_token_value(application_package_system, application_package_name, analyzed_file_name, UrlResourceSecurityStatus.VULNERABLE, token_name, token_value)
    write_to_global_report_file_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.VULNERABLE, token_name, token_value)


def report_status_to_verify_with_token_value(application_package_system, application_package_name, analyzed_file_name, token_name, token_value):
    print_on_console_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.TO_VERIFY, token_name, token_value)
    write_to_dedicated_report_file_with_token_value(application_package_system, application_package_name, analyzed_file_name, UrlResourceSecurityStatus.TO_VERIFY, token_name, token_value)
    write_to_global_report_file_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.TO_VERIFY, token_name, token_value)


def report_status_to_verify_without_token_value(application_package_system, application_package_name, analyzed_file_name, token_name):
    print_on_console_without_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.TO_VERIFY, token_name)
    write_to_dedicated_report_file_without_token_value(application_package_system, application_package_name, analyzed_file_name, UrlResourceSecurityStatus.TO_VERIFY, token_name)
    write_to_global_report_file_without_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.TO_VERIFY, token_name)


def report_status_secured_with_token_value(application_package_system, application_package_name, analyzed_file_name, token_name, token_value):
    print_on_console_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.SECURED, token_name, token_value)
    write_to_dedicated_report_file_with_token_value(application_package_system, application_package_name, analyzed_file_name, UrlResourceSecurityStatus.SECURED, token_name, token_value)
    write_to_global_report_file_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.SECURED, token_name, token_value)


def report_status_found_with_token_value(application_package_system, application_package_name, analyzed_file_name, token_name, token_value):
    print_on_console_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.FOUND, token_name, token_value)
    write_to_dedicated_report_file_with_token_value(application_package_system, application_package_name, analyzed_file_name, UrlResourceSecurityStatus.FOUND, token_name, token_value)
    write_to_global_report_file_with_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.FOUND, token_name, token_value)


def report_status_not_found(application_package_system, application_package_name, analyzed_file_name, token_name):
    print_on_console_without_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.NOT_FOUND, token_name)
    write_to_dedicated_report_file_without_token_value(application_package_system, application_package_name, analyzed_file_name, UrlResourceSecurityStatus.NOT_FOUND, token_name)
    write_to_global_report_file_without_token_value(application_package_name, analyzed_file_name, UrlResourceSecurityStatus.NOT_FOUND, token_name)


def copy_file_to_dedicated_report_directory(source_file_path, destination_file_path):
   
    file_name_to_copy_exists = os.path.isfile(destination_file_path)

    if (file_name_to_copy_exists):
        # Calculate MD5 of already existing file with new one
        # If MD5 are the same, skip copying
        # If MD5 are different, copy file with adding suffix _1, _2, etc.

        md5ExistedFile = ""
        md5NewFile = ""
        
        with open(destination_file_path, 'rb') as file_to_check:
            data = file_to_check.read()    
            md5ExistedFile = hashlib.md5(data).hexdigest()

        with open(source_file_path, 'rb') as file_to_check:
            data = file_to_check.read()    
            md5NewFile = hashlib.md5(data).hexdigest()

        if (md5ExistedFile == md5NewFile):
            print("Found file \"" + source_file_path + "\"" + "was already copied (comapred MD5s). Skipping...")
        
        else:
            seed(1)
            randomValue = str(randint(0, 100000000))

            shutil.copyfile(source_file_path, destination_file_path + "_" + randomValue)
    else:
        shutil.copyfile(source_file_path, destination_file_path)