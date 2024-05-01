import os
from openai import OpenAI
import zmq
from dotenv import load_dotenv

load_dotenv()

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
        {"role": "system", "content": "You are providing a simple recipe"},
        {"role": "user", "content": f"provide a recipe that uses {message} with no other text"}
      ]
    )

    response = completion.choices[0].message.content

    socket.send_string(response)