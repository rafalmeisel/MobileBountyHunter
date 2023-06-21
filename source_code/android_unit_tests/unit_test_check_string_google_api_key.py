import unittest
import importlib.util

test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_string_google_api_key.py'

spec = importlib.util.spec_from_file_location('check_string_google_api_key', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_string_google_api_key = module.check_string_google_api_key

class TestCheckStringCloudinary(unittest.TestCase):

    def setUp(self):
        self.content_file = '''
           <?xml version="1.0" encoding="utf-8"?>
            <resources>
                <string name="app_name">My App</string>
                <string name="hello">Hello</string>
                <string name="description">This is a sample description.</string>
                <string name="button_ok">OK</string>
                <string name="button_cancel">Cancel</string>
                <string name="error">Error</string>
                <string name="success">Success</string>
                <string name="warning">Warning</string>
                <string name="info">Info</string>
                <string name="welcome">Welcome to our app!</string>
                <string name="username">Username</string>
                <string name="password">Password</string>
                <string name="email">Email</string>
                <string name="phone">Phone</string>
                <string name="address">Address</string>
                <string name="city">City</string>
                <string name="country">Country</string>
                <string name="zipcode">Zip Code</string>
                <string name="submit">Submit</string>
                <string name="cancel">Cancel</string>
                <string name="loading">Loading...</string>
                <string name="success_message">Operation completed successfully.</string>
                <string name="error_message">An error occurred.</string>
                <string name="welcome_message">Welcome to our app, %1$s!</string>
                <string name="page">Page %1$d</string>
                <string name="remaining_attempts">Remaining attempts: %1$d</string>
                <string name="google_api_key">AIzaSyCmD-JJN2Hx2kEa5j8d4VUZ6Z4_qBXYZ13</string>
            </resources>
        '''


    def test_check_string_google_api_key(self):
        result = check_string_google_api_key(self.content_file)
        expected = [
            'AIzaSyCmD-JJN2Hx2kEa5j8d4VUZ6Z4_qBXYZ13',
        ]
        self.assertEqual(result, expected)


    def test_check_string_google_api_key_empty_file(self):
        self.content_file = ""
        result = check_string_google_api_key(self.content_file)
        expected = []
        self.assertEqual(result, expected)


    def test_check_string_google_api_key_without_elements(self):
        self.content_file = '''
        <?xml version="1.0" encoding="utf-8"?>
            <resources>
                <string name="app_name">My App</string>
                <string name="hello">Hello</string>
                <string name="description">This is a sample description.</string>
                <string name="button_ok">OK</string>
                <string name="button_cancel">Cancel</string>
                <string name="error">Error</string>
                <string name="success">Success</string>
                <string name="warning">Warning</string>
            </resources>
        '''
        result = check_string_google_api_key(self.content_file)
        expected = []
        self.assertEqual(result, expected)

    def test_check_string_google_api_key_many_values(self):
        self.content_file = '''
        <?xml version="1.0" encoding="utf-8"?>
            <resources>
                <string name="app_name">My App</string>
                <string name="hello">Hello</string>
                <string name="description">This is a sample description.</string>
                <string name="button_ok">OK</string>
                <string name="button_cancel">Cancel</string>
                <string name="error">Error</string>
                <string name="success">Success</string>
                <string name="warning">Warning</string>
                <string name="google_api_key">AIzaSyCmD-JJN2Hx2kEa5j8d4VUZ6Z4_qBXYZ13</string>
                <string name="google_api_key">AIzaSyDLRbfN8EiAMjcfsXuvE_CKfSlZ3E17xyz</string>
                <string name="google_api_key">AIzaSyDLR_asd8EiAMjcfsXuvE_CKfSl12317xy</string>
            </resources>
        '''
        result = check_string_google_api_key(self.content_file)
        expected = [
            'AIzaSyCmD-JJN2Hx2kEa5j8d4VUZ6Z4_qBXYZ13',
            'AIzaSyDLRbfN8EiAMjcfsXuvE_CKfSlZ3E17xyz',
            'AIzaSyDLR_asd8EiAMjcfsXuvE_CKfSl12317xy'
        ]
        self.assertEqual(result, expected)

    def test_check_string_google_api_key_wrong_value_wrong_prefix(self):
        self.content_file = '''
        <?xml version="1.0" encoding="utf-8"?>
            <resources>
                <string name="app_name">My App</string>
                <string name="hello">Hello</string>
                <string name="description">This is a sample description.</string>
                <string name="button_ok">OK</string>
                <string name="button_cancel">Cancel</string>
                <string name="error">Error</string>
                <string name="success">Success</string>
                <string name="warning">Warning</string>
                <string name="google_api_key">ALzaSyCmD-JJN2Hx2kEa5j8d4VUZ6Z4_qBXYZ13</string>
            </resources>
        '''
        result = check_string_google_api_key(self.content_file)
        expected = []
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()