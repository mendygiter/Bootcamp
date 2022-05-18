from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

#home page route, ditionary with list of dojos and create dojo
@app.route('/home')
def index():
    dojos = Dojo.all_dojos()
    print(dojos)
    return render_template('dojo.html', all_dojos = dojos)

#proccess create dojo route
@app.route('/create', methods = ['POST'])
def new_dojo():
    data = {
        'name': request.form['name']
    }

    Dojo.new_dojo(data)
    return redirect('/home')

@app.route('/dojos/<int:id>')
def school_data(id):
    data = {
        'id': id
    }

    dojo_ninjas = Dojo.show_ninja_from_dojo(data)
    return render_template('dojos.html', dojo_ninjas = dojo_ninjas)



