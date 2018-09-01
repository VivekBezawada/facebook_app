from facebook_app import app
from flask import render_template,request,jsonify,redirect,url_for,session
from facebook_app.models.Post import PostModel
from users.decorators import is_login

post_model = PostModel()

@app.route('/posts')
@is_login
def posts():
    posts = post_model.get_all_posts()
    print(posts)
    return render_template('posts/posts.html', posts = posts)

@app.route('/posts/create',methods=['GET','POST'])
@is_login
def create_post():
    if request.method == 'POST':
        username = session['username']
        title = request.form['title']
        content = request.form['content']
        post_model.create_post(username,title,content)
        return redirect(url_for('posts'))
    return render_template('posts/create.html')