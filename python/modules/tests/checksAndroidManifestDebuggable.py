from termcolor import colored
import re

def checksAndroidManifestDebuggable(apkName, pathToAndroidManifest, pathToResultFile):
    
    debuggableFalseRegexText='debuggable="false"'
    debuggableTrueRegexText='debuggable="true"'
    debuggableTrueRegexCompiled=re.compile(debuggableTrueRegexText)

    androidManifestFileContent = open(pathToAndroidManifest, "r").readlines()

    resultFile = open(pathToResultFile, "a")
    
    for line in androidManifestFileContent:
        if re.search(debuggableTrueRegexCompiled, line):
            print(apkName + ": AndroidManifest: ", colored(debuggableTrueRegexCompiled, 'red'))
            resultFile.write(apkName + ": AndroidManifest: " + debuggableTrueRegexCompiled)
        else:
            print(apkName + ": AndroidManifest: ", colored(debuggableFalseRegexText, 'blue'))
            resultFile.write(apkName + ": AndroidManifest: " + debuggableFalseRegexText)

    resultFile.close()