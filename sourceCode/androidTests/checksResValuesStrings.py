from termcolor import colored
import re
import requests
import boto3

# Interesting things in AndroidManifest:
# - Api keys
# - Custom schemas
# - Hardcoded values. Developers are encouraged to store strings as reference

def checksResValuesStringsAwsLongTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsAkidRegex=r'(?<=>)AK(\S*?)(?=<)'
    awsAkidNotFoundText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Long Term Access Key: " + awsAkidValue + "\n")
            print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Long Term Access Key: ", colored(awsAkidValue, 'red'))

    if len(awsAkidValue) == 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Long Term Access Key: ", colored(awsAkidNotFoundText, 'blue'))

    resultFile.close()


def checksResValuesStringsAwsShortTermAccessKeys(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsAkidRegex=r'(?<=>)AS(\S*?)(?=<)'
    awsAkidNotFoundText='Not found'
    awsAkidValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsAkidRegex, line):
            awsAkidMatch =  re.search(awsAkidRegex, line)
            awsAkidValue = awsAkidMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Short Term Access Key: " + awsAkidValue + "\n")
            print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Short Term Access Key: ", colored(awsAkidValue, 'red'))

    if len(awsAkidValue) == 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Short Term Access Key: ", colored(awsAkidNotFoundText, 'blue'))

    resultFile.close()


def checksResValuesStringsAwSecretAccessKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsSecretKeyRegex=r'(?:(AWS|aws).*>)(\S*)(?=<)'
    awsSecretKeyNotFoundText='Not found'
    awsSecretKeyValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsSecretKeyRegex, line):
            awsSecretKeyMatch =  re.search(awsSecretKeyRegex, line)
            awsSecretKeyValue = awsSecretKeyMatch.group(2)

            resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS Secret Key: " + awsSecretKeyValue + "\n")
            print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Secret Key: ", colored(awsSecretKeyValue, 'red'))

    if len(awsSecretKeyValue) == 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS Secret Key: ", colored(awsSecretKeyNotFoundText, 'blue'))

    resultFile.close()

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

