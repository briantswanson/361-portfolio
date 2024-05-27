
import zmq
import re


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")


while True:

    byte_str = socket.recv()

    string_decoded = byte_str.decode("utf-8")
    title_line = string_decoded.split(('\n', 1)[0])
    title_line = title_line[0]

    # extract the title from the string
    print(title_line)
    title = str(title_line) + ".txt"
    file_name = title # the filename will just be the title of the recipe


    # open the text file for writing
    with open("Recipes/" + file_name, 'w') as f:
        f.write(string_decoded)

    #  Send reply back to client
    socket.send(b"file saved successfully")


