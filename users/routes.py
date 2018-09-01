from facebook_app import app
from flask import render_template,request,jsonify

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=('GET','POST'))
def login():
    if request.method == 'POST':
        login_data = {
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        return jsonify(login_data)
    return render_template('users/login.html')

@app.route('/register',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        register_data = {
            'name' : request.form['name'],
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        return jsonify(register_data)
    return render_template('users/register.html')