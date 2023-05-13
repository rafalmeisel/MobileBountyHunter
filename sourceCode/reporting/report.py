from termcolor import colored
from sourceCode.reporting.reportEnums import UrlResourceSecurityStatus
import shutil
import os
import hashlib
from random import seed
from random import randint

def printOnConsoleWithoutTokenValue(applicationPackageName, fileName, issueStatus, tokenType):
    printOnConsoleWithTokenValue(applicationPackageName, fileName, issueStatus, tokenType, "")

def printOnConsoleWithTokenValue(applicationPackageName, fileName, issueStatus, tokenType, tokenValue):

    reportColor = ""
    issueStatusComment = ""

    if (UrlResourceSecurityStatus.SECURED == issueStatus):
        issueStatusComment = "is secured."
        reportColor = "blue"
    elif (UrlResourceSecurityStatus.VULNERABLE == issueStatus):
        issueStatusComment = "IS VUNLERABLE!"
        reportColor = "red"
    elif (UrlResourceSecurityStatus.TO_VERIFY == issueStatus):
        issueStatusComment = "to verify..."
        reportColor = "yellow"
    elif (UrlResourceSecurityStatus.NOT_FOUND == issueStatus):
        issueStatusComment = "not found."
        reportColor = "blue"
    elif (UrlResourceSecurityStatus.FOUND == issueStatus):
        issueStatusComment = "FOUND!"
        reportColor = "red"
    else:
        issueStatusComment = issueStatus
        reportColor = "grey"

    if len(tokenValue) == 0:
        print(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + colored(issueStatusComment, reportColor))
    
    else:
        print(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + colored(tokenValue + ": " + issueStatusComment, reportColor))

def writeToReportFile(resultFilePath, applicationPackageName, fileName, issueStatus, tokenType, tokenValue):
    
    issueStatusComment = ""

    if (UrlResourceSecurityStatus.SECURED == issueStatus):
        issueStatusComment = "is secured."
    elif (UrlResourceSecurityStatus.VULNERABLE == issueStatus):
        issueStatusComment = "IS VUNLERABLE!"
    elif (UrlResourceSecurityStatus.TO_VERIFY == issueStatus):
        issueStatusComment = "to verify..."
    elif (UrlResourceSecurityStatus.NOT_FOUND == issueStatus):
        issueStatusComment = "not found."
    elif (UrlResourceSecurityStatus.FOUND == issueStatus):
        issueStatusComment = "FOUND!"
    else:
        issueStatusComment = issueStatus

    resultFilePath = resultFilePath.replace("//", "/")

    if not(os.path.exists(resultFilePath)):
        os.makedirs(os.path.dirname(resultFilePath), exist_ok=True)
    
    resultFile = open(resultFilePath, "a")

    if len(tokenValue) == 0:
        resultFile.write(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + issueStatusComment + "\n")
    
    else:
        resultFile.write(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + tokenValue + ": " + issueStatusComment + "\n")

    resultFile.close()



def writeToCommonReportFileWithTokenValue(applicationPackageName, fileName, issueStatus, tokenType, tokenValue):
    writeToReportFile("./_MobileBountyHunterReport.txt", applicationPackageName, fileName, issueStatus, tokenType, tokenValue)

def writeToCommonReportFileWithoutTokenValue(applicationPackageName, fileName, issueStatus, tokenType):
    writeToCommonReportFileWithTokenValue(applicationPackageName, fileName, issueStatus, tokenType, "")



def writeToDedicatedReportFileWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, issueStatus, tokenType, tokenValue):
    mobileBountyHunterDirectory = "_MobileBountyHunterReport"
    writeToReportFile(outputDirectoryPath + "/" + applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + "_MobileBountyHunterReport.txt", applicationPackageName, fileName, issueStatus, tokenType, tokenValue)

def writeToDedicatedReportFileWithoutTokenValue(outputDirectoryPath, applicationPackageName, fileName, issueStatus, tokenType):
    writeToDedicatedReportFileWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, issueStatus, tokenType, "")




def reportStatusVulnerableWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType, tokenValue):
    printOnConsoleWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.VULNERABLE, tokenType, tokenValue)
    writeToCommonReportFileWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.VULNERABLE, tokenType, tokenValue)
    writeToDedicatedReportFileWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.VULNERABLE, tokenType, tokenValue)

def reportStatusToVerifyWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType, tokenValue):
    printOnConsoleWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.TO_VERIFY, tokenType, tokenValue)
    writeToCommonReportFileWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.TO_VERIFY, tokenType, tokenValue)
    writeToDedicatedReportFileWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.TO_VERIFY, tokenType, tokenValue)

def reportStatusSecuredWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType, tokenValue):
    printOnConsoleWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.SECURED, tokenType, tokenValue)
    writeToCommonReportFileWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.SECURED, tokenType, tokenValue)
    writeToDedicatedReportFileWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.SECURED, tokenType, tokenValue)

def reportStatusFoundWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType, tokenValue):
    printOnConsoleWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.FOUND, tokenType, tokenValue)
    writeToCommonReportFileWithTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.FOUND, tokenType, tokenValue)
    writeToDedicatedReportFileWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.FOUND, tokenType, tokenValue)

def reportStatusNotFound(outputDirectoryPath, applicationPackageName, fileName, tokenType):
    printOnConsoleWithoutTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.NOT_FOUND, tokenType)
    writeToCommonReportFileWithoutTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.NOT_FOUND, tokenType)
    writeToDedicatedReportFileWithoutTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.NOT_FOUND, tokenType)



def copyFileToDedicatedReportDirectory(sourceFilePath, outputDirectoryPath, applicationPackageName):
   
    mobileBountyHunterDirectory = "_MobileBountyHunterReport"
    filename = os.path.basename(sourceFilePath)
    
    filenameAlreadyExists = os.path.isfile(outputDirectoryPath + "/" + applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + filename)

    if (filenameAlreadyExists):
        # Calculate MD5 of already existing file with new one
        # If MD5 are the same, skip copying
        # If MD5 are different, copy file with adding suffix _1, _2, etc.

        md5ExistedFile = ""
        md5NewFile = ""
        existedFilePath = outputDirectoryPath + "/" + applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + filename

        with open(existedFilePath, 'rb') as file_to_check:
            data = file_to_check.read()    
            md5ExistedFile = hashlib.md5(data).hexdigest()

        with open(sourceFilePath, 'rb') as file_to_check:
            data = file_to_check.read()    
            md5NewFile = hashlib.md5(data).hexdigest()

        if (md5ExistedFile == md5NewFile):
            print("Found file \"" + sourceFilePath + "\"" + "was already copied (comapred MD5s). Skipping...")
        
        else:
            seed(1)
            randomValue = str(randint(0, 100000000))

            shutil.copyfile(sourceFilePath, outputDirectoryPath + "/" + applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + filename + "_" + randomValue)
    else:
        shutil.copyfile(sourceFilePath, outputDirectoryPath + "/" + applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + filename)