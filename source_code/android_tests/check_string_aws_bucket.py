# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

import boto3
import re
from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# [2023.06.21] Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html
# Valid AWS Bucket Url: https://bucket-name.s3.amazonaws.com
# Valid AWS Bucket Url: https://my-files.s3.amazonaws.com
# Valid AWS Bucket Url: https://images-bucket.s3.amazonaws.com

def check_string_aws_bucket(file_content):
    
    aws_bucket_regex = 'https:\/\/.*\.s3\.amazonaws\.com'
    aws_bucket_items_list = []

    aws_bucket_items_list = re.findall(aws_bucket_regex, file_content)
    
    return aws_bucket_items_list

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
                            return True
                            break
    return False

def run_check_string_aws_bucket(application_package_system, application_package_name, file_name, file_content):

    aws_bucket_items_list = check_string_aws_bucket(file_content)
    
    if len(aws_bucket_items_list) > 0:
        for aws_bucket_item in aws_bucket_items_list:
            
            aws_s3_bucket_is_open = check_aws_s3_bucket_permission(aws_bucket_item)

            if (aws_s3_bucket_is_open):
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.HIGH, IssueStatus.VULNERABLE, "AWS Bucket", aws_bucket_item)
            
            else:
                report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.SECURED, "AWS Bucket", aws_bucket_item)
            
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "AWS Bucket", "")