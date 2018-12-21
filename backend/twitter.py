# -*- coding: utf-8 -*-
import config
import json
import requests
import urllib
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(
    config.CK,
    config.CS,
    config.AT,
    config.AS)


def upload(img_url):
    url_media = 'https://upload.twitter.com/1.1/media/upload.json'
    data = urllib.request.urlopen(img_url).read()
    response = twitter.post(url_media, files={'media': data})
    if response.status_code != 200:
        return {'message': '画像をアップロードできませんでした'}
    else:
        media_id = json.loads(response.text)['media_id']
        return {'media_ids': [media_id]}


def post(params):
    url_text = 'https://api.twitter.com/1.1/statuses/update.json'
    response = twitter.post(url_text, params=params)
    if response.status_code != 200:
        return {'message': '投稿に失敗しました'}
    else:
        return {'message': '投稿に成功しました'}
