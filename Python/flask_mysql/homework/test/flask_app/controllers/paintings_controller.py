from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.painting import Painting
from flask_app.models.user import User




@app.route('/dashboard')
def home_page():
    
    paintings = Painting.all_paintings()
    print(paintings)

    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/')

    return render_template('success.html', all_paintings = paintings)


@app.route('/new_painting')
def create_painting():

    if 'user_id' not in session: 
        flash('You must be logged in')

        return redirect('/new_painting')

    return render_template('new.html')

    
@app.route('/new', methods = ['POST'])
def new_painting():

    data = {
        'users_id': session['user_id'],
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        }

    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/new_painting')

    if Painting.validate_painting(data):

        Painting.new_painting(data)

        return redirect('/dashboard')

    else:
        return redirect('/new_painting')


@app.route('/show/<int:id>')
def get_painting(id):
    data = {
        'id': id
    }

    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/new')

    get_painting = Painting.get_one(data)
    return render_template('getone.html', painting = get_painting)


@app.route('/render/<int:id>')
def render_update(id):
    data = {
        'id': id
    }
    get_painting = Painting.get_one(data)
    return render_template('edit.html', painting = get_painting)



@app.route('/update/<int:id>', methods =['POST'])
def edit_painting(id):

    data = {
        'user_id': session['user_id'],
        'id': id,
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price']
        }


    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('render')


    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/edit_painting')

    if Painting.validate_painting(data):

        Painting.edit_painting(data)
        return redirect('/dashboard')








@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }

    Painting.delete_painting(data)
    return redirect('/dashboard')