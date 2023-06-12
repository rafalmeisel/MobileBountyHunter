import xml.etree.ElementTree as ElementTree
import unittest

import importlib.util
from lxml import etree

module_path = 'source_code/android_tests/check_android_manifest_exported.py'

spec = importlib.util.spec_from_file_location('check_android_manifest_exported', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_android_manifest_exported = module.check_android_manifest_exported

class TestCheckAndroidManifestExported(unittest.TestCase):   

    def setUp(self):
        self.android_manifest_xml = '''
            <manifest xmlns:android="http://schemas.android.com/apk/res/android"
                package="com.example.myapp">

                <application
                    android:name="com.example.myapp.MyApplication.ApplicationTestExported"
                    android:exported="true"
                    android:icon="@mipmap/ic_launcher"
                    android:label="@string/app_name"
                    android:roundIcon="@mipmap/ic_launcher_round"
                    android:supportsRtl="true"
                    android:theme="@style/AppTheme">

                    <activity
                        android:name="com.example.myapp.MyApplication.ActivityTestExported"
                        android:exported="true"
                        android:label="@string/app_name">
                    </activity>

                    <service
                        android:name="com.example.myapp.MyApplication.ServiceTestExported"
                        android:exported="true">
                    </service> 
                
                </application>

            </manifest>
        '''

    def test_check_android_manifest_exported(self):
        root = etree.fromstring(self.android_manifest_xml)
        result = check_android_manifest_exported(root)
        expected = [
            'exported: application: com.example.myapp.MyApplication.ApplicationTestExported',
            'exported: activity: com.example.myapp.MyApplication.ActivityTestExported',
            'exported: service: com.example.myapp.MyApplication.ServiceTestExported'
        ]
        self.assertEqual(result, expected)

    def test_check_android_manifest_Exported_no_elements(self):
        root = etree.Element('manifest')
        result = check_android_manifest_exported(root)
        expected = []
        self.assertEqual(result, expected)

    def test_check_android_manifest_Exported_no_Exported_elements(self):
        self.android_manifest_xml = '''
        <manifest xmlns:android="http://schemas.android.com/apk/res/android"
            package="com.example.myapp">
            <application>
                <activity android:name=".MainActivity" />
                <activity android:name=".OtherActivity" />
                <service android:name=".MyService" />
                <provider android:name=".MyProvider" />
            </application>
        </manifest>
        '''
        root = etree.fromstring(self.android_manifest_xml)
        result = check_android_manifest_exported(root)
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()