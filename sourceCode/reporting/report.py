from termcolor import colored
from sourceCode.reporting.reportEnums import UrlResourceSecurityStatus
import shutil
import os

def printOnConsoleWithoutTokenValue(applicationPackageName, fileName, issueStatus, tokenType):
    printOnConsole(applicationPackageName, fileName, issueStatus, tokenType, "")

def printOnConsole(applicationPackageName, fileName, issueStatus, tokenType, tokenValue):

    reportColor = ""
    issueStatusComment = ""

    if (UrlResourceSecurityStatus.IS_SECURE == issueStatus):
        issueStatusComment = "is secured."
        reportColor = "blue"
    elif (UrlResourceSecurityStatus.IS_VULNERABLE == issueStatus):
        issueStatusComment = "IS VUNLERABLE!"
        reportColor = "red"
    elif (UrlResourceSecurityStatus.TO_VERIFY == issueStatus):
        issueStatusComment = "to verify..."
        reportColor = "yellow"
    elif (UrlResourceSecurityStatus.NOT_FOUND == issueStatus):
        issueStatusComment = "not found."
        reportColor = "blue"
    else:
        issueStatusComment = issueStatus
        reportColor = "grey"

    if len(tokenValue) == 0:
        print(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + colored(issueStatusComment, reportColor))
    
    else:
        print(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + colored(tokenValue + ": " + issueStatusComment, reportColor))

def writeToReportFile(resultFilePath, applicationPackageName, fileName, issueStatus, tokenType, tokenValue):
    
    issueStatusComment = ""

    if (UrlResourceSecurityStatus.IS_SECURE == issueStatus):
        issueStatusComment = "is secured."
    elif (UrlResourceSecurityStatus.IS_VULNERABLE == issueStatus):
        issueStatusComment = "IS VUNLERABLE!"
    elif (UrlResourceSecurityStatus.TO_VERIFY == issueStatus):
        issueStatusComment = "to verify..."
    elif (UrlResourceSecurityStatus.NOT_FOUND == issueStatus):
        issueStatusComment = "not found."
    else:
        issueStatusComment = issueStatus

    resultFilePath = resultFilePath.replace("//", "/")

    if not(os.path.exists(resultFilePath)):
        os.makedirs(os.path.dirname(resultFilePath), exist_ok=True)
    
    print("Write to file: " + resultFilePath)

    resultFile = open(resultFilePath, "a")

    if len(tokenValue) == 0:
        resultFile.write(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + issueStatusComment + "\n")
    
    else:
        resultFile.write(applicationPackageName + ": " + fileName + ": " + tokenType + ": " + tokenValue + ": " + issueStatusComment + "\n")

    resultFile.close()

def writeToCommonReportFile(applicationPackageName, fileName, issueStatus, tokenType, tokenValue):
    writeToReportFile("./_MobileBountyHunterReport.txt", applicationPackageName, fileName, issueStatus, tokenType, tokenValue)

def writeToCommonReportFileWithoutTokenValue(applicationPackageName, fileName, issueStatus, tokenType):
    writeToCommonReportFile(applicationPackageName, fileName, issueStatus, tokenType, "")

def writeToDedicatedReportFile(outputDirectoryPath, applicationPackageName, fileName, issueStatus, tokenType, tokenValue):
    mobileBountyHunterDirectory = "_MobileBountyHunterReport"
    writeToReportFile(outputDirectoryPath + "/" + applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + "_MobileBountyHunterReport.txt", applicationPackageName, fileName, issueStatus, tokenType, tokenValue)

def writeToDedicatedReportFileWithoutTokenValue(outputDirectoryPath, applicationPackageName, fileName, issueStatus, tokenType):
    writeToDedicatedReportFile(outputDirectoryPath, applicationPackageName, fileName, issueStatus, tokenType, "")

def reportStatusVulnerableWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType, tokenValue):
    printOnConsole(applicationPackageName, fileName, UrlResourceSecurityStatus.IS_VULNERABLE, tokenType, tokenValue)
    writeToCommonReportFile(applicationPackageName, fileName, UrlResourceSecurityStatus.IS_VULNERABLE, tokenType, tokenValue)
    writeToDedicatedReportFile(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.IS_VULNERABLE, tokenType, tokenValue)

def reportStatusToVerifyWithTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType, tokenValue):
    printOnConsole(applicationPackageName, fileName, UrlResourceSecurityStatus.TO_VERIFY, tokenType, tokenValue)
    writeToCommonReportFile(applicationPackageName, fileName, UrlResourceSecurityStatus.TO_VERIFY, tokenType, tokenValue)
    writeToDedicatedReportFile(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.TO_VERIFY, tokenType, tokenValue)

def reportStatusSecureWithoutTokenValue(outputDirectoryPath, applicationPackageName, fileName, tokenType):
    printOnConsoleWithoutTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.IS_SECURE, tokenType)
    writeToCommonReportFileWithoutTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.IS_SECURE, tokenType)
    writeToDedicatedReportFileWithoutTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.IS_SECURE, tokenType)

def reportStatuNotFound(outputDirectoryPath, applicationPackageName, fileName, tokenType):
    printOnConsoleWithoutTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.NOT_FOUND, tokenType)
    writeToCommonReportFileWithoutTokenValue(applicationPackageName, fileName, UrlResourceSecurityStatus.NOT_FOUND, tokenType)
    writeToDedicatedReportFileWithoutTokenValue(outputDirectoryPath, applicationPackageName, fileName, UrlResourceSecurityStatus.NOT_FOUND, tokenType)

def copyFileToDedicatedReportDirectory(sourceFilePath, applicationPackageName):
   
    mobileBountyHunterDirectory = "_MobileBountyHunterReport"
    filename = os.path.basename(sourceFilePath)
    
    shutil.copyfile(sourceFilePath, applicationPackageName + "/" + mobileBountyHunterDirectory + "/" + filename)