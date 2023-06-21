import unittest
import os

class CustomTextTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.passed_tests = []
        self.failed_tests = []
        self.error_tests = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed_tests.append(test)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed_tests.append((test, err))

    def addError(self, test, err):
        super().addError(test, err)
        self.error_tests.append((test, err))

    def printErrors(self):
        if self.passed_tests:
            self.stream.writeln("Passed tests:")
            for test in self.passed_tests:
                test_name = self.get_test_name(test)
                self.stream.writeln("{}: Passed".format(test_name))
            self.stream.writeln()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed_tests.append((test, err))

    def printErrors(self):
        if self.failed_tests:
            self.stream.writeln("Failed tests:")
            for test, err in self.failed_tests:
                test_name = self.get_test_name(test)
                self.stream.writeln("{}: Failed".format(test_name))
                self.stream.writeln("Result: {}".format(err[1]))
                self.stream.writeln("Expected: {}".format(err[0]))
                self.stream.writeln()


        super().printErrors()

    def get_test_name(self, test):
        return test.id().split('.')[-1]

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=current_dir, pattern='unit_test_*.py')

    runner = unittest.TextTestRunner(verbosity=1, resultclass=CustomTextTestResult)
    runner.run(suite)
# import unittest
# import os

# if __name__ == '__main__':

#     current_dir = os.path.dirname(os.path.abspath(__file__))
    
#     loader = unittest.TestLoader()
#     suite = loader.discover(start_dir=current_dir, pattern='unit_test_*.py')
#     runner = unittest.TextTestRunner(verbosity=1)
#     runner.run(suite)