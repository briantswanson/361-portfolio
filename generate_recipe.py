# Name: Brian Swanson
# Institution: Oregon State University
# Quarter: Spring 2024
# Class: CS 361
# Assignment: Portfolio Project

"""
This program queries ChatGPT to generate a recipe for the user based on their ingredients.
"""

import os
from openai import OpenAI
import zmq
from dotenv import load_dotenv

load_dotenv()

print("generate_recipe is now online")


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1111")

while True:
    message = socket.recv()
    print(f"received {message}")

    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are providing a simple recipe with no greeting"},
        {"role": "user", "content": f"provide a recipe that uses {message} which includes a title, ingredient list and procedure with no formatting characters. Do not have any text before the title of the recipe"}
      ]
    )

    response = completion.choices[0].message.content

    socket.send_string(response)