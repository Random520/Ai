from flask import Flask, render_template, request, redirect, url_for
  
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/AI') 
def says():    
        return render_template("ex.html", word=word )  
app.run        
