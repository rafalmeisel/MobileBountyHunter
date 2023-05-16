from termcolor import colored
import re
import requests
import boto3
from sourceCode.reporting import report
from sourceCode.reporting import reportEnums

# Interesting things in AndroidManifest:
# - Api keys
# - Custom schemas
# - Hardcoded values. Developers are encouraged to store strings as reference

def checksResValuesStringsAwsLongTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    awsAkidRegex=r'(?<=>)AK(\S*?)(?=<)'
    awsAkidNotFoundText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Long Term Access Key", awsAkidValue)

    if len(awsAkidValue) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Long Term Access Key")


def checksResValuesStringsAwsShortTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    awsAkidRegex=r'(?<=>)AS(\S*?)(?=<)'
    awsAkidNotFoundText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
   
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Short Term Access Key", awsAkidValue)

    if len(awsAkidValue) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Short Term Access Key")


def checksResValuesStringsAwSecretAccessKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    awsSecretKeyRegex=r'(?:(AWS|aws).*>)(\S*)(?=<)'
    awsSecretKeyNotFoundText='Not found'
    awsSecretKeyValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    for line in androidresValuesStringsFileContent:
        if re.search(awsSecretKeyRegex, line):
            awsSecretKeyMatch =  re.search(awsSecretKeyRegex, line)
            awsSecretKeyValue = awsSecretKeyMatch.group(2)

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Secret Key", awsSecretKeyValue)

    if len(awsSecretKeyValue) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Secret Key")


def checkAwsS3BucketPermission(APPLICATION_PACKAGE_NAME, awsBucketName):
    # create an S3 client
    s3 = boto3.client('s3')

    # specify the name of the S3 bucket to check
    bucket_name = awsBucketName

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

def checksResValuesStringsAwsBucket(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    awsBucketNameRegex=r"(https:?\/\/)(.*)(.s3.amazonaws.com)"
    awsBucketNameNotFoundText='Not found'
    awsBucketNameValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsBucketNameRegex, line):
            awsBucketNameMatch =  re.search(awsBucketNameRegex, line)
            awsBucketNameValue = awsBucketNameMatch.group(2)

            awsS3BucketIsOpen = checkAwsS3BucketPermission(APPLICATION_PACKAGE_NAME, awsBucketNameValue)

            if (awsS3BucketIsOpen):
                report.reportStatusVulnerableWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Bucket", awsBucketNameValue)
            else:
                report.reportStatusSecuredWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Bucket")
            

    if len(awsBucketNameValue) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "AWS Bucket")


# https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop-mobile/ios/in-app-msg.htm
def checksResValuesStringsPushIoApplicationIdentifier(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    pushIoApplicationIdentifierRegex=r'pio-([^<]+)'
    pushIoApplicationIdentifierNotFoundText='Not found'
    pushIoApplicationIdentifierValue=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
   
    for line in resValuesStringsFileContent:
        if re.search(pushIoApplicationIdentifierRegex, line):
            pushIoApplicationIdentifierMatch =  re.search(pushIoApplicationIdentifierRegex, line)
            pushIoApplicationIdentifierValue = pushIoApplicationIdentifierMatch.group()

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "PushIoApplicationIdentifier", pushIoApplicationIdentifierValue)

    if len(pushIoApplicationIdentifierValue) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "PushIoApplicationIdentifier")

def sendRequestToFirabase(APPLICATION_PACKAGE_NAME, firebaseUrl):
    response = requests.get(firebaseUrl + "/.json")
    data = str(response.json())
    
    return data

