from termcolor import colored
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus
import re
import requests
import boto3
from source_code.report_manager import *
from source_code.config_file_manager import get_android_output_directory_relative_path

application_package_system = "Android"

# Interesting things in AndroidManifest:
# - Api keys
# - Custom schemas
# - Hardcoded values. Developers are encouraged to store strings as reference

def check_res_values_strings_aws_long_term_access_keys(application_package_name, android_res_values_strings_relative_file_path):
    
    aws_akid_regex=r'(?<=>)AK(\S*?)(?=<)'
    aws_akid_value=""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(aws_akid_regex, line):
            aws_akid_match =  re.search(aws_akid_regex, line)
            aws_akid_value = aws_akid_match.group()

            report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.MEDIUM, IssueStatus.FOUND, "AWS Long Term Access Key", aws_akid_value)
            # report_status_found_with_token_value("Android", application_package_name, "ResValuesStrings", "AWS Long Term Access Key", aws_akid_value)

    if len(aws_akid_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Long Term Access Key", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "AWS Long Term Access Key")


def check_res_values_strings_aws_short_term_access_keys(application_package_name, android_res_values_strings_relative_file_path):
    
    aws_akid_regex=r'(?<=>)AS(\S*?)(?=<)'
    aws_akid_value=""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
   
    for line in android_res_values_strings_file_content:
        if re.search(aws_akid_regex, line):
            aws_akid_match =  re.search(aws_akid_regex, line)
            aws_akid_value = aws_akid_match.group()
            
            report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.MEDIUM, IssueStatus.FOUND, "AWS Short Term Access Key", aws_akid_value)
            # report_status_found_with_token_value("Android", application_package_name, "ResValuesStrings", "AWS Short Term Access Key", aws_akid_value)

    if len(aws_akid_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Short Term Access Key", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "AWS Short Term Access Key")


def check_res_values_strings_aws_secret_access_key(application_package_name, android_res_values_strings_relative_file_path):
    
    aws_secret_key_regex=r'(?:(AWS|aws).*>)(\S*)(?=<)'
    aws_secret_key_value=""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()

    for line in android_res_values_strings_file_content:
        if re.search(aws_secret_key_regex, line):
            aws_secret_key_match =  re.search(aws_secret_key_regex, line)
            aws_secret_key_value = aws_secret_key_match.group(2)
            
            report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.MEDIUM, IssueStatus.FOUND, "AWS Secret Key", aws_secret_key_value)
            # report_status_found_with_token_value("Android", application_package_name, "ResValuesStrings", "AWS Secret Key", aws_secret_key_value)

    if len(aws_secret_key_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Secret Key", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "AWS Secret Key")


def check_aws_s3_bucket_permission(aws_bucket_name):
    # create an S3 client
    s3 = boto3.client('s3')

    # specify the name of the S3 bucket to check
    bucket_name = aws_bucket_name

    # get the bucket policy
    bucket_policy = s3.get_bucket_policy(Bucket=bucket_name)

    # check if the bucket policy allows public access
    if 'Statement' in bucket_policy:
        for statement in bucket_policy['Statement']:
            if 'Effect' in statement and statement['Effect'] == 'Allow':
                if 'Principal' in statement and statement['Principal'] == '*':
                    if 'Action' in statement and 's3:GetObject' in statement['Action']:
                        if 'Resource' in statement and statement['Resource'] == 'arn:aws:s3:::{}/*'.format(bucket_name):
                            # print("Bucket is publicly accessible")
                            # aws_url = f"https://{bucket_name}.s3.amazonaws.com/"
                            # print("AWS URL: ", aws_url)
                            return True
                            break

    # if the bucket policy doesn't allow public access
    # else:
    #     print("Bucket is not publicly accessible")
    return False

def check_res_values_strings_aws_bucket(application_package_name, android_res_values_strings_relative_file_path):
    
    aws_bucket_name_regex=r"(https:?\/\/)(.*)(.s3.amazonaws.com)"
    aws_bucket_name_value=""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(aws_bucket_name_regex, line):
            aws_bucket_name_match =  re.search(aws_bucket_name_regex, line)
            aws_bucket_name_value = aws_bucket_name_match.group(2)

            aws_s3_bucket_is_open = check_aws_s3_bucket_permission(application_package_name, aws_bucket_name_value)

            if (aws_s3_bucket_is_open):
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.HIGH, IssueStatus.VULNERABLE, "AWS Bucket", aws_bucket_name_value)
                # report_status_vulnerable_with_token_value("Android", application_package_name, "ResValuesStrings", "AWS Bucket", aws_bucket_name_value)
            else:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.SECURED, "AWS Bucket", aws_bucket_name_value)
                # report_status_secured_with_token_value("Android", application_package_name, "ResValuesStrings", "AWS Bucket")
            

    if len(aws_bucket_name_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Bucket", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "AWS Bucket")


# https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop-mobile/ios/in-app-msg.htm
def check_res_values_strings_push_io_application_identifier(application_package_name, android_res_values_strings_relative_file_path):
    
    push_io_application_identifier_regex=r'pio-([^<]+)'
    push_io_application_identifier_value=""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
   
    for line in android_res_values_strings_file_content:
        if re.search(push_io_application_identifier_regex, line):
            pushIoApplicationIdentifier_match =  re.search(push_io_application_identifier_regex, line)
            push_io_application_identifier_value = pushIoApplicationIdentifier_match.group()

            report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.MEDIUM, IssueStatus.FOUND, "PushIoApplicationIdentifier", push_io_application_identifier_value)
            # report_status_found_with_token_value("Android", application_package_name, "ResValuesStrings", "PushIoApplicationIdentifier", push_io_application_identifier_value)

    if len(push_io_application_identifier_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "PushIoApplicationIdentifier", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "PushIoApplicationIdentifier")

