from pymongo import MongoClient
import json

class UserModel:
    def __init__(self):
        config = json.load(open('./config.json', 'r'))
        client = MongoClient(config['mongoDB']['host'], config['mongoDB']['port'])
        self.db = client[config['mongoDB']['db']]

    def register_user(self,name,username,password):
        register_user_data = {
            'name' : name,
            'username' : username,
            'password' : password,
            'friends' : []
        }
        self.db.users.insert_one(register_user_data)

    def get_user_by_username(self, username):
        query = {
            'username': username
        }
        cursor = self.db.users.find(query)
        if cursor.count() == 0:
            return None
        for user in cursor:
            return user

    def authenticate(self, username, password):
        query = {
            'username': username,
            'password': password
        }
        cursor = self.db.users.find(query)
        if cursor.count() == 0:
            return False
        else:
            return True
