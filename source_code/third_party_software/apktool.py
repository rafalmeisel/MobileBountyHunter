import subprocess
import distro
from source_code.config_file_manager import get_autoinstall_third_party_software

def is_installed_apktool():
    is_installed_apktool = False

    try:
        subprocess.check_output(["which", "apktool"])
        is_installed_apktool = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        is_installed_apktool = False

    return is_installed_apktool

def show_installation_process_android_decompiler_apktool():

    distribution = distro.id()

    if (distribution == "kali" or distribution =="debian"):
        print("Please install apktool using command: apt install apktool")
    elif (distribution == "linuxmint"):
        print("Please install apktool using command: apt install apktool")
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def install_android_decompiler_apktool():
  
    distribution = distro.id()

    print("=== Installing Apktool ===")
    if (distribution == "kali" or distribution =="debian"):
        subprocess.run('apt install apktool -y', shell=True, check=True)
    elif (distribution == "linuxmint"):
        subprocess.run('apt install apktool -y', shell=True, check=True)
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def run_install_process_android_decompiler_apktool():
    
    is_autoinstall_third_party_software = get_autoinstall_third_party_software()

    if not (is_installed_apktool()):
        if (is_autoinstall_third_party_software):
            install_android_decompiler_apktool()
        else:
            show_installation_process_android_decompiler_apktool()

    if not(is_installed_apktool()):
        exit()