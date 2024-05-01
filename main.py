# Name: Brian Swanson
# Institution: Oregon State University
# Quarter: Spring 2024
# Class: CS 361
# Assignment: Portfolio Project

from openai import OpenAI
import zmq

def mainMenu():
    """
    This represents the main menu that the user interacts with in the command line.
    """
    print(f"Hello, please select an option:\n\n"
          f"1. Get a suggested recipe with your ingredients\n"
          f"2. Receive a random recipe\n"
          f"3. List the recipe log\n"
          f"4. Print a specific recipe from the recipe log\n"
          f"5. Receive a grocery list based on a recipe you choose\n"
          f"6. Exit the program\n")
    return

def communicator(service_socket, service_command = None):
    """
    A function that runs after the user selects a service. The function will use ZeroMQ to communicate with the service.
    :param service_socket: the socket defined for the service based on the main program
    :param service_command: an optional command that this function will send to some services
    :return: a string manipulated and prepared for the user
    """
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:" + str(service_socket))

    if service_command is None:
        socket.send_string("run")
    else:
        socket.send_string(service_command)

    message = socket.recv()

    return message


def generate_recipe_with_ingredients():
    print('You selected: "Get a suggested recipe with your ingredients." Please enter your ingredients one by one'
          'separated by commas and we will suggest you a recipe.\n'
          '(Please note that misspelled words or ingredients you do not have may yield unsatisfactory results.\n'
          'Example: onion, bell pepper, steak')
    service_command = input("Enter your ingredients here: ")

    try:
        user_confirmation = int(input(f"You have entered: {service_command}. Are you sure these are correct?\n"
                                      f"Enter 1 if yes or 2 if you would like to re-enter your ingredients: "))
    except ValueError:
        print("Input not recognized.")
        user_confirmation = 2

    while user_confirmation != 1:
        service_command = input("Enter your ingredients here: ")

        try:
            user_confirmation = int(input(f"You have entered: {service_command}. Are you sure these are correct?\n"
                                          f"Enter 1 if yes or 2 if you would like to re-enter your ingredients: "))
        except ValueError:
            print("Input not recognized.")

    print(f"Generating a recipe with {service_command}!")
    return service_command


user_input = None

while user_input != 6:
    mainMenu()
    try:
        user_input = int(input("Which option would you like to choose? "))
    except ValueError:
        print("Input not recognized, please review the options in the main menu and try again.\n")

    if user_input == 1:
        # Generate a recipe using the user's ingredients
        service_command = generate_recipe_with_ingredients()
        service_socket = 1111
        response = communicator(service_socket, service_command)
        print(response)

    elif user_input == 2:
        # Receive a random recipe from chatGPT
        print('You selected: "Receive a random recipe."')

        service_socket = 2222
        pass

    elif user_input == 3:
        # Call a service to print the titles of recipes already generated
        print('You selected: "List the recipe log."')
        service_socket = 3333
        pass

    elif user_input == 4:
        # Call a service to search currently generated recipes
        print('You selected: "Print a specific recipe from the recipe log."')
        service_socket = 4444
        pass

    elif user_input == 5:
        # Call a service to search for an already generated recipe and print the ingredients
        print('You selected: "Receive a grocery list based on a recipe you choose."')
        service_socket = 5555
        pass

    elif user_input == 6:
        print("Exiting the program.")