import os
from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


@app.route("/")
def home():
    return "CI/CD Day 4 — deployed live via a pipeline! 🚀"


@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return {"result": add(a, b)}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)