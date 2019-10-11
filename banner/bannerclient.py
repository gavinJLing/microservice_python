#!/usr/local/bin/python3

import requests
import json

# Get a banner
r = requests.get("http://localhost:5000/banner/helloworld?font=thick",  headers={"password":"stumpylongnose"})


print(r.text)
