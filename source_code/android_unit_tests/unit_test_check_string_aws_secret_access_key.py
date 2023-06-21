import unittest
import importlib.util

test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_string_aws_secret_access_key.py'

spec = importlib.util.spec_from_file_location('check_string_aws_secret_access_key', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_string_aws_secret_access_key = module.check_string_aws_secret_access_key

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
                <string name="aws_secret_access_key">wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY</string>
            </resources>
        '''


    def test_check_string_aws_secret_access_key(self):
        result = check_string_aws_secret_access_key(self.content_file)
        expected = [
            'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
        ]
        self.assertEqual(result, expected)


    def test_check_string_aws_secret_access_key_empty_file(self):
        self.content_file = ""
        result = check_string_aws_secret_access_key(self.content_file)
        expected = []
        self.assertEqual(result, expected)


    def test_check_string_aws_secret_access_key_without_elements(self):
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
        result = check_string_aws_secret_access_key(self.content_file)
        expected = []
        self.assertEqual(result, expected)

    def test_check_string_aws_secret_access_key_many_values(self):
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
                <string name="aws_secret_access_key">wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY</string>
                <string name="aws_secret_access_key">wJalrXJHKAjasd/asda/AKJNSKJDNKA/12312/as</string>
                <string name="aws_secret_access_key">aska8912NKJASDnjk/1231/a9sdj1/3AJNKSJDaD</string>
            </resources>
        '''
        result = check_string_aws_secret_access_key(self.content_file)
        expected = [
            'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
            'wJalrXJHKAjasd/asda/AKJNSKJDNKA/12312/as',
            'aska8912NKJASDnjk/1231/a9sdj1/3AJNKSJDaD'
        ]
        self.assertEqual(result, expected)

    def test_check_string_aws_secret_access_key_wrong_value_too_short(self):
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
                <string name="aws_secret_access_key">wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPL</string>
            </resources>
        '''
        result = check_string_aws_secret_access_key(self.content_file)
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()