from flask import Flask

print('about to set app var')
app = Flask(__name__)

print('about to define route')
@app.route('/')
def hello():
    return 'Hello World! this is an app'