def checksResValuesStringsFirebaseUrl(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    firebaseUrlRegex = r'https.*firebaseio.com'
    firebaseNotFoundText='Not found'
    firebaseUrl=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(firebaseUrlRegex, line):
            firebaseMatch =  re.search(firebaseUrlRegex, line)
            firebaseUrl = firebaseMatch.group()
            
            firebaseResponseData = sendRequestToFirabase(APPLICATION_PACKAGE_NAME, firebaseUrl)

            
            if "Permission denied" in firebaseResponseData:
                report.reportStatusSecuredWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Firebase Url", firebaseUrl)
            elif len(firebaseResponseData) == 0:
                report.reportStatusVulnerableWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Firebase Url", firebaseUrl)
            else:
                report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Firebase Url", firebaseUrl + ": " + firebaseResponseData)

    if len(firebaseUrl) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Firebase Url")


def sendRequestToGoogleApi(APPLICATION_PACKAGE_NAME, googleApiKey):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountains+View,+CA&key=" + googleApiKey)
    data = str(response.json())

    return data
    
def checksResValuesStringGoogleApiKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):

    # Example: <string name="google_api_key">AizaSyCBuDfLsTrMv-Q4EP1hP4Uh88Hohdl0ZCU</string>
    googleApiKeyRegex = r'(?:"google_api_key">)(.*)(?:<\/string>)'
    googleApiKeyNotFoundText='Not found'
    googleApiKey=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleApiKeyRegex, line):
            googleApiKeyMatch =  re.search(googleApiKeyRegex, line)
            googleApiKey = googleApiKeyMatch.group(1)

            googleApiResponseData = sendRequestToGoogleApi(APPLICATION_PACKAGE_NAME, googleApiKey)

            if "REQUEST_DENIED" in googleApiResponseData:
                report.reportStatusSecuredWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google API", googleApiKey)
            else:
                report.reportStatusVulnerableWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google API", googleApiKey)
            
    if len(googleApiKey) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google API")


def checksResValuesStringGoogleCloudPlatformGoogleUserContent(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):

    googleCloudPlatformGoogleUserContentRegex = r'[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com'
    googleCloudPlatformGoogleUserContentNotFoundText='Not found'
    googleCloudPlatformGoogleUserContent=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleCloudPlatformGoogleUserContentRegex, line):
            googleCloudPlatformGoogleUserContentMatch =  re.search(googleCloudPlatformGoogleUserContentRegex, line)
            googleCloudPlatformGoogleUserContent = googleCloudPlatformGoogleUserContentMatch.group()

            report.reportStatusFoundWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google Cloud Platform Google User Content", googleCloudPlatformGoogleUserContent)
            
    if len(googleCloudPlatformGoogleUserContent) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google Cloud Platform Google User Content")


def checksResValuesStringGoogleOAuthAccessToken(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    googleOAuthAccessTokenRegex = r'ya29\.[0-9A-Za-z_-]+'
    googleOAuthAccessTokenNotFoundText='Not found'
    googleOAuthAccessToken=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleOAuthAccessTokenRegex, line):
            googleOAuthAccessTokenMatch =  re.search(googleOAuthAccessTokenRegex, line)
            googleOAuthAccessToken = googleOAuthAccessTokenMatch.group()

            report.reportStatusFoundWithoutTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google Oauth Access Token", googleOAuthAccessToken)

    if len(googleOAuthAccessToken) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google Oauth Access Token")
        

def sendRequestToGoogleAppSpot(APPLICATION_PACKAGE_NAME, googleAppSpot):
    response = requests.get("https://" + googleAppSpot)
    return response

def checksResValuesStringGoogleAppSpot(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH):
    
    googleAppSpotRegex = r'(?:>)(.*.appspot.com)(?:<)'
    googleAppSpotNotFoundText='Not found'
    googleAppSpot=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleAppSpotRegex, line):
            googleAppSpotMatch =  re.search(googleAppSpotRegex, line)
            googleAppSpot = googleAppSpotMatch.group(1)

            googleAppSpotResponseData = sendRequestToGoogleAppSpot(APPLICATION_PACKAGE_NAME, googleAppSpot)

            if "Error: Page not found" in googleAppSpotResponseData:
                report.reportStatusSecuredWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google AppSpot", googleAppSpot)
            else:
                report.reportStatusToVerifyWithTokenValue(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google AppSpot", googleAppSpot)
            
    if len(googleAppSpot) == 0:
        report.reportStatusNotFound(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, "ResValuesStrings", "Google AppSpot")