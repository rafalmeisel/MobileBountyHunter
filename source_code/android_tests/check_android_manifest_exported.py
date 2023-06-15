# These 2 lines are needed to perform Unit Tests.
import sys
sys.path.append('./')

from source_code.report_manager import report_issue
from source_code.report_manager import IssueSeverity
from source_code.report_manager import IssueStatus

# <application android:name="application_name" android:exported="true">
# <activity android:name="activity_name" android:exported="true">
# <service android:name="service_name" android:exported="true">
# <service android:exported="true">

def check_android_manifest_exported(android_manifest_xml_root):
    
    token_name = 'exported'

    exported_items_list = []

    for element in android_manifest_xml_root.iter():
        for key, value in element.attrib.items():

            if token_name in key and value == 'true':
                element_type = element.tag.split('}')[-1]
                element_name = None
            
                for attr_key, attr_value in element.attrib.items():
                    if attr_key.endswith('name'):
                        element_name = attr_value
                        break
                
                element_full_name = ""
                if element_name is None:
                    element_full_name = element_type
                else:
                    element_full_name = element_type + ": " + element_name
                
                exported_items_list.append(element_full_name)

    return exported_items_list


def run_check_android_manifest_exported(application_package_system, application_package_name, file_name, xml_file_content):

    allow_backup_items_list = check_android_manifest_exported(xml_file_content)
    
    if len(allow_backup_items_list) > 0:
        for allow_backup_item in allow_backup_items_list:
            report_issue(application_package_system, application_package_name, file_name, IssueSeverity.LOW, IssueStatus.TO_VERIFY, "exported", allow_backup_item)
    else:
        report_issue(application_package_system, application_package_name, file_name, IssueSeverity.INFORMATIVE, IssueStatus.NOT_FOUND, "exported", "")