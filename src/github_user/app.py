from flask import Flask, render_template, request
import requests
import json



app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/form", methods=["POST", "GET"])
def get_user_nick():
    
    user_nick = request.form.get("search_user")
    
    response = requests.get(f"http://api.github.com/users/{user_nick}/repos")
    resp = response.status_code
    return render_template('form.html', user_nick=resp)


if __name__ == "__main__":
    app.run(debug = True)