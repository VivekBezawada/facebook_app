from pymongo import MongoClient
import json

class PostModel:
    def __init__(self):
        config = json.load(open('./config.json', 'r'))
        client = MongoClient(config['mongoDB']['host'], config['mongoDB']['port'])
        self.db = client[config['mongoDB']['db']]
