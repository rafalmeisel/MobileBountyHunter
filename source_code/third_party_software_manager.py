import os
import urllib.request
import shutil
import sys
import subprocess

# Tool to full decompiling Android application with reverse engineering of source code and .smali files
def install_android_decompiler_jadx():
    
    jadx_absolute_path = '/usr/bin/jadx'

    if not os.path.exists(jadx_absolute_path):
        print("=== Installing Jadx ===")

        subprocess.run(["git", "clone", "https://github.com/skylot/jadx.git"])
        subprocess.run(["./jadx/gradlew", "dist"])
        subprocess.run(["rm", "-rf", "jadx"])

# Tool to quick decompiling Android application with reverse engineering of .smali files
def install_android_decompiler_apktools():
    
    apktool_absolute_path = '/usr/local/bin/apktool.jar'
    
    if not os.path.exists(apktool_absolute_path):
        print("=== Installing ApkTools ===")

        current_installation_step = 0
        total_installation_steps = 6
        
        current_installation_step+=1
        print("Step " + current_installation_step + "/" + total_installation_steps + ": Download Linux wrapper script")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool", "apktool.sh")

        current_installation_step+=1
        print("Step " + current_installation_step + "/" + total_installation_steps + ": Download apktool-2")
        urllib.request.urlretrieve("https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.7.0.jar", "apktool_2.7.0.jar")

        current_installation_step+=1
        print("Step " + current_installation_step + "/" + total_installation_steps + ": Rename downloaded jar to apktool.jar")
        os.rename("apktool_2.7.0.jar", "apktool.jar")

        current_installation_step+=1
        print("Step " + current_installation_step + "/" + total_installation_steps + ": Move 'apktool.jar' and 'apktool' to /usr/local/bin")
        shutil.move("apktool.sh" "/usr/local/bin/apktool.sh")
        shutil.move("apktool.jar" "/usr/local/bin/apktool.jar")

        current_installation_step+=1
        print("Step " + current_installation_step + "/" + total_installation_steps + ": Make 'apktool.jar' and 'apktool' executable (755)")
        os.chmod("/usr/local/bin/apktool.sh", 755)
        os.chmod("/usr/local/bin/apktool.jar", 755)
        
        current_installation_step+=1
        print("Step " + current_installation_step + "/" + total_installation_steps + ": Check if apktool was successfully installed")
        os.system("which apktool")
    

# Tool to download Android application from Google Play
def install_apkeep():
    
    apkeep_absolute_path = '/home/kali/.cargo/bin/apkeep'

    if not os.path.exists(apkeep_absolute_path):
        print("=== Installing Apkeep ===")
        os.system("apt install libssl-dev")
        os.system("apt install pkg-config -y")
        os.system("cargo install apkeep --locked")


# Tool to using AWS Console
def install_aws_cli():

    aws_cli_absolute_path='/usr/bin/aws'

    if not os.path.exists(aws_cli_absolute_path):
        print("=== Installing AwsCli ===")
        os.system("apt install awscli -y")


def install_third_party_software():
    
    install_android_decompiler_jadx()
    install_android_decompiler_apktools()
    install_apkeep()
    install_aws_cli()