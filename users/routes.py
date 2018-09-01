from facebook_app import app
from flask import render_template,request,jsonify,redirect,url_for,session
from facebook_app.models.User import UserModel

user_model = UserModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username =  request.form['username']
        password = request.form['password']

        user_model.authenticate(username,password)
        session['username'] = user_model.get_user_by_username(username)['username']
        return redirect(url_for('posts'))
    # TODO : Implement Flash Message that username / password does not match
    return render_template('users/login.html')

@app.route('/register',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        
        user_exists = False if user_model.get_user_by_username(username) is None else True
 
        # continue if false
        if not user_exists:
            user_model.register_user(name,username,password)
            user_data = user_model.get_user_by_username(username)
            return redirect(url_for('login'))
        # TODO : Implement Flash Message that the user exists
        return render_template('users/register.html')
    return render_template('users/register.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))