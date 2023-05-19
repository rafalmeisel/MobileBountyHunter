# from sourceCode.environment import *
from sourceCode.thirdPartySoftware import installThirdPartySoftware
from sourceCode.directories import createDirectories
import sourceCode.applicationManager

import sys
import getopt

# Parameters:
# -h / help - show help
# -f / apkFile - analyze specified application file
# -i / inputDirectory - analyze all applications in input
# -o / outputDirectory - output directory
# -l / apksListFile - analyze application listed in file
# -s / storeUrlsFile - analyze applications from storeUrls file
# -d / decompilingTool - decompile application with specific tool like apktool, jadx
# -u / directUrl - analyze specified URL - can be url to specified android/ios apk, specified android/ios developer

def main(argv):
    
    USER_CHOICE=""
    INPUT_DIRECTORY_PATH = "./workspace/input/"
    INPUT_ANALYZED_DIRECTORY_PATH = "./workspace/input_analyzed/"
    OUTPUT_DIRECTORY_PATH = "./workspace/output/"
    OUTPUT_ANALYZED_DIRECTORY_PATH = "./workspace/output_analyzed/"
    APPLICATION_LIST_FILE_PATH = "./workspace/apksList.txt"
    DEVELOPERS_URLS_PROFILE_FILE = "./workspace/storeUrlsList.txt"
    DECOMPILING_TOOL="apktools"
    APK_FILE = ""
    URL = ""

    opts, args = getopt.getopt(argv,"hf:iolsu:d:",["apkFile=", "inputDirectory=", "outputDirectory=", "apksListFile=", "storeUrlsListFile=", "decompilingTool=", "url="])
   
    for opt, arg in opts:
        if opt == '-h':
            print ('main.py -h [help] -a [all] -f <apkFile> -i <inputDirectory> -u <urlToStore>')
            sys.exit()

        elif opt in ("-f", "--apkFile"):
            if len(arg)>0:
                APK_FILE = arg
            USER_CHOICE="apkFile"

        elif opt in ("-i", "--inputDirectory"):
            if len(arg)>0:
                INPUT_DIRECTORY_PATH = arg
            USER_CHOICE="inputDirectory"

        elif opt in ("-o", "--outputDirectory"):
            if len(arg)>0:
                OUTPUT_DIRECTORY_PATH = arg
            USER_CHOICE="outputDirectory"

        elif opt in ("-l", "--apksListFile"):
            if len(arg)>0:
                APPLICATION_LIST_FILE_PATH = arg
            USER_CHOICE="apksListFile"

        elif opt in ("-s", "--storeUrlsListFile"):
            if len(arg)>0:
                STORE_URL = arg
            USER_CHOICE="storeUrlsListFile"

        elif opt in ("-u", "--url"):
            if len(arg)>0:
                DIRECT_URL = arg
            USER_CHOICE="url"
        elif opt in ("-d", "--decompilingTool"):
            if len(arg)>0:
                selectedDecompilingdTool = arg
                if selectedDecompilingdTool == "apktools":
                    DECOMPILING_TOOL = "apktools"
                elif selectedDecompilingdTool == "jadx":
                    DECOMPILING_TOOL = "jadx"
                else:
                    DECOMPILING_TOOL = "apktools"

    installThirdPartySoftware()
    createDirectories(DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)

    match USER_CHOICE:
        case "apkFile":
            print("Analyze selected apkFile. Will be added later.")

        case "inputDirectory":
            print("Analyze selected inputDirectory")
            sourceCode.applicationManager.analyzeInputDirectory(DECOMPILING_TOOL, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)

        case "outputDirectory":
            print("Analyze selected outputDirectory")
            sourceCode.applicationManager.analyzeOutputDirectory(OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)

        case "apksListFile":
            print("Analyze selected apksListFile")
            sourceCode.applicationManager.analyzeApplicationFromList(DECOMPILING_TOOL, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)

        case "storeUrlsListFile":
            sourceCode.applicationManager.runAnalyzeApplicationFromStoreUrlList(DECOMPILING_TOOL, DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)

        case "url":
            print("Analyze selected url. Will be added later.")

        case _:
            print("Default")
            sourceCode.applicationManager.runAnalyzeApplicationFromStoreUrlList(DECOMPILING_TOOL, DEVELOPERS_URLS_PROFILE_FILE, APPLICATION_LIST_FILE_PATH, INPUT_DIRECTORY_PATH, INPUT_ANALYZED_DIRECTORY_PATH, OUTPUT_DIRECTORY_PATH, OUTPUT_ANALYZED_DIRECTORY_PATH)

    

if __name__ == '__main__':
    main(sys.argv[1:])