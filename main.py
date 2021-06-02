
import pandas as pd
import random
from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def home():
    with open('myweapons.json') as f:
        data = json.load(f)

    return render_template('index.html', weapon = data)


if __name__ == "__main__":
    app.run(debug = True)