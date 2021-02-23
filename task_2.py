import json
import os


def read(path):
    """This function for opens json file"""
    with open(path, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
    return json_file


def instruction():
    """This function prints instructions"""
    print('To open an object or get the value of a parameter, enter its name.')
    print('If you want to end session enter "command exit".\n\n')


def json_navigation(file):
    """This function navigates on a .json file"""

    curr_directory = file

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        instruction()

        print('Directory objects:')
        if isinstance(curr_directory, list):
            counter = 1
            for element in curr_directory:
                if isinstance(element, dict):
                    print(f"* dict {counter}")
                elif isinstance(element, list):
                    print(f"* list {counter}")
                else:
                    print("* " + str(element))
                counter += 1

        elif isinstance(curr_directory, dict):
            for element in curr_directory.keys():
                print("* " + str(element))

        else:
            print(f'Value: {curr_directory}')

        command = input('\nCommand: ')

        if command == 'command exit':
            exit(0)

        elif isinstance(curr_directory, dict) or isinstance(curr_directory, list):
            if isinstance(curr_directory, dict) and command in curr_directory.keys():
                curr_directory = curr_directory[command]
            elif len(command.split()) == 2 and (command.startswith('list') or command.startswith('dict')) \
                    and command.split()[1].isdigit:
                if 0 < int(command.split()[1]) < counter:
                    curr_directory = curr_directory[int(
                        command.split()[1]) - 1]
        else:
            print('No such object.')


def input_path():
    """This function is for user to input path"""

    path = input('Enter the path to the json file you want to open: ')
    if not os.path.isfile(path):
        print('No such file.')
    json_navigation(read(path))


input_path()
