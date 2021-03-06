# Native Imports
from os import environ
import logging
from json import dumps

# 3rd-Party Imports
from maapi.mati import MAV4

logging.basicConfig(filename=None, encoding='utf-8', level=logging.WARNING)

username = environ['MAV4_USER']
password = environ['MAV4_PASS']

if __name__ == "__main__":
    client = MAV4(username, password)
    items = client.get_items("actor", limit=5000)
    print(dumps(items, indent=4))
