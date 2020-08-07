from flask import Flask, redirect, request  #, url_for
import os
import urllib.parse
import requests as ex_requests
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


@app.route('/callback', methods=["GET", "POST"])
def callback_oauth():

    # log incoming request
    print(request.method)  # "GET", "POST"
    print(request.args)  # access url params ?key=123 eg: request.args.get("key", ""))
    print(request.form)  # access form data posted to this endpoint, eg: request.form["user"]

    # read values from env vars
    l_code = request.args.get("code", "0")  # get code from request
    l_client_id = os.getenv("OAUTH_CLIENT_ID", "12345")  # from dev portal
    l_client_secret = os.getenv("OAUTH_CLIENT_SECRET", "12345")  # from dev portal
    l_redirect_url = os.getenv("REDIRECT_URL", "http://localhost")  # url for callback (this server), case sensitive and must match value registered on dev portal

    # create request from vars
    l_dict = {"grant_type": "authorization_code", "code": l_code, "client_id": l_client_id, "client_secret": l_client_secret, "redirect_url": l_redirect_url}
    auth_token_url = "https://www.bungie.net/platform/app/oauth/token"

    # do post request to get token
    m_access_token = ""
    m_resp = ex_requests.post(auth_token_url, data=l_dict)  # post data as x-www-form-urlencoded
    if m_resp.status_code == ex_requests.codes.ok:
        print("Post was successful!")
        full_json_body = m_resp.json()
        print(full_json_body)
        # extract token from response
        m_access_token = full_json_body["access_token"]

        # extract refresh token from response
        m_refresh_token = full_json_body["refresh_token"]
        # TODO save refresh token to db
        # ...
    else:
        print("Res:"+m_resp.text)
        return "Error couldn\'t get access token"

    # return token
    return "Access token: "+m_access_token
