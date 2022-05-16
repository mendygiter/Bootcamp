from user_crud import app
from flask import render_template, redirect, request
from user_crud.models.user import User


#3. Returns our query in our memory, we add inside render_template all_users = users
@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)

#build out a route that will take use to the create_user function
@app.route('/user')
def new_user(): 

    return render_template('create.html')


@app.route('/create', methods = ['POST'])
def create_user():
    data = {
        
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }

    user_id = User.new_user(data)
    return redirect(f'/show/{user_id}')


@app.route('/show/<int:id>')
def get_user(id):
    data = {
        'id': id
    }

    user = User.get_one(data)
    return render_template("readone.html", user = user)



#route to render update form
@app.route('/render/<int:id>')
def render_update(id):

    data = {
        'id': id
    }
    user = User.get_one(data)
    print(user.last_name)
    return render_template('update.html', user = user)

#proccessing route to update user
@app.route('/update', methods = ['POST'])
def update():

    data = {
        'id': request.form ['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.update_user(data)
    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }

    User.delete_user(data)
    return redirect('/')