import subprocess
import distro
import getpass
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
    if (distribution == "kali" or distribution =="debian"):
        subprocess.run('apt install libssl-dev -y', shell=True, check=True)
        subprocess.run('apt install pkg-config -y', shell=True, check=True)
        subprocess.run('apt install cargo -y', shell=True, check=True)
        subprocess.run('cargo install apkeep --locked', shell=True, check=True)
        subprocess.run('export PATH=$PATH:/home/' + getpass.getuser() + '/.cargo/bin', shell=True, check=True)

    elif (distribution == "linuxmint"):
        subprocess.run('flatpak install flathub com.github.skylot.jadx', shell=True, check=True)

    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")


def is_apkeep_installed_not_added_to_path():
    is_apkeep_installed = os.path.isfile('/home/' + getpass.getuser() + '/.cargo/bin/apkeep')

    if(is_apkeep_installed):
        return True
    else:
        return False

# TODO: It seems to not work on Linux Mint. Cargo/bin path cannot be permamently saved.
def add_apkeep_to_path():
    os.environ['PATH'] += ':/home/' + getpass.getuser() + '/.cargo/bin'

def check_apkeep_and_update_path():
    
    is_apkeep_installed = os.path.isfile('/home/' + getpass.getuser() + '/.cargo/bin/apkeep')
    if (is_apkeep_installed):
        subprocess.run('export PATH=$PATH:/home/' + getpass.getuser() + '/.cargo/bin', shell=True, check=True)
    

def run_install_process_apkeep():
    
    is_autoinstall_third_party_software = get_autoinstall_third_party_software()
    
    # In Linux Mint, there is an issue to update $PATH with ./cargo/bin
    # Due to this issue each time, when user run the script, there is check:
    # 1. to verify if apkeep is already installed:
    # a) yes - add /.cargo/bin to $PATH (it works only in current Python session!)
    # b) no - continue script and install apkeep

    if (is_apkeep_installed_not_added_to_path):
        add_apkeep_to_path()
    else:
        if not (is_installed_apkeep()):

            if (is_autoinstall_third_party_software):
                install_android_apkeep()
            else:
                show_installation_process_android_decompiler_apkeep()
        
        if not (is_installed_apkeep()):
            exit()