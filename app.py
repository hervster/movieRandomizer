import os
from random import randint
from datetime import datetime
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from dotenv import load_dotenv

# Import env variables
load_dotenv()

# Set up application and configuration
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect to database
db = SQLAlchemy(app)

from models import Movie

@app.route('/')
def hello():
    return "What up my g?, it's " + datetime.today().strftime('%m/%d/%Y')
    
@app.route('/test')
def testMeth():
    # testMovie = Movie.query.get((randint(1,2)))
    testMovie = Movie.query.filter_by(dateWatched=None)
    return testMovie[1].movieName

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# For google assistant api
@app.route('/randomMovieGoogle', methods=['GET','POST'])
def returnRandomizedMovieGoogle():
    global movieList
    if request.method == 'GET':
        movieList = pullData() # Array
        
        movie = randomizeMovie()
        return {"message": "success", "data" : movie}

    else:    
        movieList = pullData() # Array
        
        movie = randomizeMovie()
        gRequest = request.get_json()
        print(gRequest)
        return {
            "session": {
                "id": gRequest.session.id,
                "params": gRequest.session.params
            },
            "prompt": {
                "override": false,
                "firstSimple": {
                    "speech": "You are watching \""+movie.movieName+"\", directed by \""+movie.movieDirector+"\", in \""+movie.movieYear+"\".",
                    "text": "You are watching \""+movie.movieName+"\", directed by \""+movie.movieDirector+"\", in \""+movie.movieYear+"\"."  
                }
            },
            "scene": {
                "name": gRequest.scene.name,
                "slots":gRequest.scene.slots,
                "next": {
                    "name": "actions.scene.END_CONVERSATION"
                }
            }
        }


@app.route('/randomMovie')
def returnRandomizedMovie():
    global movieList
    movieList = pullData() # Array
    
    movie = randomizeMovie()
    return {"message": "success", "data": movie}



''' Pulls all of the database data, filtering by dateWatched column  '''
def pullData():
    try:
        unwatchedMovies = Movie.query.filter_by(dateWatched=None)
    except:
        print("No unwatched movies.")
    # DB is small (<1000), find better solution if expanding
    movieList = [
        {
            "id": movie.id,
           "title": movie.movieName,
           "director": movie.movieDirector,
           "year": movie.movieYear, 
           "dateWatched": movie.dateWatched
        } for movie in unwatchedMovies    ]
    return movieList



''' Returns a random movie from database in JSON format '''
def randomizeMovie():    
    size = len(movieList)  # Figure out a better way to do this to save space

    if size == 0:
        return {"error": "No unwatched films"}
    # Random number based on size of list
    randomNumber = randint(0,(size-1))

    # Grabbing id from list of unwatched films
    randomMovieID = movieList[randomNumber]['id']

    # Query by ID
    try:
        randomMovie = Movie.query.get(randomMovieID)
    except:
        print("No movie with this id: " + randomMovieID)
    
    # Don't return anything if there are no unwatched films
    if randomMovie.dateWatched != None: 
        return {"error": "No unwatched films"}

    randomMovieResponse = {
        "title": randomMovie.movieName,
        "director": randomMovie.movieDirector,
        "year": randomMovie.movieYear, 
        "dateWatched": randomMovie.dateWatched
    }

    # Update randomMovie in database dateWatched column item
    randomMovie.dateWatched = datetime.today().strftime('%m/%d/%Y')
    print(randomMovie)
    print(randomMovie.dateWatched)
    db.session.add(randomMovie)
    db.session.commit()

    return randomMovieResponse


if __name__ == '__main__':
    app.run()