import os
from flask import Flask
from dotenv import load_dotenv

# Import env variables
load_dotenv()

# Set up application and configuration
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))


@app.route('/')
def hello():
    return "What up my g?"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()