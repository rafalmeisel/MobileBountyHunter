import subprocess
import distro
import getpass
import os
from source_code.config_file_manager import get_autoinstall_third_party_software

def is_installed_apkeep():
    
    try:
        subprocess.check_output(["which", "apkeep"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        apkeep_file_path = '/home/' + getpass.getuser() + '/.cargo/bin/apkeep'
    
        if os.path.exists(apkeep_file_path):
            return True
        else:
            return False

def show_installation_process_android_decompiler_apkeep():
    
    distribution = distro.id()

    if (distribution == "kali" or distribution =="debian" or distribution == "linuxmint"):
        print('Please install apkeep using commands:')
        print('apt install libssl-dev -y')
        print('apt install pkg-config -y')
        print('apt install cargo -y')
        print('cargo install apkeep --locked')
        print('export PATH="$PATH:/home/' + getpass.getuser() + '/.cargo/bin"')

    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def install_android_apkeep():
    
    distribution = distro.id()

    print("=== Installing Apkeep ===")
    if (distribution == "kali" or distribution =="debian" or distribution == "linuxmint"):
        subprocess.run('apt install libssl-dev -y', shell=True, check=True)
        subprocess.run('apt install pkg-config -y', shell=True, check=True)
        subprocess.run('apt install cargo -y', shell=True, check=True)
        subprocess.run('cargo install apkeep --locked', shell=True, check=True)
        subprocess.run('export PATH=$PATH:/home/' + getpass.getuser() + '/.cargo/bin', shell=True, check=True)

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