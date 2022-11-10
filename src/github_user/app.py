from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/form", methods=["POST"])
def get_user_nick():
    user_nick = request.form.get("search_user")
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug = True)