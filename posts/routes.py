from facebook_app import app
from flask import render_template,request,jsonify,redirect,url_for,session
from facebook_app.models.Post import PostModel
from users.decorators import is_login

@app.route('/posts')
@is_login
def posts():
    return "Posts"