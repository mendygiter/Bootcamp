from flask_app import app
# ...server.py

#remmember to change name of controller
from flask_app.controllers import users_controllers


if __name__=='__main__':
    app.run(debug=True)