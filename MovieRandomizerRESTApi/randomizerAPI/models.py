from app import db
from sqlalchemy.dialects.postgresql import JSON

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    movieName = db.Column(db.String())
    movieDirector = db.Column(db.String())
    movieYear = db.Column(db.String())
    dateWatched = db.Column(db.String())

    # Initialize Movie class
    def __init__(self, movieName, movieDirector, movieYear, dateWatched):
        self.movieName = movieName
        self.movieDirector = movieDirector
        self.movieYear = movieYear
        self.dateWatched = dateWatched

    # Represents the object when queried
    def __repr__(self):
        return '<id {}>'.format(self.id)