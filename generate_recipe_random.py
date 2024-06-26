# Name: Brian Swanson
# Institution: Oregon State University
# Quarter: Spring 2024
# Class: CS 361
# Assignment: Portfolio Project

"""
This program queries ChatGPT to generate a random recipe for the user.
"""

import os
from openai import OpenAI
import zmq
from dotenv import load_dotenv

load_dotenv()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:2222")

print("generate_recipe_random is now online")

while True:
    message = socket.recv()
    print(f"received {message}")

    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are providing a simple recipe with no greeting"},
        {"role": "user", "content": f"provide a random recipe which includes a title and ingredient list and procedure and no formatting characters. Do not have any text before the title of the recipe"}
      ]
    )

    response = completion.choices[0].message.content

    socket.send_string(response)