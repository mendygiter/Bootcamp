from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

from flask_bcrypt import Bcrypt    

bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 

@app.route('/')
def index():
    return render_template('index.html')

#proccessing method for register
@app.route('/user/register', methods = ['POST'])
def register_user():
    
    #validate user
    if User.validate_user(request.form):
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
            }
        
        # User.create_user(data)

    else: 
        print('is not valid')
    
    # if valid add to database

    return redirect('/')



