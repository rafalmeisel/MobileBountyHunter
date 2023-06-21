import unittest
import importlib.util

test_color_passed = "green"
test_color_failed = "red"

module_path = 'source_code/android_tests/check_string_push_io_application_identifier.py'

spec = importlib.util.spec_from_file_location('check_string_push_io_application_identifier', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
check_string_push_io_application_identifier = module.check_string_push_io_application_identifier

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
                <string name="pushio_application_identifier">pio-ABEgGFd_CNo9NOL_87c6k2GzI</string>
            </resources>
        '''


    def test_check_string_push_io_application_identifier(self):
        result = check_string_push_io_application_identifier(self.content_file)
        expected = [
            'pio-ABEgGFd_CNo9NOL_87c6k2GzI',
        ]
        self.assertEqual(result, expected)


    def test_check_string_push_io_application_identifier_empty_file(self):
        self.content_file = ""
        result = check_string_push_io_application_identifier(self.content_file)
        expected = []
        self.assertEqual(result, expected)


    def test_check_string_push_io_application_identifier_without_elements(self):
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
        result = check_string_push_io_application_identifier(self.content_file)
        expected = []
        self.assertEqual(result, expected)

    def test_check_string_push_io_application_identifier_many_values(self):
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
                <string name="pushio_application_identifier">pio-ABEgGFd_CNo9NOL_87c6k2GzI</string>
                <string name="pushio_application_identifier">pio-njj1jjNNGg</string>
                <string name="pushio_application_identifier">pio-Aasdasdkq_askjndk1jn2</string>
            </resources>
        '''
        result = check_string_push_io_application_identifier(self.content_file)
        expected = [
            'pio-ABEgGFd_CNo9NOL_87c6k2GzI',
            'pio-njj1jjNNGg',
            'pio-Aasdasdkq_askjndk1jn2'
        ]
        self.assertEqual(result, expected)

    def test_check_string_push_io_application_identifier_wrong_value_wrong_prefix(self):
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
                <string name="pushio_application_identifier">pia-njj1jjNNGg</string>
            </resources>
        '''
        result = check_string_push_io_application_identifier(self.content_file)
        expected = []
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()