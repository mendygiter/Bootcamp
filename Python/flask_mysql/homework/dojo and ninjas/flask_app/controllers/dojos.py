from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos

@app.route('/home')
def index():
    dojos = Dojos.all_dojos()
    print(dojos)
    return render_template('dojo.html', all_dojos = dojos)