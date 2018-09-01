from pymongo import MongoClient
import json

class PostModel:
    def __init__(self):
        config = json.load(open('./config.json', 'r'))
        client = MongoClient(config['mongoDB']['host'], config['mongoDB']['port'])
        self.db = client[config['mongoDB']['db']]

    def create_post(self,username,title,content):
        create_post_data = {
            'username' : username,
            'title' : title,
            'content' : content
        }
        self.db.posts.insert_one(create_post_data)

    def get_all_posts(self):
        cursor = self.db.posts.find({})
        posts = cursor if cursor.count() > 0 else None
        return posts
