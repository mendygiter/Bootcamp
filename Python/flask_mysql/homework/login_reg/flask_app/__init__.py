from flask import Flask

app = Flask(__name__)
app.secret_key = "dont share this pass"

# __init__.py