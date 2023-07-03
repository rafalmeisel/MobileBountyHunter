import subprocess
import distro
import requests
import os
import getpass
import json
from source_code.config_file_manager import get_autoinstall_third_party_software

def is_installed_jadx():
    
    try:
        subprocess.check_output(["which", "jadx"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        jadx_file_path = '/usr/jadx/bin/jadx'
    
        if os.path.exists(jadx_file_path):
            return True
        else:
            return False

def show_installation_process_android_decompiler_jadx():
    distribution = distro.id()

    if (distribution == "kali" or distribution =="debian"):
        print("Please install jadx using command: apt install jadx")
    elif (distribution == "linuxmint"):

        # Fetching the latest version of JADX
        api_url = "https://api.github.com/repos/skylot/jadx/releases/latest"
        response = requests.get(api_url)
        data = json.loads(response.text)
        
        # example: "tag_name": "v1.4.7",
        jadx_repository_tag_name = data["tag_name"]
        # example: "name": "1.4.7",
        jadx_repository_name = data["name"]

        # example: https://github.com/skylot/jadx/releases/download/v1.4.7/jadx-1.4.7.zip
        # Downloading JADX zip file
        jadx_url = f"https://github.com/skylot/jadx/releases/download/{jadx_repository_tag_name}/jadx-{jadx_repository_name}.zip"
        print("Download file as 'jadx.zip': " + jadx_url)
        
        # Extracting JADX zip file
        print("Unzip file: unzip jadx.zip -d jadx-tem")
        
        # Moving JADX binaries and libraries to /usr/jadx
        print("Move JADX binaries and libraries to /usr/jadx:")
        print("mkdir -p /usr/jadx/bin")
        print("mv jadx-temp/bin/jadx /usr/jadx/bin")
        print("mv jadx-temp/bin/jadx-gui /usr/jadx/bin")
        print("mv jadx-temp/lib /usr/jadx")

        # Adding JADX to the system PATH
        print("Update $PATH")
        print("export PATH=$PATH:/usr/jadx/bin | sudo tee -a /etc/profile")
        print("source /etc/profile")
        
        # Remove jadx.zip
        print("rm jadx.zip")
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def install_android_decompiler_jadx():
    distribution = distro.id()

    print("=== Installing Jadx ===")
    if (distribution == "kali" or distribution =="debian"):
        subprocess.run('apt install jadx -y', shell=True, check=True)
    elif (distribution == "linuxmint"):

        # Fetching the latest version of JADX
        api_url = "https://api.github.com/repos/skylot/jadx/releases/latest"
        response = requests.get(api_url)
        data = json.loads(response.text)
        
        # example: "tag_name": "v1.4.7",
        jadx_repository_tag_name = data["tag_name"]
        # example: "name": "1.4.7",
        jadx_repository_name = data["name"]

        # example: https://github.com/skylot/jadx/releases/download/v1.4.7/jadx-1.4.7.zip
        # Downloading JADX zip file
        jadx_url = f"https://github.com/skylot/jadx/releases/download/{jadx_repository_tag_name}/jadx-{jadx_repository_name}.zip"
        subprocess.run(['curl', '-Lo', 'jadx.zip', jadx_url])

        # Extracting JADX zip file
        subprocess.run(['unzip', 'jadx.zip', '-d', 'jadx-temp'])

        # Moving JADX binaries and libraries to /opt/jadx
        subprocess.run(['mkdir', '-p', '/usr/jadx/bin'], check=True)
        subprocess.run(['mv', 'jadx-temp/bin/jadx', '/usr/jadx/bin'], check=True)
        subprocess.run(['mv', 'jadx-temp/bin/jadx-gui', '/usr/jadx/bin'], check=True)
        subprocess.run(['mv', 'jadx-temp/lib', '/usr/jadx'], check=True)

        # Adding JADX to the system PATH
        os.environ['PATH'] += ':/opt/jadx/bin'

        # Remove jadx.zip
        subprocess.run(['rm', 'jadx.zip'], check=True)
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")


def run_install_process_android_decompiler_jadx():
    
    is_autoinstall_third_party_software = get_autoinstall_third_party_software()

    if not (is_installed_jadx()):
        if (is_autoinstall_third_party_software):
            install_android_decompiler_jadx()
        else:
            show_installation_process_android_decompiler_jadx()

    if not (is_installed_jadx()):
        exit()