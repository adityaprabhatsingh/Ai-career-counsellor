from flask import Flask 


app = Flask(__name__)

@app.route('/')
def home():
    return "the app is running successfully in the server and ready to use for the users"