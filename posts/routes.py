from facebook_app import app
from flask import render_template,request,jsonify,redirect,url_for,session
from facebook_app.models.Post import PostModel
from users.decorators import is_login

post_model = PostModel()

@app.route('/posts')
@is_login
def posts():
    posts = post_model.get_all_posts()
    username = session['username']
    updated_posts_list = []
    for post in posts:
        can_like = True
        for liked_username in post['likes']:
            if (liked_username == username):
                can_like = False
        if post['username'] == username:
            can_like = False
        post['can_like'] = can_like
        updated_posts_list.append(post)

    return render_template('posts/posts.html', posts = updated_posts_list)

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

@app.route('/posts/like/<post_id>')
@is_login
def like_post(post_id):
    username = session['username']
    post_model.like_post_by_post_id(username,post_id)
    return redirect(url_for('posts'))

@app.route('/posts/edit/<post_id>', methods=['GET','POST'])
@is_login
def edit_post(post_id):
    post_data = post_model.get_post_by_id(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post_model.update_data_by_post_id(title,content,post_id)
        return redirect(url_for('posts'))
    return render_template('posts/create.html',update=True,post_id = post_id,title=post_data['title'],content=post_data['content'])

@app.route('/posts/delete/<post_id>')
@is_login
def delete_post(post_id):
    username = session['username']
    post_model.delete_by_id(post_id)
    return redirect(url_for('posts'))