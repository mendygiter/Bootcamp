from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#How we create redirect to a new page
@app.route('/results', methods = ['POST'])
def recieve_form():
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port = 5005)
