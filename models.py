from app import db
from sqlalchemy.dialects.postgresql import JSON

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    movieName = db.Column(db.String())
    movieDirector = db.Column(db.String())
    movieYear = db.Column(db.String())

    allMovies = db.Column(JSON)

    # Initialize Movie class
    def __init__(self, movieName, movieDirector, movieYear, allMovies):
        self.movieName = movieName
        self.movieDirector = movieDirector
        self.movieYear = movieYear
        self.allMovies = allMovies

    # Represents the object when queried
    def __repr__(self):
        return '<id {}>'.format(self.id)