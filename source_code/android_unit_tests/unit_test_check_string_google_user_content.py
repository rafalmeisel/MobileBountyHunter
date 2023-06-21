import unittest
import importlib.util

test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_string_google_user_content.py'

spec = importlib.util.spec_from_file_location('check_string_google_user_content', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_string_google_user_content = module.check_string_google_user_content

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
                <string name="google_user_content">1234567890.apps.googleusercontent.com</string>
            </resources>
        '''


    def test_check_string_google_user_content(self):
        result = check_string_google_user_content(self.content_file)
        expected = [
            '1234567890.apps.googleusercontent.com',
        ]
        self.assertEqual(result, expected)


    def test_check_string_google_user_content_empty_file(self):
        self.content_file = ""
        result = check_string_google_user_content(self.content_file)
        expected = []
        self.assertEqual(result, expected)


    def test_check_string_google_user_content_without_elements(self):
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
        result = check_string_google_user_content(self.content_file)
        expected = []
        self.assertEqual(result, expected)

    def test_check_string_google_user_content_many_values(self):
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
                <string name="google_user_content">google_use1234567890.apps.googleusercontent.com</string>
                <string name="google_user_content">1234567890-abc123def456.apps.googleusercontent.com</string>
                <string name="google_user_content">example.apps.googleusercontent.com</string>
            </resources>
        '''
        result = check_string_google_user_content(self.content_file)
        expected = [
            'google_use1234567890.apps.googleusercontent.com',
            '1234567890-abc123def456.apps.googleusercontent.com',
            'example.apps.googleusercontent.com'
        ]
        self.assertEqual(result, expected)

    def test_check_string_google_user_content_wrong_value_wrong_prefix(self):
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
                <string name="google_user_content">1234567890.apps.googleusercontenta.com</string>
            </resources>
        '''
        result = check_string_google_user_content(self.content_file)
        expected = []
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()