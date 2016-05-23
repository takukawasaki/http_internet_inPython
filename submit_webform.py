#!/usr/local/bin/python3

import requests
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

ID_USERNAME = ''
ID_EMAIL = 'example.com'
ID_PASSWORD = ''
USERNAME = ''
EMAIL = '@example.com'
PASSWORD = ''
SIGNUP_URL = 'https://twitter.com/account/create'


def submit_form():
    """Submit a form"""
    payload = {ID_USERNAME : USERNAME,
               ID_EMAIL    :  EMAIL,
               ID_PASSWORD : PASSWORD,}
    
    # make a get request
    resp = requests.get(SIGNUP_URL)
    print("Response to GET request: %s" %resp.content)
    
    # send POST request
    resp = requests.post(SIGNUP_URL, payload)
    print("Headers from a POST request response: %s" %resp.headers)
    #print "HTML Response: %s" %resp.read()


if __name__ == '__main__':
    submit_form()