def checksResValuesStringsAwsBucket(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    awsBucketNameRegex=r"(https:?\/\/)(.*)(.s3.amazonaws.com)"
    awsBucketNameNotFoundText='Not found'
    awsBucketNameValue=""

    androidresValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in androidresValuesStringsFileContent:
        if re.search(awsBucketNameRegex, line):
            awsBucketNameMatch =  re.search(awsBucketNameRegex, line)
            awsBucketNameValue = awsBucketNameMatch.group(2)

            awsS3BucketIsOpen = checkAwsS3BucketPermission(APPLICATION_PACKAGE_NAME, awsBucketName)

            if (awsS3BucketIsOpen):
                resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS URL: " + awsBucketNameValue + ": is OPEN.\n")
                print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS URL: ", colored(awsBucketNameValue + " is OPEN!", 'red'))
            else:
                resultFile.write(APPLICATION_PACKAGE_NAME + ": " + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH + ": AWS URL: " + awsBucketNameValue + "is closed.\n")
                print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS URL: ", colored(awsBucketNameValue + "is closed", 'blue'))
            

    if len(awsBucketNameValue) == 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: AWS URL: ", colored(awsBucketNameNotFoundText, 'blue'))

    resultFile.close()


# https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop-mobile/ios/in-app-msg.htm
def checksResValuesStringsPushIoApplicationIdentifier(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    pushIoApplicationIdentifierRegex=r'pio-([^<]+)'
    pushIoApplicationIdentifierNotFoundText='Not found'
    pushIoApplicationIdentifierValue=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()

    resultFile = open(RESULT_FILE_PATH, "a")
    
    for line in resValuesStringsFileContent:
        if re.search(pushIoApplicationIdentifierRegex, line):
            pushIoApplicationIdentifierMatch =  re.search(pushIoApplicationIdentifierRegex, line)
            pushIoApplicationIdentifierValue = pushIoApplicationIdentifierMatch.group()

            resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: PushIoApplicationIdentifier: " + pushIoApplicationIdentifierValue + "\n")
            print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: PushIoApplicationIdentifier: ", colored(pushIoApplicationIdentifierValue, 'red'))

    if len(pushIoApplicationIdentifierValue) == 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: PushIoApplicationIdentifier: ", colored(pushIoApplicationIdentifierNotFoundText, 'blue'))

    resultFile.close()


def checkFirabasePermission(APPLICATION_PACKAGE_NAME, firebaseUrl, RESULT_FILE_PATH):
    response = requests.get(firebaseUrl + "/.json")
    data = str(response.json())

    resultFile = open(RESULT_FILE_PATH, "a")

    if "Permission denied" in data:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + colored(firebaseUrl, 'yellow') + ": " + colored(data, 'blue'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + firebaseUrl + ": Secured" + "\n")
    elif len(data) == 0:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + colored(firebaseUrl, 'yellow') + ": " + colored(data, 'red'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + firebaseUrl + ": OPEN!" + "\n")
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + colored(firebaseUrl, 'yellow') + ": " + colored(data, 'yellow'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: " + firebaseUrl + ": To check" + "\n")
    
    resultFile.close()

def checksResValuesStringsFirebaseUrl(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    firebaseUrlRegex = r'https.*firebaseio.com'
    firebaseNotFoundText='Not found'
    firebaseUrl=""

    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(firebaseUrlRegex, line):
            firebaseMatch =  re.search(firebaseUrlRegex, line)
            firebaseUrl = firebaseMatch.group()
            
            # print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: ", colored(firebaseUrl, 'red'))
            checkFirabasePermission(APPLICATION_PACKAGE_NAME, firebaseUrl, RESULT_FILE_PATH)

    if len(firebaseUrl) == 0:
        resultFile = open(RESULT_FILE_PATH, "a")
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Firebase Url: ", colored(firebaseNotFoundText, 'blue'))
        resultFile.close()


def checkGoogleApiPermission(APPLICATION_PACKAGE_NAME, googleApiKey, RESULT_FILE_PATH):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountains+View,+CA&key=" + googleApiKey)
    data = str(response.json())

    resultFile = open(RESULT_FILE_PATH, "a")

    if "REQUEST_DENIED" in data:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google API: " + colored(googleApiKey, 'yellow') + ": " + colored("Secured", 'blue'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google API: " + googleApiKey + ": Secured" + "\n")
    else:
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google API: " + colored(googleApiKey, 'yellow') + ": " + colored("OPEN!", 'red'))
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google API: " + googleApiKey + ": OPEN!" + "\n")

    resultFile.close()

    
def checksResValuesStringGoogleApiKey(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):

    # Example: <string name="google_api_key">AizaSyCBuDfLsTrMv-Q4EP1hP4Uh88Hohdl0ZCU</string>
    googleApiKeyRegex = r'(?:"google_api_key">)(.*)(?:<\/string>)'
    googleApiKeyNotFoundText='Not found'
    googleApiKey=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleApiKeyRegex, line):
            googleApiKeyMatch =  re.search(googleApiKeyRegex, line)
            googleApiKey = googleApiKeyMatch.group(1)

            # print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google API Key: ", colored(googleApiKey, 'red'))
            checkGoogleApiPermission(APPLICATION_PACKAGE_NAME, googleApiKey, RESULT_FILE_PATH)

    if len(googleApiKey) == 0:
        resultFile = open(RESULT_FILE_PATH, "a")
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google API Key: ", colored(googleApiKeyNotFoundText, 'blue'))
        resultFile.close()


def checksResValuesStringGoogleCloudPlatformGoogleUserContent(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):

    googleCloudPlatformGoogleUserContentRegex = r'[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com'
    googleCloudPlatformGoogleUserContentNotFoundText='Not found'
    googleCloudPlatformGoogleUserContent=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleCloudPlatformGoogleUserContentRegex, line):
            googleCloudPlatformGoogleUserContentMatch =  re.search(googleCloudPlatformGoogleUserContentRegex, line)
            googleCloudPlatformGoogleUserContent = googleCloudPlatformGoogleUserContentMatch.group()

            print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Cloud Platform Google User Content: ", colored(googleCloudPlatformGoogleUserContent, 'red'))
            
            resultFile = open(RESULT_FILE_PATH, "a")
            resultFile.write(APPLICATION_PACKAGE_NAME + ": Google Cloud Platform Google User Content: " + googleCloudPlatformGoogleUserContent + "\n")
            resultFile.close()

    if len(googleCloudPlatformGoogleUserContent) == 0:
        
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Cloud Platform Google User Content: ", colored(googleCloudPlatformGoogleUserContentNotFoundText, 'blue'))
        
        resultFile = open(RESULT_FILE_PATH, "a")
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Cloud Platform Google User Content: " + googleCloudPlatformGoogleUserContent + "\n")
        resultFile.close()

def checksResValuesStringGoogleOAuthAccessToken(OUTPUT_DIRECTORY_PATH, APPLICATION_PACKAGE_NAME, ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, RESULT_FILE_PATH):
    
    googleOAuthAccessTokenRegex = r'ya29\.[0-9A-Za-z_-]+'
    googleOAuthAccessTokenNotFoundText='Not found'
    googleOAuthAccessToken=""

    
    resValuesStringsFileContent = open(OUTPUT_DIRECTORY_PATH + APPLICATION_PACKAGE_NAME + ANDROID_RES_VALUES_STRINGS_RELATIVE_FILE_PATH, "r").readlines()
    
    for line in resValuesStringsFileContent:
        if re.search(googleOAuthAccessTokenRegex, line):
            googleOAuthAccessTokenMatch =  re.search(googleOAuthAccessTokenRegex, line)
            googleOAuthAccessToken = googleOAuthAccessTokenMatch.group()

            print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Oauth Access Token: ", colored(googleOAuthAccessToken, 'red'))
            
            resultFile = open(RESULT_FILE_PATH, "a")
            resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Oauth Access Token: " + googleOAuthAccessToken + "\n")
            resultFile.close()

    if len(googleOAuthAccessToken) == 0:
        
        print(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Oauth Access Token: ", colored(googleOAuthAccessTokenNotFoundText, 'blue'))
        
        resultFile = open(RESULT_FILE_PATH, "a")
        resultFile.write(APPLICATION_PACKAGE_NAME + ": ResValuesStrings: Google Oauth Access Token: " + googleOAuthAccessToken + "\n")
        resultFile.close()