from flask import Flask, render_template
from helpers import generate_checkerboard

app = Flask(__name__)

if __name__=='__main__':
    app.run(debug = True)

# @app.route('/')
# def index():
#     return 'hello!'

@app.route('/')
def checkerboard_1():
    result = generate_checkerboard(8, 8)
    return render_template('index.html', result = result )


@app.route('/<int:y>')
def checkerboard_2(y):
    result = generate_checkerboard(8, y)
    return render_template('index.html', result = result )

@app.route('/<int:x>/<int:y>')
def checkerboard_3(x, y):
    result = generate_checkerboard(x, y)
    return render_template('index.html', result = result )

