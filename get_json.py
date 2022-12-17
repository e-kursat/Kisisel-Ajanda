import json


def get_data():
    try:
        with open('accounts.json', 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        with open('accounts.json', 'w') as file:
            file.write("{}")

        with open('accounts.json', 'r') as file:
            data = json.load(file)

    return data
