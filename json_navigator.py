"""
DARIA SHABATSKA
LAB 3 TASK 2
GitHub: https://github.com/S-Daria/LAB3_TASK2.git
"""

import json


def json_decoding(path: str) -> dict:
    """
    get json file
    return dict object with contents of the file
    """
    with open(path, 'r', encoding='utf-8') as file:
        decoded_kved = json.load(file)
        return decoded_kved

path = "friends_list_Obama.json"
decoded_object = json_decoding(path)

# print(decoded_object.keys())
# print(decoded_object['users'][0].keys())

def choose_key(data_dict: dict) -> object:
    """
    get dictionary
    let the user choose the key 
    return choice
    """
    print('******************************************************')
    print(f'please, choose a key from presented below:')
    for key in data_dict.keys():
        print(key)
    chosen_key = input('enter your choice: ')
    while chosen_key not in data_dict.keys():
        print('invalid key, please, choose again')
        chosen_key = input('*** enter your choice: ')
    else:
        return chosen_key


def choose_index(data_list: list) -> int:
    """
    get list
    let the user choose index of the item
    or whether he want to display all items
    return choice
    or return False if user want all elements to be shown
    """
    print('******************************************************')
    print(f'the next object is a list\nplease, choose an index from 0 to \
{len(data_list) - 1} of an element you want to be displayed or type "-1" to display each:')
    chosen_index = input('enter your choice: ')
    while chosen_index not in [str(i) for i in range(-1, len(data_list))]:
        print('invalid index, please, choose again')
        chosen_index = input('*** enter your choice: ')
    else:
        # if chosen_index == '-1':
        #     return False
        return int(chosen_index)

# print(print_keys(decoded_object))

# choose_index(decoded_object['users'])

def type_check(current_object):
    if isinstance(current_object, dict):
        return choose_key(current_object)
    elif isinstance(current_object, list):
        return choose_index(current_object)
    else:
        return False


def navigator(json_dict: dict):
    """
    get json file as dictionary object 
    navigates through dict be interacting with user
    return None
    """
    current_object = json_dict
    chosen = type_check(current_object)
    while str(chosen) == '0' or chosen:
        current_object = current_object[chosen]
        chosen = type_check(current_object)
    print('******************************************************')
    print(current_object)

navigator(decoded_object)
