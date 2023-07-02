import subprocess
import distro
from source_code.config_file_manager import get_autoinstall_third_party_software

def is_installed_jadx():
    is_installed_jadx = False

    try:
        subprocess.check_output(["which", "jadx"])
        is_installed_jadx = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        is_installed_jadx = False

    return is_installed_jadx

def show_installation_process_android_decompiler_jadx():
    distribution = distro.id()

    if (distribution == "kali" or distribution =="debian"):
        print("Please install jadx using command: apt install jadx")
    elif (distribution == "linuxmint"):
        print("Please install jadx using command: flatpak install flathub com.github.skylot.jadx")
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def install_android_decompiler_jadx():
    distribution = distro.id()

    print("=== Installing Jadx ===")
    if (distribution == "kali" or distribution =="debian"):
        subprocess.run('apt install jadx', shell=True, check=True)
    elif (distribution == "linuxmint"):
        subprocess.run('flatpak install flathub com.github.skylot.jadx', shell=True, check=True)
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def run_install_process_android_decompiler_jadx():
    
    is_installed_jadx = is_installed_jadx()
    is_autoinstall_third_party_software = get_autoinstall_third_party_software()

    if not (is_installed_jadx):
        if (is_autoinstall_third_party_software):
            install_android_decompiler_jadx()
        else:
            show_installation_process_android_decompiler_jadx()