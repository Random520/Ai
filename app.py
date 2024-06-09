from flask import Flask, render_template, request, redirect, url_for
import pyttsx3
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/AI', methods=['GET', 'POST']) 
def says():
    if request.method == 'POST': 
    
        word = request.form.get('say') 
        return render_template("ex.html", word=word )
        time.sleep(2) 
        speak("word")
    else: 
         
     return render_template("index.html") 
app.run        
