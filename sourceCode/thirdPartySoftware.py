import os
import urllib.request
import shutil
import sys
import subprocess

APKTOOL_PATH = '/usr/local/bin/apktool.jar'
RUST_PATH = '/home/kali/.cargo/bin/rustc'
APKEEP_PATH = '/home/kali/.cargo/bin/apkeep'
AWSCLI_PATH='/usr/bin/aws'

def installApkTools():
    
    if not os.path.exists(APKTOOL_PATH):
        
        currentInstallationStep = 0
        totalInstallationSteps = 6

        print("ApkTool is not installed. Start installing...")
        
        currentInstallationStep+=1
        print("Step " + currentInstallationStep + "/" + totalInstallationSteps + ": Download Linux wrapper script")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool", "apktool.sh")

        currentInstallationStep+=1
        print("Step " + currentInstallationStep + "/" + totalInstallationSteps + ": Download apktool-2")
        urllib.request.urlretrieve("https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.7.0.jar", "apktool_2.7.0.jar")

        currentInstallationStep+=1
        print("Step " + currentInstallationStep + "/" + totalInstallationSteps + ": Rename downloaded jar to apktool.jar")
        os.rename("apktool_2.7.0.jar", "apktool.jar")

        currentInstallationStep+=1
        print("Step " + currentInstallationStep + "/" + totalInstallationSteps + ": Move 'apktool.jar' and 'apktool' to /usr/local/bin")
        shutil.move("apktool.sh" "/usr/local/bin/apktool.sh")
        shutil.move("apktool.jar" "/usr/local/bin/apktool.jar")

        currentInstallationStep+=1
        print("Step " + currentInstallationStep + "/" + totalInstallationSteps + ": Make 'apktool.jar' and 'apktool' executable (755)")
        os.chmod("/usr/local/bin/apktool.sh", 755)
        os.chmod("/usr/local/bin/apktool.jar", 755)
        
        currentInstallationStep+=1
        print("Step " + currentInstallationStep + "/" + totalInstallationSteps + ": Check if apktool was successfully installed")
        os.system("which apktool")
    
def installRust():
    
    if not os.path.exists(RUST_PATH):

        urllib.request.urlretrieve("https://sh.rustup.rs", "rustup-init.sh")
        os.system("sh rustup-init.sh")
        os.system("source '$HOME/.cargo/env'")
        os.system("which apktool")
    

def installApkeep():
    
    if not os.path.exists(APKEEP_PATH):

        os.system("apt install libssl-dev")
        os.system("apt install pkg-config -y")
        os.system("cargo install apkeep --locked")


def installAwsCli():

    if not os.path.exists(AWSCLI_PATH):

        os.system("apt install awscli -y")

def installBoto3():
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'boto3'])


def installThirdPartySoftware():
    
    installApkTools()
    installRust()
    installApkeep()
    installAwsCli()
    installBoto3()