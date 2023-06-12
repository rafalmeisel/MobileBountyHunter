import xml.etree.ElementTree as ElementTree
import re

# <application android:name="application_name" android:debuggable="true">
# <activity android:name="activity_name" android:debuggable="true">
# <service android:name="service_name" android:debuggable="true">
# <service android:debuggable="true">

def check_android_manifest_debuggable(android_manifest_xml_root):
    
    attribute_name = 'debuggable'

    debuggable_items_list = []

    for element in android_manifest_xml_root.iter():
        for key, value in element.attrib.items():

            if attribute_name in key and value == 'true':
                element_type = element.tag.split('}')[-1]
                element_name = None
            
                for attr_key, attr_value in element.attrib.items():
                    if attr_key.endswith('name'):
                        element_name = attr_value
                        break
                
                if element_name is None:
                    element_full_name = f"{attribute_name}: {element_type}"
                else:
                    element_full_name = f"{attribute_name}: {element_type}: {element_name}"
                
                debuggable_items_list.append(element_full_name)

    return debuggable_items_list