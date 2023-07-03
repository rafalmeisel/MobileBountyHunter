import json
import shutil
import os

def get_mobile_bounty_hunter_config_path():
    mobile_bounty_hunter_directory = os.getcwd()
    config_path = mobile_bounty_hunter_directory + "/workspace/config/config.json"
    return config_path


def get_mobile_bounty_hunter_config_runtime_path():
    mobile_bounty_hunter_directory = os.getcwd()
    config_runtime_path = mobile_bounty_hunter_directory + "/workspace/config/config_runtime.json"
    return config_runtime_path


def create_config_runtime_file():
    config_path = get_mobile_bounty_hunter_config_path()
    config_runtime_path = get_mobile_bounty_hunter_config_runtime_path()
    shutil.copyfile(config_path, config_runtime_path)


def delete_config_runtime_file():
    config_runtime_path = get_mobile_bounty_hunter_config_runtime_path()
    os.remove(config_runtime_path)


def read_config_runtime_file():
    config_runtime_path = get_mobile_bounty_hunter_config_runtime_path()
    with open(config_runtime_path) as config_runtime_file:
        config_runtime_file_contents = json.load(config_runtime_file)
    return config_runtime_file_contents


def write_config_runtime_file(key, value):
    config_runtime_path = get_mobile_bounty_hunter_config_runtime_path()

    with open(config_runtime_path, 'r') as config_runtime_file:
        config_runtime_file_contents = json.load(config_runtime_file)
        config_runtime_file_contents[key] = value
    
    with open(config_runtime_path, 'w') as config_runtime_file:
        json.dump(config_runtime_file_contents, config_runtime_file, indent=4)
    
    return config_runtime_file_contents


def set_true_autoinstall_third_party_software():
    write_config_runtime_file("autoinstallThirdPartySoftware", "True")


def set_false_autoinstall_third_party_software():
    write_config_runtime_file("autoinstallThirdPartySoftware", "False")


def get_autoinstall_third_party_software():
    config_file_json = read_config_runtime_file()
    autoinstall_third_party_software_value = config_file_json["autoinstallThirdPartySoftware"]

    if (autoinstall_third_party_software_value == "True"):
        return True
    else:
        return False
    

def set_android_decompiling_tool(decompiling_tool):
    write_config_runtime_file("androidDecompilingTool", decompiling_tool)


def set_ios_decompiling_tool(decompiling_tool):
    write_config_runtime_file("iosDecompilingTool", decompiling_tool)


def get_workspace_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["workspaceRelativePath"]


def get_global_mobile_bounty_hunter_report_file_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["globalMobileBountyHunterReportFileRelativePath"]


def get_dedicated_mobile_bounty_hunter_report_file_name():
    config_file_json = read_config_runtime_file()
    return config_file_json["dedicatedMobileBountyHunterReportFileName"]


def get_dedicated_mobile_bounty_hunter_report_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["dedicatedMobileBountyHunterReportDirectoryRelativePath"]


def get_android_store_urls_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidStoreUrlsListRelativePath"]


def get_android_application_package_name_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidApplicationPackageNameListRelativePath"]


def get_ios_application_package_name_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosApplicationPackageNameListRelativePath"]


def get_android_decompiling_tool():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidDecompilingTool"]


def get_android_input_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidInputDirectoryRelativePath"]


def get_android_input_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidInputAnalyzedDirectoryRelativePath"]


def get_android_output_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidOutputDirectoryRelativePath"]


def get_android_output_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["androidOutputAnalyzedDirectoryRelativePath"]


def get_ios_store_urls_list_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosStoreUrlsListRelativePath"]


def get_ios_input_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosInputDirectoryRelativePath"]


def get_ios_input_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosInputAnalyzedDirectoryRelativePath"]


def get_ios_output_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosOutputDirectoryRelativePath"]


def get_ios_output_analyzed_directory_relative_path():
    config_file_json = read_config_runtime_file()
    return config_file_json["iosOutputAnalyzedDirectoryRelativePath"]