from tkinter import Y
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/hello_world') #function 1
def another_route():
    return 'Hello World!' #another link on this site

@app.route('/dojo') #function 2
def dojo():
    return 'Dojo!'

@app.route('/names/<say>/<name>') #function 3
def names(say, name):
    return f'{say} {name}'

@app.route('/<repeat>/<int:number_id>/<bye>')
def numbers(repeat, number_id, bye):
    return f'{repeat} {number_id} {bye}' * number_id










@app.route('/test/<route_data>') # set up new route
def test_data(route_data): 
    return f'the route data that was passed in was {route_data}' # calling the name of the function

@app.route('/multiply/int<x>/<y>')
def multiply_two_numbers(x, y):
    return f"the result is {x} and {y} is {x * Y} "

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)    # Run the app in debug mode.




@app.route('/success')
def success():
    return 'success'