from termcolor import colored
import shutil
import os
import hashlib
import pathlib
from random import seed
from random import randint
from enum import Enum
from source_code.config_file_manager import *

class IssueSeverity(Enum):
    CRITICAL = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    INFORMATIVE = 4

class IssueStatus(Enum):
    VULNERABLE = 0
    SECURED = 1
    TO_VERIFY = 2
    FOUND = 3
    NOT_FOUND = 4


def report_issue(application_package_system, application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value):
    
    print_on_console(application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value)
    write_to_dedicated_report_file(application_package_system, application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value)
    write_to_global_report_file(application_package_system, application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value)


def print_on_console(application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value):
    
    issue_severity_report_color = ""
    issue_status_report_color = ""

    match issue_severity:
        case IssueSeverity.HIGH:
            issue_severity_report_color = "red"
        case IssueSeverity.MEDIUM:
            issue_severity_report_color = "yellow"
        case IssueSeverity.LOW:
            issue_severity_report_color = "blue"
        case IssueSeverity.INFORMATIVE:
            issue_severity_report_color = "grey"
        case _:
            issue_severity_report_color = "grey"
    
    match issue_status:
        case IssueStatus.VULNERABLE:
            issue_status_report_color = "red"
        case IssueStatus.SECURED:
            issue_status_report_color = "blue"
        case IssueStatus.TO_VERIFY:
            issue_status_report_color = "yellow"
        case IssueStatus.FOUND:
            issue_status_report_color = "red"
        case IssueStatus.NOT_FOUND:
            issue_status_report_color = "grey"
        case _:
            issue_status_report_color = "grey"

    if len(analyzed_file_name) == 0 and len(token_value) == 0:
        print(application_package_name + ": " + colored(str(issue_severity.name), issue_severity_report_color) + ": " + colored(str(issue_status.name) + ": " + token_name, issue_status_report_color))

    elif len(token_value) == 0:
        print(application_package_name + ": " + analyzed_file_name + ": " + colored(str(issue_severity.name), issue_severity_report_color) + ": " + colored(str(issue_status.name) + ": " + token_name, issue_status_report_color))
    
    else:
        print(application_package_name + ": " + analyzed_file_name + ": " + colored(str(issue_severity.name), issue_severity_report_color) + ": " + colored(str(issue_status.name) + ": " + token_name + ": " + token_value, issue_status_report_color))


def write_to_dedicated_report_file(application_package_system, application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value):
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_directory_relative_path = get_dedicated_mobile_bounty_hunter_report_directory_relative_path()
    dedicated_mobile_bounty_hunter_report_file_name = get_dedicated_mobile_bounty_hunter_report_file_name()

    dedicated_mobile_bounty_huinter_report_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, dedicated_mobile_bounty_hunter_report_directory_relative_path, dedicated_mobile_bounty_hunter_report_file_name)
    if not(os.path.exists(dedicated_mobile_bounty_huinter_report_file_path)):
        os.makedirs(os.path.dirname(dedicated_mobile_bounty_huinter_report_file_path), exist_ok=True)
    
    report_global_file = open(dedicated_mobile_bounty_huinter_report_file_path, "a")

    if len(analyzed_file_name) == 0 and len(token_value) == 0:
        report_global_file.write(application_package_system + ": " + application_package_name + ": " + str(issue_severity.name) + ": " + str(issue_status.name) + ": " + token_name)

    elif len(token_value) == 0:
        report_global_file.write(application_package_system + ": " + analyzed_file_name + ": " + str(issue_severity.name) + ": " + str(issue_status.name) + ": " + token_name)
    
    else:
        report_global_file.write(application_package_system + ": " + analyzed_file_name + ": " + str(issue_severity.name) + ": " + str(issue_status.name) + ": " + token_name + ": " + token_value)

    report_global_file.close()


def write_to_global_report_file(application_package_system, application_package_name, analyzed_file_name, issue_severity, issue_status, token_name, token_value):
    
    global_mobile_bounty_hunter_report_file_relative_path = get_global_mobile_bounty_hunter_report_file_relative_path()

    if not(os.path.exists(global_mobile_bounty_hunter_report_file_relative_path)):
        os.makedirs(os.path.dirname(global_mobile_bounty_hunter_report_file_relative_path), exist_ok=True)
    
    report_global_file = open(global_mobile_bounty_hunter_report_file_relative_path, "a")

    if len(analyzed_file_name) == 0 and len(token_value) == 0:
        report_global_file.write(application_package_system + ": " + application_package_name + ": " + str(issue_severity.name) + ": " + str(issue_status.name) + ": " + token_name)

    elif len(token_value) == 0:
        report_global_file.write(application_package_system + ": " + analyzed_file_name + ": " + str(issue_severity.name) + ": " + str(issue_status.name) + ": " + token_name)
    
    else:
        report_global_file.write(application_package_system + ": " + analyzed_file_name + ": " + str(issue_severity.name) + ": " + str(issue_status.name) + ": " + token_name + ": " + token_value)

    report_global_file.close()

    
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

        if not(md5ExistedFile == md5NewFile):
            seed(1)
            randomValue = str(randint(0, 100000000))

            shutil.copyfile(source_file_path, destination_file_path + "_" + randomValue)

    else:
        shutil.copyfile(source_file_path, destination_file_path)