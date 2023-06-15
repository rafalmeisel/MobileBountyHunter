import unittest
import os

if __name__ == '__main__':

    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=current_dir, pattern='unit_test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)