from flask import Flask, app, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Dane"
