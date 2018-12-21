# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
import twitter

app = Flask(__name__,
            static_folder='../dist/static',
            template_folder='../dist')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tweet', methods=['GET', 'POST'])
def tweet_with_img():
    if request.method == 'POST':
        json = request.get_json()
        img_url = json['img']
        message = json['msg'] if 'msg' in json.keys() else ''
        response = twitter.upload(img_url)
        if 'media_ids' in response.keys():
            response['status'] = message + ' #speeech'
            response = twitter.post(response)
            return jsonify(response)
        else:
            return jsonify(response)
    else:
        return jsonify(response)
