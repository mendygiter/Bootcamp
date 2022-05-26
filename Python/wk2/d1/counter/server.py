from typing import Counter
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dont share with anyone'

@app.route('/')
def counter():
    return render_template('index.html')