from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja_render():
    dojos = Dojo.all_dojos()
    print(dojos)
    return render_template('ninja.html', all_dojos = dojos)

@app.route('/create/ninja', methods = ['POST'])
def new_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    
    Ninja.save(data)
    return redirect(f"/ninjas/{data['dojo_id']}")

