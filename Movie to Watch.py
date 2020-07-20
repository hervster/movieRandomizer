# Author : Herve Nyemeck
# Randomly pick a line from pre-existing file
# Output said line and email to user

# import sendEmail 
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from datetime import datetime
import os
import sys

movieListFile = "Movies to Watch.txt"
oldMovieListFile = "Old Movies.txt"
today = "Today.txt"

def removePreexisting():
    exists = os.path.isfile(today)
    if exists:
        os.remove(today)
    else:
        return  

removePreexisting()

file = open(movieListFile,"r")
lines = []
for line in file:
    lines.append(line)
size = len(lines)



movie=""
def generateMovie():    
    random_number = randint(0,(size-1))
    global movie
    movie = lines[random_number]
generateMovie()
file.close()

old_movies = open(oldMovieListFile,"r")
old_movies_list = []

for line in old_movies:
    old_movies_list.append(line)
    

#def runItBack():
while movie in old_movies_list:
    generateMovie()

old_movies.close()

old_movies = open(oldMovieListFile,"a")
old_movies.write(movie)
old_movies.close()
# print(movie)
file.close()

today_movie = open(today, "w")
today_movie.write(movie)
today_movie.close()
# sendEmail.sendEmail()
# sys.exit()
#print (file.readlines())

# msg = EmailMessage()
#runItBack()