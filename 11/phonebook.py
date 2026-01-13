"""Phonebook application;
Functionality:
    - Add data into database
    - Delete data from database by id
    - Find contact by:
        - name
        - phone number
    - Update contact
    - List all contacts

Data format:
    - id
    - phone number
    - name
    - city

DATABASE_FORMAT_EXAMPLE:
{
  "contacts": [
      {
          "phone_number": 123,
          "name": "",
          "city": ""
      },
    ]
}
"""
import json
import os.path

from actions import add_contact, search, update
"""
from edit_module import edit_contact
from find_module import find_contact
from delete_module import delete_contact
from list_module import list_contact
"""

DEFAULT_DATABASE_NAME = 'phonebook.json'


def validate_user_input(data):
    clean_data = data.strip()
    if not clean_data.isnumeric():
        raise ValueError('Use numbers to enter action')
    action_number = int(clean_data)
    if action_number not in [1, 2, 3, 4, 5]:
        raise ValueError('Action should be one off ...')
    return action_number

AVAILABLE_FUNCTIONAL_INFO = """\n
This is a phone book application.
Available options are:
    1) add
    2) search
    3) update
    4) delete
    ---
    5) exit
your contacts.
"""




def ensure_database(name=DEFAULT_DATABASE_NAME):
    if not os.path.exists(name):
        empty_db = {'contacts': []}
        json.dump(empty_db, open(name, 'w'))


if __name__ == '__main__':
    ensure_database()
    print(AVAILABLE_FUNCTIONAL_INFO)
    try:
        user_input = input("enter number")
        action_number = validate_user_input(user_input)
        if action_number == 1:
            add_contact(DEFAULT_DATABASE_NAME)
        if action_number == 2:
            search(DEFAULT_DATABASE_NAME)
        if action_number == 3:
            update(DEFAULT_DATABASE_NAME)
    except KeyboardInterrupt:
        print('\nExiting')
