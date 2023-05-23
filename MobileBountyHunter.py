import sys
import argparse
from source_code.third_party_software_manager import install_third_party_software
import source_code.application_manager
from source_code.config_file_manager import create_config_runtime_file
from source_code.config_file_manager import delete_config_runtime_file
from source_code.config_file_manager import set_android_decompiling_tool
from source_code.config_file_manager import set_ios_decompiling_tool

def main(argv):
    
    install_third_party_software()

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-ai", "--analyze_android_input_directory", required=False, action='store_true')
    parser.add_argument("-ao", "--analyze_android_output_directory", required=False, action='store_true')
    parser.add_argument("-al", "--analyze_android_application_package_name_file", required=False, action='store_true')
    parser.add_argument("-as", "--analyze_android_store_list_file", required=False, action='store_true')
    parser.add_argument("-ad", "--android_decompiling_tool", required=False, action='store_true')
    
    parser.add_argument("-ii", "--analyze_ios_input_directory", required=False, action='store_true')
    parser.add_argument("-io", "--analyze_ios_output_directory", required=False, action='store_true')
    parser.add_argument("-il", "--analyze_ios_application_package_name_file", required=False, action='store_true')
    parser.add_argument("-is", "--analyze_ios_store_list_file", required=False, action='store_true')
    parser.add_argument("-id", "--ios_decompiling_tool", required=False, action='store_true')
    
    args = parser.parse_args()

    create_config_runtime_file()

    if args.android_decompiling_tool:
        print("You set Android decompiling tool: ")   
        set_android_decompiling_tool(args.android_decompiling_tool)
    elif args.ios_decompiling_tool:
        print("You set iOS decompiling tool: ")   
        set_ios_decompiling_tool(args.android_decompiling_tool)

    if args.analyze_android_input_directory:
        print('You choose: analyze_android_input_directory')
        source_code.application_manager.analyze_android_input_directory()

    elif args.analyze_android_output_directory:
        print('You choose: analyze_android_output_directory')
        source_code.application_manager.analyze_android_output_directory()

    elif args.analyze_android_application_package_name_file:
        print('You choose: analyze_android_application_package_name_file')
        source_code.application_manager.analyze_android_application_package_name_list_file()

    elif args.analyze_android_store_list_file:
        print('You choose: analyze_android_store_list_file')
        source_code.application_manager.analyze_android_store_list_file()

    elif args.analyze_ios_input_directory:
        print('You choose: analyze_ios_input_directory')
        source_code.application_manager.analyze_ios_input_directory()

    elif args.analyze_ios_output_directory:
        print('You choose: analyze_ios_output_directory')
        source_code.application_manager.analyze_ios_output_directory()

    elif args.analyze_ios_application_package_name_file:
        print('You choose: analyze_ios_application_package_name_file')
        source_code.application_manager.analyze_ios_application_package_name_list_file()

    elif args.analyze_ios_store_url_file:
        print('You choose: analyze_ios_store_url_file')
        source_code.application_manager.analyze_ios_store_list_file()

    delete_config_runtime_file()
    
if __name__ == '__main__':
    main(sys.argv[1:])