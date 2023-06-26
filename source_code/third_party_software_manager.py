import os
import subprocess

# Tool to full decompiling Android application with reverse engineering of source code and .smali files
def install_android_decompiler_jadx():
    
    try:
        result = subprocess.run(['jadx', '--version'], capture_output=True, text=True)
        if result.returncode == 0 and 'jadx' in result.stdout:
            print("Jadx is already installed")
        else:
            print("=== Installing Jadx ===")
            subprocess.run(["git", "clone", "https://github.com/skylot/jadx.git"])
            subprocess.run(['cd', 'jadx', '&&', './gradlew', 'dist'])
    except FileNotFoundError as error:
            print(error)


# Tool to quick decompiling Android application with reverse engineering of .smali files
def install_android_decompiler_apktools():
    
    apktool_absolute_path = '/usr/local/bin/apktool.jar'
    
    if not os.path.exists(apktool_absolute_path):
        print("=== Installing ApkTools ===")
        subprocess.run(['sudo', 'apt', 'install', 'apktool', '-y'])
        

# Tool to download Android application from Google Play
def install_apkeep():
    
    apkeep_absolute_path = '$HOME/cargo/bin/apkeep'

    if not os.path.exists(apkeep_absolute_path):
        print("=== Installing Apkeep ===")
        subprocess.run(['sudo', 'apt', 'install', 'libssl-dev', '-y'])
        subprocess.run(['sudo', 'apt', 'install', 'pkg-config', '-y'])
        subprocess.run(['sudo', 'apt', 'install', 'cargo', '-y'])
        subprocess.run(['sudo', 'cargo', 'install', 'apkeep', '--locked'])


# Tool to using AWS Console
def install_aws_cli():

    aws_cli_absolute_path='/usr/bin/aws'

    if not os.path.exists(aws_cli_absolute_path):
        print("=== Installing AwsCli ===")
        subprocess.run(['sudo', 'apt', 'install', 'awscli', '-y'])


def install_third_party_software():
    
    install_android_decompiler_jadx()
    install_android_decompiler_apktools()
    install_apkeep()
    install_aws_cli()