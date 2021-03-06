from flask import Flask, render_template, redirect, request
#import freind class
from friend import Friend

app = Flask(__name__)

@app.route('/')
def index():
    friends = Friend.get_all() #This gets all the data from freinds class
    print(friends)
    return render_template("index.html", friends = friends)


@app.route('/add_data', methods = ['POST'])
def add_data():
    data = {
        'first_name': 'Shui',
        'last_name': 'Kastel',
        'occupation': 'Founder'
    }
    Friend.insert_friends(data)
    return redirect('/')
    


@app.route('/show/<int:id>')
def get_friend(id):
    data = {
        'id': id
    }

    friend = Friend.get_one(data)
    return render_template("show_one.html", friend = friend)



@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)