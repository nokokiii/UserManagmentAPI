import unittest

from src.api import app
from src.db import create_conn

class FlaskIntegrationTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def test_create_update_delete_get_user(self):
        # Clear database
        conn = create_conn()
        conn["users"].drop(ignore=True)
        
        # Create user
        response = self.app.post('/users', json={"name": "John", "lastname": "Doe"})
        self.assertEqual(response.status_code, 201)
        
        # Check if user exists and has correct values
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "John", "lastname": "Doe"})
        
        # Update user name
        response = self.app.patch('/users/1', json={"name": "Aduarto"})
        self.assertEqual(response.status_code, 204)
        
        # Check if user has correct values
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "Aduarto", "lastname": "Doe"})
        
        # Update user lastname
        response = self.app.patch('/users/1', json={"lastname": "Montanof"})
        self.assertEqual(response.status_code, 204)
        
        # Check if user has correct values

        
        # Delete user
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)
        
        # Check if user exists
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 404)

    
    
    def test_update_add_id(self):
        # Clear database
        conn = create_conn()
        conn["users"].drop(ignore=True)
        
        # Generate example users
        response = self.app.get('/generate_users')
        self.assertEqual(response.status_code, 201)
        
        # Update user with update_add_user
        response = self.app.put('/users/1', json={"name": "John", "lastname": "Smith"})
        self.assertEqual(response.status_code, 204)
        
        # Check if user has correct values
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "John", "lastname": "Smith"})
        
        # Create new user with id 700
        response = self.app.put('/users/700', json={"name": "John", "lastname": "Smith"})
        self.assertEqual(response.status_code, 201)
        
        # Check if user has correct values
        response = self.app.get('/users/700')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "John", "lastname": "Smith"})
        
        # Create new user
        response = self.app.post('/users', json={"name": "James", "lastname": "Miller"})
        self.assertEqual(response.status_code, 201)
        
        # Check if user has correct values and id 701
        response = self.app.get('/users/701')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "James", "lastname": "Miller"})
    
    
    def test_create_update_delete_get_all(self):
        # Clear database
        conn = create_conn()
        conn["users"].drop(ignore=True)
        
        # Generate example users
        response = self.app.get('/generate_users')
        self.assertEqual(response.status_code, 201)
        
        # Check if get_all_users returns correct values
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.json), list)
        self.assertEqual(len(response.json), 6)
        self.assertEqual(response.json, [
                {"name": "John", "lastname": "Doe", "rowid": 1},
                {"name": "Alex", "lastname": "Smith", "rowid": 2},
                {"name": "Emily", "lastname": "Johnson", "rowid": 3},
                {"name": "Chris", "lastname": "Williams", "rowid": 4},
                {"name": "Jessica", "lastname": "Brown", "rowid": 5},
                {"name": "Michael", "lastname": "Davis", "rowid": 6}
        ])
        
        # Create user
        response = self.app.post('/users', json={"name": "Leo", "lastname": "Wilson"})
        self.assertEqual(response.status_code, 201)
        
        # Check if users have correct values
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.json), list)
        self.assertEqual(len(response.json), 7)
        self.assertEqual(response.json, [
                {"name": "John", "lastname": "Doe", "rowid": 1},
                {"name": "Alex", "lastname": "Smith", "rowid": 2},
                {"name": "Emily", "lastname": "Johnson", "rowid": 3},
                {"name": "Chris", "lastname": "Williams", "rowid": 4},
                {"name": "Jessica", "lastname": "Brown", "rowid": 5},
                {"name": "Michael", "lastname": "Davis", "rowid": 6},
                {"name": "Leo", "lastname": "Wilson", "rowid": 7}
        ])
        
        # Update user
        response = self.app.patch('/users/7', json={"name": "Leonard", "lastname": "Wilson"})
        self.assertEqual(response.status_code, 204)
        
        # Check if users have correct values
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.json), list)
        self.assertEqual(len(response.json), 7)
        self.assertEqual(response.json, [
                {"name": "John", "lastname": "Doe", "rowid": 1},
                {"name": "Alex", "lastname": "Smith", "rowid": 2},
                {"name": "Emily", "lastname": "Johnson", "rowid": 3},
                {"name": "Chris", "lastname": "Williams", "rowid": 4},
                {"name": "Jessica", "lastname": "Brown", "rowid": 5},
                {"name": "Michael", "lastname": "Davis", "rowid": 6},
                {"name": "Leonard", "lastname": "Wilson", "rowid": 7}
        ])
        
        # Create user with id 700
        response = self.app.put('/users/700', json={"name": "Jeo", "lastname": "Biden"})
        self.assertEqual(response.status_code, 201)
        
        # Check if users have correct values
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.json), list)
        self.assertEqual(len(response.json), 8)
        self.assertEqual(response.json, [
                {"name": "John", "lastname": "Doe", "rowid": 1},
                {"name": "Alex", "lastname": "Smith", "rowid": 2},
                {"name": "Emily", "lastname": "Johnson", "rowid": 3},
                {"name": "Chris", "lastname": "Williams", "rowid": 4},
                {"name": "Jessica", "lastname": "Brown", "rowid": 5},
                {"name": "Michael", "lastname": "Davis", "rowid": 6},
                {"name": "Leonard", "lastname": "Wilson", "rowid": 7},
                {"name": "Jeo", "lastname": "Biden", "rowid": 700}
        ])
        
        # Delete user
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)
        
        # Check if users have correct values
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.json), list)
        self.assertEqual(len(response.json), 7)
        self.assertEqual(response.json, [
                {"name": "Alex", "lastname": "Smith", "rowid": 2},
                {"name": "Emily", "lastname": "Johnson", "rowid": 3},
                {"name": "Chris", "lastname": "Williams", "rowid": 4},
                {"name": "Jessica", "lastname": "Brown", "rowid": 5},
                {"name": "Michael", "lastname": "Davis", "rowid": 6},
                {"name": "Leonard", "lastname": "Wilson", "rowid": 7},
                {"name": "Jeo", "lastname": "Biden", "rowid": 700}
        ])
