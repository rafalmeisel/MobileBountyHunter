import xml.etree.ElementTree as ElementTree
import unittest

import importlib.util
from lxml import etree

from termcolor import colored
test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_android_manifest_debuggable.py'

spec = importlib.util.spec_from_file_location('check_android_manifest_debuggable', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_android_manifest_debuggable = module.check_android_manifest_debuggable

class TestCheckAndroidManifestDebuggable(unittest.TestCase):   

    def setUp(self):
        self.android_manifest_xml = '''
            <manifest xmlns:android="http://schemas.android.com/apk/res/android"
                package="com.example.myapp">

                <application
                    android:name="com.example.myapp.MyApplication.ApplicationTestDebuggable"
                    android:debuggable="true"
                    android:icon="@mipmap/ic_launcher"
                    android:label="@string/app_name"
                    android:roundIcon="@mipmap/ic_launcher_round"
                    android:supportsRtl="true"
                    android:theme="@style/AppTheme">

                    <activity
                        android:name="com.example.myapp.MyApplication.ActivityTestDebuggable"
                        android:debuggable="true"
                        android:label="@string/app_name">
                    </activity>

                    <service
                        android:name="com.example.myapp.MyApplication.ServiceTestDebuggable"
                        android:debuggable="true">
                    </service> 
                
                </application>

            </manifest>
        '''

    def test_check_android_manifest_debuggable(self):
        root = etree.fromstring(self.android_manifest_xml)
        result = check_android_manifest_debuggable(root)
        expected = [
            'application: com.example.myapp.MyApplication.ApplicationTestDebuggable',
            'activity: com.example.myapp.MyApplication.ActivityTestDebuggable',
            'service: com.example.myapp.MyApplication.ServiceTestDebuggable'
        ]
        self.assertEqual(result, expected)

        
    def test_check_android_manifest_debuggable_no_elements(self):
        root = etree.Element('manifest')
        result = check_android_manifest_debuggable(root)
        expected = []
        self.assertEqual(result, expected)


    def test_check_android_manifest_debuggable_no_debuggable_elements(self):
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
        result = check_android_manifest_debuggable(root)
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()