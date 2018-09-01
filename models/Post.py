from pymongo import MongoClient
from bson.objectid import ObjectId
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
            'content' : content,
            'likes' : []
        }
        self.db.posts.insert_one(create_post_data)

    def get_all_posts(self):
        cursor = self.db.posts.find({})
        posts = cursor if cursor.count() > 0 else None
        return posts

    def get_post_by_id(self,post_id):
        query = {
            '_id' : ObjectId(post_id)
        }
        cursor = self.db.posts.find(query)
        post_data = cursor[0] if cursor.count() > 0 else None
        if post_data is None:
            return False
        return post_data

    def update_data_by_post_id(self,title,content,post_id):
        query = {
            '_id' : ObjectId(post_id)
        }
        cursor = self.db.posts.find(query)
        post_data = cursor[0] if cursor.count() > 0 else None
        if post_data is None:
            return False
        self.db.posts.update_one(query,{'$set':{'title':title,'content':content}})

    def like_post_by_post_id(self,username,post_id):
        query = {
            '_id' : ObjectId(post_id)
        }
        cursor = self.db.posts.find(query)
        post_data = cursor[0] if cursor.count() > 0 else None
        if post_data is None:
            return False
        print("Post Data is ")
        print(post_data)
        post_likes = post_data['likes']
        post_likes.append(username)
        self.db.posts.update_one(query,{'$set':{'likes':post_likes}})

    def delete_by_id(self,post_id):
        self.db.posts.delete_one({'_id': ObjectId(post_id)})

