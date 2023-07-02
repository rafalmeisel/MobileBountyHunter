import subprocess
import distro
from source_code.config_file_manager import get_autoinstall_third_party_software

def is_installed_awscli():
    is_installed_awscli = False
    
    try:
        subprocess.check_output(["which", "aws"])
        is_installed_awscli = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        is_installed_awscli = False
    
    return is_installed_awscli


def show_installation_process_aws_cli():
    distribution = distro.id()

    if (distribution == "kali" or distribution =="debian" or distribution =="linuxmint"):
        print("Please install awscli using command: apt install awscli")
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def install_awscli():
    distribution = distro.id()

    print("=== Installing AwsCli ===")
    if (distribution == "kali" or distribution =="debian" or distribution =="linuxmint"):
        subprocess.run('apt install awscli -y', shell=True, check=True)
    else:
        print("You're using " + distribution + " system. It suprised us that you are using this system. Please, let us know about adding this system to the script ;)")

def run_install_process_aws_cli():
    
    is_autoinstall_third_party_software = get_autoinstall_third_party_software()

    if not (is_installed_awscli()):
        if (is_autoinstall_third_party_software):
            install_awscli()
        else:
            show_installation_process_aws_cli()
    
    if not (is_installed_awscli()):
        exit()