from source_code.third_party_software.apkeep import run_install_process_apkeep
from source_code.third_party_software.apktool import run_install_process_android_decompiler_apktool
from source_code.third_party_software.awscli import run_install_process_aws_cli
from source_code.third_party_software.jadx import run_install_process_android_decompiler_jadx

def install_third_party_software():

    run_install_process_apkeep()
    run_install_process_android_decompiler_apktool()
    run_install_process_aws_cli()
    run_install_process_android_decompiler_jadx()