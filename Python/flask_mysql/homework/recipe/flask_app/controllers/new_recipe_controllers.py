from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.new_recipe import Recipe
from flask_app.models.user import User


@app.route('/dashboard')
def home_page():
    
    recipes = Recipe.all_recipes()
    print(recipes)

    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/')

    return render_template('success.html', all_recipes = recipes)

@app.route('/new_recipe')
def create_recipe():

    if 'user_id' not in session: 
        flash('You must be logged in')

        return redirect('/new_recipe')

    return render_template('new.html')
    
@app.route('/new', methods = ['POST'])
def new_recipe():

    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'made_on': request.form['made_on'],
        'description': request.form['description'],
        'under_30_min': request.form['under_30_min'],
        'instructions': request.form['instructions'],
    }

    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/new_recipe')

    if Recipe.validate_recipe(data):

        new_recipe = Recipe.new_recipe(data)
        return redirect('/dashboard')

    else:
        return redirect('/new_recipe')


@app.route('/show/<int:id>')
def get_recipe(id):
    data = {
        'id': id
    }

    if 'user_id' not in session: 
        flash('You must be logged in')
        return redirect('/new')

    get_recipe = Recipe.get_one(data)
    return render_template('getone.html', recipe = get_recipe)


@app.route('/render/<int:id>')
def render_update(id):
    data = {
        'id': id
    }
    get_recipe = Recipe.get_one(data)
    return render_template('edit.html', recipe = get_recipe)


@app.route('/update/<int:id>', methods =['POST'])
def edit_user(id):

    data = {
        'user_id': session['user_id'],
        'id': id,
        'name': request.form['name'],
        'made_on': request.form['made_on'],
        'description': request.form['description'],
        'under_30_min': request.form['under_30_min'],
        'instructions': request.form['instructions'],
    }

    Recipe.edit_recipe(data)
    return redirect('/dashboard')
    

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }

    Recipe.delete_recipe(data)
    return redirect('/dashboard')