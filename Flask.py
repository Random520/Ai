from flask import *
app = Flask(__name__)
with open("more.Html","r") as t:
    j = t.read()
with open("Home.Html","r") as f:
    code = f.read()
@app.route("/")
def home():
    return code

@app.route("/more")
def more():
    return j

if __name__ == '__main__':
    app.run()
