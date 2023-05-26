from termcolor import colored
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus
import re
import requests
import boto3
from source_code.report_manager import *

application_package_system = "Android"

# Interesting things in AndroidManifest:
# - Api keys
# - Custom schemas
# - Hardcoded values. Developers are encouraged to store strings as reference

def check_res_values_strings_aws_long_term_access_keys(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    aws_akid_regex = r'(?<=>)AK(\S*?)(?=<)'
    aws_akid_value = ""
    issue_type = "AWS Long Term Access Key"

    for line in android_values_strings_content:
        if re.search(aws_akid_regex, line):
            aws_akid_match =  re.search(aws_akid_regex, line)
            aws_akid_value = aws_akid_match.group()

            report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.MEDIUM, IssueStatus.FOUND, issue_type, aws_akid_value)

    if len(aws_akid_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")


def check_res_values_strings_aws_short_term_access_keys(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    aws_akid_regex = r'(?<=>)AS(\S*?)(?=<)'
    aws_akid_value = ""
    issue_type = "AWS Short Term Access Key"
   
    for line in android_values_strings_content:
        if re.search(aws_akid_regex, line):
            aws_akid_match =  re.search(aws_akid_regex, line)
            aws_akid_value = aws_akid_match.group()
            
            report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.MEDIUM, IssueStatus.FOUND, issue_type, aws_akid_value)

    if len(aws_akid_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")


def check_res_values_strings_aws_secret_access_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    aws_secret_key_regex = r'(?:(AWS|aws).*>)(\S*)(?=<)'
    aws_secret_key_value = ""
    issue_type = "AWS Secret Key"

    for line in android_values_strings_content:
        if re.search(aws_secret_key_regex, line):
            aws_secret_key_match =  re.search(aws_secret_key_regex, line)
            aws_secret_key_value = aws_secret_key_match.group(2)
            
            report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.MEDIUM, IssueStatus.FOUND, issue_type, aws_secret_key_value)

    if len(aws_secret_key_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")


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

def check_res_values_strings_aws_bucket(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    aws_bucket_name_regex = r"(https:?\/\/)(.*)(.s3.amazonaws.com)"
    aws_bucket_name_value = ""
    issue_type = "AWS Bucket"
    
    
    for line in android_values_strings_content:
        if re.search(aws_bucket_name_regex, line):
            aws_bucket_name_match =  re.search(aws_bucket_name_regex, line)
            aws_bucket_name_value = aws_bucket_name_match.group(2)

            aws_s3_bucket_is_open = check_aws_s3_bucket_permission(application_package_name, aws_bucket_name_value)

            if (aws_s3_bucket_is_open):
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.HIGH, IssueStatus.VULNERABLE, issue_type, aws_bucket_name_value)
            
            else:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.SECURED, issue_type, aws_bucket_name_value)
            

    if len(aws_bucket_name_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")


# https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop-mobile/ios/in-app-msg.htm
def check_res_values_strings_push_io_application_identifier(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    push_io_application_identifier_regex = r'pio-([^<]+)'
    push_io_application_identifier_value = ""
    issue_type = "PushIoApplicationIdentifier"
    
   
    for line in android_values_strings_content:
        if re.search(push_io_application_identifier_regex, line):
            pushIoApplicationIdentifier_match =  re.search(push_io_application_identifier_regex, line)
            push_io_application_identifier_value = pushIoApplicationIdentifier_match.group()

            report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.MEDIUM, IssueStatus.FOUND, issue_type, push_io_application_identifier_value)

    if len(push_io_application_identifier_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")

def send_request_to_firebase(firebase_url):
    response = requests.get(firebase_url + "/.json")
    data = str(response.json())
    
    return data

def check_res_values_strings_firebase_url(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    firebase_url_regex = r'https.*firebaseio.com'
    firebase_url_value = ""
    issue_type = "Firebase Url"
    
    
    for line in android_values_strings_content:
        if re.search(firebase_url_regex, line):
            firebase_match =  re.search(firebase_url_regex, line)
            firebase_url_value = firebase_match.group()
            
            firebase_response_data = send_request_to_firebase(firebase_url_value)

            
            if "Permission denied" in firebase_response_data:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.SECURED, issue_type, firebase_url_value + " permission denied.")
                
            elif "deactivated" in firebase_response_data:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.SECURED, issue_type, firebase_url_value + " deactivated.")
                
            elif len(firebase_response_data) == 0:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.HIGH, IssueStatus.VULNERABLE, issue_type, firebase_url_value + " is open.")
                
            else:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.MEDIUM, IssueStatus.TO_VERIFY, issue_type, firebase_url_value)
                

    if len(firebase_url_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")
        


def send_request_to_google_api(google_api_key):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountains+View,+CA&key=" + google_api_key)
    data = str(response.json())

    return data
    
def check_res_values_strings_google_api_key(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):

    # Example: <string name="google_api_key">AizaSyCBuDfLsTrMv-Q4EP1hP4Uh88Hohdl0ZCU</string>
    google_api_key_regex = r'(?:"google_api_key">)(.*)(?:<\/string>)'
    google_api_key_value = ""
    issue_type = "Google API"
    
    for line in android_values_strings_content:
        if re.search(google_api_key_regex, line):
            google_api_key_match =  re.search(google_api_key_regex, line)
            google_api_key_value = google_api_key_match.group(1)

            googleApiResponseData = send_request_to_google_api(google_api_key_value)

            if "REQUEST_DENIED" in googleApiResponseData:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.SECURED, issue_type, google_api_key_value + " permission denied.")
                
            else:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.VULNERABLE, issue_type, google_api_key_value + " is open.")
                
            
    if len(google_api_key_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")
        


def check_res_values_strings_google_cloud_platform_google_user_content(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):

    google_cloud_platform_google_user_content_regex = r'[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com'
    google_cloud_platform_google_user_content_value = ""
    issue_type = "Google Cloud Platform Google User Content"
    
    for line in android_values_strings_content:
        if re.search(google_cloud_platform_google_user_content_regex, line):
            google_cloud_platform_google_user_content_match =  re.search(google_cloud_platform_google_user_content_regex, line)
            google_cloud_platform_google_user_content_value = google_cloud_platform_google_user_content_match.group()

            report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.FOUND, issue_type, google_cloud_platform_google_user_content_value)
            
            
    if len(google_cloud_platform_google_user_content_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")
        


def check_res_values_strings_google_oauth_access_token(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    google_oauth_access_token_regex = r'ya29\.[0-9A-Za-z_-]+'
    google_oauth_access_token_value = ""
    issue_type = "Google Oauth Access Token"
    
    for line in android_values_strings_content:
        if re.search(google_oauth_access_token_regex, line):
            google_oauth_access_token_match =  re.search(google_oauth_access_token_regex, line)
            google_oauth_access_token_value = google_oauth_access_token_match.group()

            report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.MEDIUM, IssueStatus.FOUND, issue_type, google_oauth_access_token_value)

    if len(google_oauth_access_token_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")

        

def send_request_to_google_app_spot(google_app_spot):
    response = requests.get("https://" + google_app_spot)
    response_body = response.text
    return response_body

def check_res_values_strings_google_app_spot(application_package_system, application_package_name, android_values_strings_basename, android_values_strings_content):
    
    google_app_spot_regex = r'(?:>)(.*.appspot.com)(?:<)'
    google_app_spot_value = ""
    issue_type = "Google AppSpot"
    
    for line in android_values_strings_content:
        if re.search(google_app_spot_regex, line):
            google_app_spot_match =  re.search(google_app_spot_regex, line)
            google_app_spot_value = google_app_spot_match.group(1)

            google_app_spot_response_data = send_request_to_google_app_spot(google_app_spot_value)
            
            if "Error: Page not found" in google_app_spot_response_data:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.SECURED, issue_type, "Error: Page not found: " + google_app_spot_value)
            
            elif "Error: Server Error" in google_app_spot_response_data:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.TO_VERIFY, issue_type, "Error: Server Error: " + google_app_spot_value)                

            else:
                report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.LOW, IssueStatus.TO_VERIFY, issue_type, google_app_spot_value)
                
            
    if len(google_app_spot_value) == 0:
        report_issue(application_package_system, application_package_name, android_values_strings_basename, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, issue_type, "")
        