def send_request_to_firebase(firebase_url):
    response = requests.get(firebase_url + "/.json")
    data = str(response.json())
    
    return data

def check_res_values_strings_firebase_url(application_package_name, android_res_values_strings_relative_file_path):
    
    firebase_url_regex = r'https.*firebaseio.com'
    firebase_url_value = ""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(firebase_url_regex, line):
            firebase_match =  re.search(firebase_url_regex, line)
            firebase_url_value = firebase_match.group()
            
            firebase_response_data = send_request_to_firebase(firebase_url_value)

            
            if "Permission denied" in firebase_response_data:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.SECURED, "Firebase Url", firebase_url_value + " permission denied.")
                # report_status_secured_with_token_value("Android", application_package_name, "ResValuesStrings", "Firebase Url", firebase_url_value)
            elif "deactivated" in firebase_response_data:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.SECURED, "Firebase Url", firebase_url_value + " deactivated.")
                # report_status_secured_with_token_value("Android", application_package_name, "ResValuesStrings", "Firebase Url", firebase_url_value)
            elif len(firebase_response_data) == 0:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.HIGH, IssueStatus.VULNERABLE, "Firebase Url", firebase_url_value + " is open.")
                # report_status_vulnerable_with_token_value("Android", application_package_name, "ResValuesStrings", "Firebase Url", firebase_url_value)
            else:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.MEDIUM, IssueStatus.TO_VERIFY, "Firebase Url", firebase_url_value)
                # report_status_to_verify_with_token_value("Android", application_package_name, "ResValuesStrings", "Firebase Url", firebase_url_value + ": " + firebase_response_data)

    if len(firebase_url_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Firebase Url", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "Firebase Url")


def send_request_to_google_api(google_api_key):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountains+View,+CA&key=" + google_api_key)
    data = str(response.json())

    return data
    
def check_res_values_strings_google_api_key(application_package_name, android_res_values_strings_relative_file_path):

    # Example: <string name="google_api_key">AizaSyCBuDfLsTrMv-Q4EP1hP4Uh88Hohdl0ZCU</string>
    google_api_key_regex = r'(?:"google_api_key">)(.*)(?:<\/string>)'
    google_api_key_value = ""
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(google_api_key_regex, line):
            google_api_key_match =  re.search(google_api_key_regex, line)
            google_api_key_value = google_api_key_match.group(1)

            googleApiResponseData = send_request_to_google_api(google_api_key_value)

            if "REQUEST_DENIED" in googleApiResponseData:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.SECURED, "Google API", google_api_key_value + " permission denied.")
                # report_status_secured_with_token_value("Android", application_package_name, "ResValuesStrings", "Google API", google_api_key_value)
            else:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.VULNERABLE, "Google API", google_api_key_value + " is open.")
                # report_status_vulnerable_with_token_value("Android", application_package_name, "ResValuesStrings", "Google API", google_api_key_value)
            
    if len(google_api_key_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google API", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "Google API")


def check_res_values_strings_google_cloud_platform_google_user_content(application_package_name, android_res_values_strings_relative_file_path):

    google_cloud_platform_google_user_content_regex = r'[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com'
    google_cloud_platform_google_user_content_value = ""
    
    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(google_cloud_platform_google_user_content_regex, line):
            google_cloud_platform_google_user_content_match =  re.search(google_cloud_platform_google_user_content_regex, line)
            google_cloud_platform_google_user_content_value = google_cloud_platform_google_user_content_match.group()

            report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.FOUND, "Google Cloud Platform Google User Content", google_cloud_platform_google_user_content_value)
            # report_status_found_with_token_value("Android", application_package_name, "ResValuesStrings", "Google Cloud Platform Google User Content", google_cloud_platform_google_user_content_value)
            
    if len(google_cloud_platform_google_user_content_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google Cloud Platform Google User Content", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "Google Cloud Platform Google User Content")


def check_res_values_strings_google_oauth_access_token(application_package_name, android_res_values_strings_relative_file_path):
    
    google_oauth_access_token_regex = r'ya29\.[0-9A-Za-z_-]+'
    google_oauth_access_token_value = ""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(google_oauth_access_token_regex, line):
            google_oauth_access_token_match =  re.search(google_oauth_access_token_regex, line)
            google_oauth_access_token_value = google_oauth_access_token_match.group()

            report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.MEDIUM, IssueStatus.FOUND, "Google Oauth Access Token", google_oauth_access_token_value)
            # report_status_found_with_token_value("Android", application_package_name, "ResValuesStrings", "Google Oauth Access Token", google_oauth_access_token_value)

    if len(google_oauth_access_token_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google Oauth Access Token", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "Google Oauth Access Token")
        

def send_request_to_google_app_spot(google_app_spot):
    response = requests.get("https://" + google_app_spot)
    return response

def check_res_values_strings_google_app_spot(application_package_name, android_res_values_strings_relative_file_path):
    
    google_app_spot_regex = r'(?:>)(.*.appspot.com)(?:<)'
    google_app_spot_value = ""

    android_output_directory_relative_path = get_android_output_directory_relative_path()
    android_res_values_strings_file_path = pathlib.Path(android_output_directory_relative_path, application_package_name, android_res_values_strings_relative_file_path)
    android_res_values_strings_file_content = open(android_res_values_strings_file_path, "r").readlines()
    
    for line in android_res_values_strings_file_content:
        if re.search(google_app_spot_regex, line):
            google_app_spot_match =  re.search(google_app_spot_regex, line)
            google_app_spot_value = google_app_spot_match.group(1)

            google_app_spotResponseData = send_request_to_google_app_spot(google_app_spot_value)

            if "Error: Page not found" in google_app_spotResponseData:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.SECURED, "Google AppSpot", google_app_spot_value)
                # report_status_secured_with_token_value("Android", application_package_name, "ResValuesStrings", "Google AppSpot", google_app_spot_value)
            else:
                report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.LOW, IssueStatus.TO_VERIFY, "Google AppSpot", google_app_spot_value)
                # report_status_to_verify_with_token_value("Android", application_package_name, "ResValuesStrings", "Google AppSpot", google_app_spot_value)
            
    if len(google_app_spot_value) == 0:
        report_issue(application_package_system, application_package_name, "ResValuesStrings", IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "Google AppSpot", "")
        # report_status_not_found("Android", application_package_name, "ResValuesStrings", "Google AppSpot")