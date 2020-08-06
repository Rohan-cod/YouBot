from flask import Flask, render_template, request

#from chatbot import chatbot
import os
from pytube import YouTube





app = Flask(__name__)
app.static_folder = 'static'

    
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    yt = YouTube(str(userText))
    ys = yt.streams.get_highest_resolution()
    l=[("Title: " + str(yt.title)), ("Views: " + str(yt.views)), ("Length: " + str(yt.length)), ("Ratings: " + str(yt.rating))]
    print(str("\n".join(l)))
    ys.download()
    return str("\t\t\t".join(l))


