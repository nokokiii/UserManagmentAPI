import unittest

from src.tests.FlaskIntegrationTest import FlaskIntegrationTest
from src.tests.FlaskUnitTest import FlaskUnitTest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    
    suite = loader.loadTestsFromTestCase(FlaskIntegrationTest)
    suite.addTests(loader.loadTestsFromTestCase(FlaskUnitTest))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
     