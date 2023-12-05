import unittest
import src.api as api
from src.db import create_conn

class FlaskUnitTest(unittest.TestCase):
        
    def test_all_users(self):
        with api.app.test_request_context():
            response, status_code = api.get_all_users()
            self.assertEqual(status_code, 200)
            self.assertIs(type(response), list)
    
    
    def test_get_user(self):
        with api.app.test_request_context():
            response, status_code = api.get_user(1)
            self.assertEqual(status_code, 200)
            self.assertIs(type(response), dict)
            
            
    def test_create_user(self):
        with api.app.test_request_context():
            data = {"name": "test", "lastname": "test"}
            response, status_code = api.create_user(data)
            self.assertEqual(status_code, 201)
            self.assertIs(type(response), dict)
            
            response, status_code = api.create_user({})
            self.assertEqual(status_code, 400)
            self.assertIs(type(response), dict)
            
    def test_update_user(self):
        with api.app.test_request_context():
            data = {"name": "test"}
            response, status_code = api.update_user(1, data)
            self.assertEqual(status_code, 204)
            self.assertIs(type(response), dict)
            
            data = {"lastname": "test"}
            response, status_code = api.update_user(1, data)
            
            response, status_code = api.update_user(100, data)
            self.assertEqual(status_code, 404)
            self.assertIs(type(response), dict)
            
            response, status_code = api.update_user(1, {})
            self.assertEqual(status_code, 400)
            self.assertIs(type(response), dict)
    
    
    def test_update_add_user(self):
        with api.app.test_request_context():
            data = {"name": "test", "lastname": "test"}
            response, status_code = api.update_add_user(1, data)
            self.assertEqual(status_code, 204)
            self.assertIs(type(response), dict)
            
            response, status_code = api.update_add_user(100, data)
            self.assertEqual(status_code, 404)
            self.assertIs(type(response), dict)
            
            response, status_code = api.update_add_user(1, {})
            self.assertEqual(status_code, 400)
            self.assertIs(type(response), dict)
            
    
    def test_delete_user(self):
        with api.app.test_request_context():
            response, status_code = api.delete_user(1)
            self.assertEqual(status_code, 204)
            self.assertIs(type(response), dict)
            
            response, status_code = api.delete_user(100)
            self.assertEqual(status_code, 404)
            self.assertIs(type(response), dict)
                
unittest.main()
