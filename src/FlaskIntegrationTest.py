import unittest
from api import app

class FlaskIntegrationTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        
if __name__ == "__main__":
    unittest.main()