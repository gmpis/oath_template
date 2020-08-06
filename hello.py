from flask import Flask, redirect  #, url_for
import urllib.parse
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/start')
def start_oauth():

    # read values from env vars
    l_state = 111111  # TODO generate random value, used to maintain state and prevent csrf attacks

    l_client_id = os.getenv("OAUTH_CLIENT_ID", "12345")  # from dev portal
    l_redirect_url = os.getenv("REDIRECT_URL", "http://localhost")  # url for callback (this server), case sensitive and must match value registered on dev portal
    # scope param is not supported, must be declared on dev portal

    # create url from vars
    l_dict = {"response_type": "code", "client_id": l_client_id, "state": l_state, "redirect_url": l_redirect_url}
    l_params = urllib.parse.urlencode(l_dict)

    auth_base_url = "https://www.bungie.net/en/oauth/authorize?%s" % l_params

    # print(l_params)
    # print(auth_base_url)
    # return "DEV:"+auth_base_url

    # do redirect
    return redirect(auth_base_url)
