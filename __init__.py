from flask import Flask
import json

app = Flask(__name__)

config = json.load(open('./config.json', 'r'))
app.secret_key = config['secret_key']

from users import routes
from posts import routes