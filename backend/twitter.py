# -*- coding: utf-8 -*-
import config
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(
    config.consumer_key,
    config.consumer_secret,
    config.access_token,
    config.access_secret)
