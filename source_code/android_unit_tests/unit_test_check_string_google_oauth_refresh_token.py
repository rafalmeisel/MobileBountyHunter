import unittest
import importlib.util

test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_string_google_oauth_refresh_token.py'

spec = importlib.util.spec_from_file_location('check_string_google_oauth_refresh_token', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_string_google_oauth_refresh_token = module.check_string_google_oauth_refresh_token

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
                <string name="google_oauth_refresh_token">1//0gd2xhT4mpKx-CgYIARAAGBASNwF-L9IrrYekXHq_dI5g7A4a4z6ZX0eRvzYg-9Zbo2bkRr3LiN0DlwS8gJ-Rg7zWK_TFlbOcNu8</string>
            </resources>
        '''


    def test_check_string_google_oauth_refresh_token(self):
        result = check_string_google_oauth_refresh_token(self.content_file)
        expected = [
            '1//0gd2xhT4mpKx-CgYIARAAGBASNwF-L9IrrYekXHq_dI5g7A4a4z6ZX0eRvzYg-9Zbo2bkRr3LiN0DlwS8gJ-Rg7zWK_TFlbOcNu8',
        ]
        self.assertEqual(result, expected)


    def test_check_string_google_oauth_refresh_token_empty_file(self):
        self.content_file = ""
        result = check_string_google_oauth_refresh_token(self.content_file)
        expected = []
        self.assertEqual(result, expected)


    def test_check_string_google_oauth_refresh_token_without_elements(self):
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
        result = check_string_google_oauth_refresh_token(self.content_file)
        expected = []
        self.assertEqual(result, expected)

    def test_check_string_google_oauth_refresh_token_many_values(self):
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
                <string name="google_oauth_refresh_token">1//0gd2xhT4mpKx-CgYIARAAGBASNwF-L9IrrYekXHq_dI5g7A4a4z6ZX0eRvzYg-9Zbo2bkRr3LiN0DlwS8gJ-Rg7zWK_TFlbOcNu8</string>
                <string name="google_oauth_refresh_token">1/Ry68</string>
                <string name="google_oauth_refresh_token">1/KAJSDH91231k23nAJSNDAKj-utsrqpnmolkjihgASJKL12</string>
            </resources>
        '''
        result = check_string_google_oauth_refresh_token(self.content_file)
        expected = [
            '1//0gd2xhT4mpKx-CgYIARAAGBASNwF-L9IrrYekXHq_dI5g7A4a4z6ZX0eRvzYg-9Zbo2bkRr3LiN0DlwS8gJ-Rg7zWK_TFlbOcNu8',
            '1/Ry68',
            '1/KAJSDH91231k23nAJSNDAKj-utsrqpnmolkjihgASJKL12'
        ]
        self.assertEqual(result, expected)

    def test_check_string_google_oauth_refresh_token_wrong_value_wrong_prefix(self):
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
                <string name="google_oauth_refresh_token">2//0gd2xhT4mpKx-CgYIARAAGBASNwF-L9IrrYekXHq_dI5g7A4a4z6ZX0eRvzYg-9Zbo2bkRr3LiN0DlwS8gJ-Rg7zWK_TFlbOcNu8</string>
            </resources>
        '''
        result = check_string_google_oauth_refresh_token(self.content_file)
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()