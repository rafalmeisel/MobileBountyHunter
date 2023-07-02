import subprocess
import distro
import os
from source_code.config_file_manager import get_autoinstall_third_party_software

def is_installed_apkeep():
    is_installed_apkeep = False

    try:
        subprocess.check_output(["which", "apkeep"])
        is_installed_apkeep = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        is_installed_apkeep = False

    return is_installed_apkeep

def show_installation_process_android_decompiler_apkeep():
    
    distribution = distro.id()

    if (distribution == "kali" or distribution =="debian" or distribution == "linuxmint"):
        print("Please install apkeep using commands:")
        print("sudo apt install libssl-dev -y")
        print("sudo apt install pkg-config -y")
        print("sudo apt install cargo -y")
        print("sudo cargo install apkeep --locked")
        print("export PATH=$PATH:/root/.cargo/bin")

    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def install_android_apkeep():
    
    distribution = distro.id()

    print("=== Installing Apkeep ===")
    if (distribution == "kali" or distribution =="debian" or distribution == "linuxmint"):
        subprocess.run('sudo apt install libssl-dev -y', shell=True, check=True)
        subprocess.run('sudo apt install pkg-config -y', shell=True, check=True)
        subprocess.run('sudo apt install cargo -y', shell=True, check=True)
        subprocess.run('sudo cargo install apkeep --locked', shell=True, check=True)


        path = os.environ.get('PATH', '')
        new_path = '/root/.cargo/bin:' + path
        os.environ['PATH'] = new_path

    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")


def run_install_process_apkeep():
    
    is_autoinstall_third_party_software = get_autoinstall_third_party_software()

    if not (is_installed_apkeep()):
        if (is_autoinstall_third_party_software):
            install_android_apkeep()
        else:
            show_installation_process_android_decompiler_apkeep()
    
    if not (is_installed_apkeep()):
        exit()