from flask import Flask

app = Flask('class2python')

@app.route("/") #root
def home():
    return "This is the home page"

#Create an about endpoint and show your name

@app.route("/about") 
def about():
    me = {
        "first": "Nathan",
        "last": "Hundley",
        "age": 29
    }
    return "<h2>Nathan Hundley</h2>"



app.run(debug=True)

