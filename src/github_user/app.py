from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

class GithubUserData():
    
    def __init__(self):
        user_name = user_name
        stars = stars
        
    def getting_user_name(self):
        user_name = user_name
        return user_name
        

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/form", methods=["POST", "GET"])
def get_user_nick():
    
    user_nick = request.form.get("search_user")
    
    response = requests.get(f"http://api.github.com/users/{user_nick}/repos")
    resp = response.json()
               
    return render_template('forms.html',user_nick=user_nick, repository_name=resp)


if __name__ == "__main__":
    app.run(debug = True)