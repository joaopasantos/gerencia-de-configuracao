from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
        return "Flask!"

@app.route("/hello")
def hello():
    return "Hello!"

@app.route("/hello/<name>")
def helloName(name):
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)