# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
import twitter

app = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")


@app.route('/')
def index():
    return render_template("index.html")
