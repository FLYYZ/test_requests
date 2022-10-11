import json

import requests
import logging
import pytest

class TestRequest():
    logging.basicConfig(level=logging.INFO)

    def test_get(self):
        r = requests.get('https://testerhome.com/api/v3/topics.json?limit=3')
        # logging.INFO(r)
        # logging.INFO(r.text)
        # logging.INFO(json.dumps(r.json()))
        print(r)
        print(r.text)
        print(r.json())
        print(json.dumps(r.json(),indent = 2))



