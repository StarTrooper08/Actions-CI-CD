from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/build")
def build():
    return "<p>Updated flask app for testing Github actions workflow</p>"


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)