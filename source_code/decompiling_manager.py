import os
import subprocess
import source_code.config_file_manager
import zipfile
import pathlib
import shutil

# Decompiling only Google Store applications with JADX
def decompile_apk_with_jadx(application_package_name):
    
    print("Decompiling: " + application_package_name + " with JADX.")

    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
    input_application_package_absolute_path = os.path.abspath(pathlib.Path(input_directory_relative_path, application_package_name))

    output_directory_relative_path = source_code.config_file_manager.get_android_output_directory_relative_path()
    output_application_package_absolute_path = os.path.abspath(pathlib.Path(output_directory_relative_path, application_package_name))

    subprocess.run(['jadx', input_application_package_absolute_path,'-d', output_application_package_absolute_path])


# Decompiling only Google Store applications with ApkTools
def decompile_apk_with_apk_tools(application_package_name):
    
    print("Decompiling: " + application_package_name + " with ApkTools.")

    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
    input_application_package_absolute_path = os.path.abspath(pathlib.Path(input_directory_relative_path, application_package_name))

    output_directory_relative_path = source_code.config_file_manager.get_android_output_directory_relative_path()
    output_application_package_absolute_path = os.path.abspath(pathlib.Path(output_directory_relative_path, application_package_name))

    os.system("apktool d " + input_application_package_absolute_path + " -o " + output_application_package_absolute_path + " -f --quiet")


# Decompiling only Google Store applications with Jadx
def decompile_xapk_with_jadx(application_package_name):
    
    if (is_valid_xapk(application_package_name)):

        xapk_application_package_name = application_package_name        
        apk_application_package_name = application_package_name.replace(".xapk", ".apk")

        unzip_xapk(xapk_application_package_name)
        move_apk_from_temporary_to_input_directory(apk_application_package_name)

        print("Decompiling: " + application_package_name + " with JADX.")

        input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
        input_application_package_absolute_path = os.path.abspath(pathlib.Path(input_directory_relative_path, apk_application_package_name))

        output_directory_relative_path = source_code.config_file_manager.get_android_output_directory_relative_path()
        output_application_package_absolute_path = os.path.abspath(pathlib.Path(output_directory_relative_path, apk_application_package_name))

        subprocess.run(['jadx', input_application_package_absolute_path, '-d', output_application_package_absolute_path])
        remove_unzip_apk_temporary_directory(apk_application_package_name)


# Decompiling only Google Store applications with ApkTools
def decompile_xapk_with_apk_tools(application_package_name):

    if (is_valid_xapk(application_package_name)):

        xapk_application_package_name = application_package_name        
        apk_application_package_name = application_package_name.replace(".xapk", ".apk")

        unzip_xapk(xapk_application_package_name)
        move_apk_from_temporary_to_input_directory(apk_application_package_name)

        print("Decompiling: " + application_package_name + " with ApkTools.")

        input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
        input_application_package_absolute_path = os.path.abspath(pathlib.Path(input_directory_relative_path, apk_application_package_name))

        output_directory_relative_path = source_code.config_file_manager.get_android_output_directory_relative_path()
        output_application_package_absolute_path = os.path.abspath(pathlib.Path(output_directory_relative_path, apk_application_package_name))

        os.system("apktool d " + input_application_package_absolute_path + " -o " + output_application_package_absolute_path + " -f --quiet")

        remove_unzip_apk_temporary_directory(apk_application_package_name)


def use_apk_tools(decompiling_tool):
    if decompiling_tool == "apktool":
        return True
    else:
        return False


def use_jadx(decompiling_tool):
    if decompiling_tool == "jadx":
        return True
    else:
        return False
    

def is_xapk(application_package_name):
    if ".xapk" in application_package_name:
        return True
    else:
        return False


def is_apk(application_package_name):
    if ".apk" in application_package_name:
        return True
    else:
        return False
    

def is_valid_xapk(application_package_name):

    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path
    input_application_package_absolute_path = os.path.abspath(input_directory_relative_path, application_package_name)

    if zipfile.is_zipfile(input_application_package_absolute_path):
        print("Application: " + application_package_name + " is a valid file.")
        return True
    else:
        print("Application: " + application_package_name + " is not a valid file (corrupted).")
        return False


def unzip_xapk(application_package_name):
    
    print("Unzipping Xapk file : " + application_package_name)

    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path
    input_xapk_application_package_absolute_path = str(os.path.abspath(input_directory_relative_path, application_package_name))
    input_xapk_temporary_directory_absolute_path = str(os.path.abspath(input_directory_relative_path, "xapk_temporary"))

    with zipfile.ZipFile(input_xapk_application_package_absolute_path, "r") as zip_ref:
            zip_ref.extractall(input_xapk_temporary_directory_absolute_path)


def remove_unzip_apk_temporary_directory(application_package_name):

    print("Remove temporary directory : " + application_package_name)
    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path
    input_xapk_temporary_directory_absolute_path = str(os.path.abspath(input_directory_relative_path, "xapk_temporary"))
    
    if os.path.isdir(input_xapk_temporary_directory_absolute_path):
        shutil.rmtree(input_xapk_temporary_directory_absolute_path)


def move_apk_from_temporary_to_input_directory(apk_application_package_name):

    print("Move apk from temporary directory to Input directory : " + apk_application_package_name)
    input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path
    input_xapk_temporary_directory_absolute_path = str(os.path.abspath(input_directory_relative_path, "xapk_temporary"))
    input_apk_temporary_directory_absolute_path = str(os.path.abspath(input_xapk_temporary_directory_absolute_path, apk_application_package_name))
    input_apk_application_package_name_absolute_path = str(os.path.abspath(input_directory_relative_path, apk_application_package_name))

    if os.path.isfile(input_apk_temporary_directory_absolute_path):
        shutil.move(input_apk_temporary_directory_absolute_path, input_apk_application_package_name_absolute_path)
    

def decompile_android_application(application_package_name, decompiling_tool):
    
    if (is_apk(application_package_name) and use_apk_tools(decompiling_tool)):
        decompile_apk_with_apk_tools(application_package_name)
    elif (is_apk(application_package_name) and use_jadx(decompiling_tool)):
        decompile_apk_with_jadx(application_package_name)
    elif (is_xapk(application_package_name) and use_apk_tools(decompiling_tool)):
        decompile_xapk_with_apk_tools(application_package_name)
    elif (is_xapk(application_package_name) and use_jadx(decompiling_tool)):
        decompile_xapk_with_jadx(application_package_name)


# def decompile_android_input_directory():

#     input_directory_relative_path = source_code.config_file_manager.get_android_input_directory_relative_path()
#     decompiling_tool = source_code.config_file_manager.get_android_decompiling_tool()

#     for application_package_name in os.listdir(input_directory_relative_path):
#         decompile_android_application(application_package_name, decompiling_tool)


def decompile_ios_application(application_package_name, decompiling_tool):

    print("iOS is not supported yet :(")


def decompile_ios_input_directory():

    print("iOS is not supported yet :(")