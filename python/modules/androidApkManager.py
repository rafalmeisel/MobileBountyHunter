# 1 Read file: googlePlayDeveloperProfileUrl
# 2 Retrieve apk names from HTTP Response
# 3 Write apk names to googlePlayApksToDownload
# 4 Download apk from googlePlayApksToDownload
# 5 Decompile Apks to output

import os


def retrieveAndroidApkPackageNamesFromGooglePlayDeveloperUrlFile(GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH):


def createIfNotExistsGooglePlayDeveloperProfileUrlsFile(GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH):

    if os.path.exists(GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH):
        print("Detected file: " + GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH)

    else:
        f = open(GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH, "r")
        os.chmod(GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH, 766)
        print("Created file: " + GOOGLE_PLAY_DEVELOPERS_URLS_FILE_PATH + " - Please provide the Developers Urls from Google Play in this file.")


