import sys
import argparse
from source_code.third_party_software_manager import install_third_party_software
import source_code.application_manager

def main(argv):
    
    install_third_party_software()

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-ia", "--analyze_android_input_directory", required=False, action='store_true')
    parser.add_argument("-ii", "--analyze_ios_input_directory", required=False, action='store_true')
    parser.add_argument("-oa", "--analyze_android_output_directory", required=False, action='store_true')
    parser.add_argument("-oi", "--analyze_ios_output_directory", required=False, action='store_true')
    parser.add_argument("-la", "--analyze_android_application_package_name_file", required=False, action='store_true')
    parser.add_argument("-li", "--analyze_ios_application_package_name_file", required=False, action='store_true')
    parser.add_argument("-s", "--analyze_store_url_file", required=False, action='store_true')
    
    args = parser.parse_args()
    
    if args.analyze_android_input_directory:
        print('You choose: analyze_android_input_directory')
        source_code.application_manager.analyze_android_input_directory()

    elif args.analyze_android_output_directory:
        print('You choose: analyze_android_output_directory')
        source_code.application_manager.analyze_android_output_directory()

    elif args.analyze_android_application_package_name_file:
        print('You choose: analyze_android_application_package_name_file')
        source_code.application_manager.analyze_android_application_package_name_list_file()

    elif args.analyze_ios_input_directory:
        print('You choose: analyze_ios_input_directory')
        source_code.application_manager.analyze_ios_input_directory()

    elif args.analyze_ios_output_directory:
        print('You choose: analyze_ios_output_directory')
        source_code.application_manager.analyze_ios_output_directory()

    elif args.analyze_ios_application_package_name_file:
        print('You choose: analyze_ios_application_package_name_file')
        source_code.application_manager.analyze_ios_application_package_name_list_file()

    elif args.analyze_store_url_file:
        print('You choose: analyze_store_url_file')

if __name__ == '__main__':
    main(sys.argv[1:])