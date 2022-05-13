from flask import Flask, render_template, redirect, request

from user import User

app = Flask(__name__)

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

    User.new_user(data)
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)