# Name: Brian Swanson
# Institution: Oregon State University
# Quarter: Spring 2024
# Class: CS 361
# Assignment: Portfolio Project

"""
This microservice is able to query the recipe folder present in this program and returns a list of titles.
"""

import zmq
import os
import json

print("Recipe displayer is now online")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:3333")

while True:
    message = socket.recv()
    print(f"received {message}")

    directory = "Recipes"

    recipe_list = []
    for filename in os.listdir(directory):
        recipe_list.append(filename)

    recipe_json = json.dumps(recipe_list)
    socket.send_json(recipe_json)
