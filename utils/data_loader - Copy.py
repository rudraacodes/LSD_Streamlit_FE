import json

def load_businesses():
    with open("data/businesses.json", "r") as file:
        return json.load(file)