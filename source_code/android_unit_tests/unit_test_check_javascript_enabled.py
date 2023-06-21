import unittest
import importlib.util
from lxml import etree

test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_string_javascript_enabled.py'

spec = importlib.util.spec_from_file_location('check_string_javascript_enabled', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_string_javascript_enabled = module.check_string_javascript_enabled

class TestCheckAndroidManifestAllowBackup(unittest.TestCase):   

    def setUp(self):
        self.file_content = '''
            public class HelloWebApp extends Activity {
                /** Called when the activity is first created. */
                @Override
                public void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.main);
                    WebView webView = (WebView)findViewById(R.id.webView);
                    webView.getSettings().setJavaScriptEnabled(true);
                    webView.loadUrl("file:///android_asset/www/index.html");
                }
        '''

    def test_smali_check_string_javascript_enabled(self):
        self.file_content = '''
        # Find the WebView instance
        # ...
        # Get the settings of the WebView
        invoke-virtual {v0}, Landroid/webkit/WebView;->getSettings()Landroid/webkit/WebSettings;
        move-result-object v1
        # Enable JavaScript
        const/4 v2, 1
        invoke-virtual {v1, v2}, Landroid/webkit/WebSettings;->setJavaScriptEnabled(Z)V
        '''
        result = check_string_javascript_enabled(self.file_content)
        expected = [
            'setJavaScriptEnabled',
        ]
        self.assertEqual(result, expected)

    def test_java_check_string_javascript_enabled(self):
        self.file_content = '''
            public class HelloWebApp extends Activity {
                /** Called when the activity is first created. */
                @Override
                public void onCreate(Bundle savedInstanceState) {
                    super.onCreate(savedInstanceState);
                    setContentView(R.layout.main);
                    WebView webView = (WebView)findViewById(R.id.webView);
                    webView.getSettings().setJavaScriptEnabled(true);
                    webView.loadUrl("file:///android_asset/www/index.html");
                }
        '''
        result = check_string_javascript_enabled(self.file_content)
        expected = [
            'setJavaScriptEnabled',
        ]
        self.assertEqual(result, expected)

#     def test_check_string_javascript_enabled_no_elements(self):
#         root = etree.Element('manifest')
#         result = check_string_javascript_enabled(root)
#         expected = []
#         self.assertEqual(result, expected)

        
#     def test_check_string_javascript_enabled_no_allow_backup_elements(self):
#         self.file_content = '''
#         <manifest xmlns:android="http://schemas.android.com/apk/res/android"
#             package="com.example.myapp">
#             <application>
#                 <activity android:name=".MainActivity" />
#                 <activity android:name=".OtherActivity" />
#                 <service android:name=".MyService" />
#                 <provider android:name=".MyProvider" />
#             </application>
#         </manifest>
#         '''
#         root = etree.fromstring(self.file_content)
#         result = check_string_javascript_enabled(root)
#         expected = []
#         self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()