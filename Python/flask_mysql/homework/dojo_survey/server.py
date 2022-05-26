from flask import Flask, render_template, redirect, request, session
app =  Flask(__name__)
app.secret_key = 'shhh'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proccess', methods = ['POST'])
def proccessing():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def show_results():
    return render_template(
        'result.html', name = session ['name'], location = session['location'], language = session ['language'], Comment = session ['comment']
    )

if __name__=="__main__":   
    app.run(debug=True)  

