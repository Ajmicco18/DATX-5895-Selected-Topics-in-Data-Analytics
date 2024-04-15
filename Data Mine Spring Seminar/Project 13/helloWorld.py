from flask import Flask
from flask import render_template

#print("Hello World")

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

app.run(host='0.0.0.0',port=8000,debug=True)