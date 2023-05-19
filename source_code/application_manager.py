import source_code.decompiling_manager
import source_code.application_list_manager
import source_code.download_manager

def analyze_input_directory():
    print("Input dir")
    # source_code.decompiling_manager.decompile_application(application_package_system, application_package_name, decompiling_tool)


def analyze_application_package_name_list_file():
    print("Package File")
    source_code.download_manager.download_applications()

def analyze_store_list_file():
    print("Store")
    source_code.application_list_manager.retrieve_all_application_package_names_from_store_file_list_to_application_file_list()
    source_code.download_manager.download_applications()
