from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dont share with anyone'

@app.route('/')
def counter():
    if 'counts' in session:
        session['counts'] = session['counts'] + 1
    else:
        session['counts'] = 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session['counts'] = 0

    return redirect('/')

if __name__=="__main__":
    app.run(debug = True)

