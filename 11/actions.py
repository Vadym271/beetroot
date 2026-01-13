import os
import json

# Change that if you don't want to enter data manually
__DEVELOPMENT_MODE__ = os.environ.get('DEVELOPMENT_MODE', False)


def add_contact(db_name):
    """Get user input, and create a contact if absent"""
    if __DEVELOPMENT_MODE__:
        phone_number = "123"
        name = "User1"
        city = "City1"
    else:
        phone_number = input('enter number, only digits ')
        name = input('enter name ')
        city = input('enter city ')

    # Assume only numbers are in phone_number
    clean_number = phone_number.strip()

    # Construct a line to be written into database
    datum = {'number': clean_number, 'name': name, 'city': city}

    # open database and parse it into json
    db = json.load(open(db_name))

    # append item to the contacts list
    db['contacts'].append(datum)

    # write `db` dictionary to the json database
    json.dump(db, open(db_name, 'w'))

def search(db_name):
    db = json.load(open(db_name))
    options = ['name', 'city', 'number']
    users_option = input('you wanna search by firstname, secondname, city or number:')
    while users_option not in options:
        users_option = input('you wanna search by firstname, secondname, city or number:')
        print('there is no such option. please choose one of the options listed below')

    phonebook = db.get('contacts')

    # search by firstname or secondname
    if users_option == 'name':
        name = input('enter firstname or secondname')
        check = False
        for i in phonebook:
            names = [j.lower() for j in i.get('name').split()]
            if name.lower() in names:
                print(i)
                check = True
        if not check:
            print('no person with such name')
    # search by firstname or secondname
    if users_option == 'city':
        city = input('enter a city:')
        check = False
        for i in phonebook:
            cities = [j.lower() for j in i.get('city').split()]
            if city.lower() in cities:
                print(i)
                check = True
        if not check:
            print('you do not know anyone in this city(')

    if users_option == 'number':
        number = input('enter a number:')
        while number.isdigit() == False:
            print('your input should only contain digits')
            number = input('enter a number:')
        check = False
        for i in phonebook:
            numbers = [j for j in i.get('number')]
            if number in numbers:
                print(i)
                check = True
        if not check:
            print('you do not have anyone with this number')


# updating contact's info
def update(db_name):
    db = json.load(open(db_name))
    options = ['name', 'city', 'number']
    users_option = input('you wanna update name, city or number?  ')
    phonebook = db.get('contacts')
    check = False
    if users_option == 'name':
        oldname = input('enter old contacts name')
        newname = input('enter new contacts name')
        for i in range(len(phonebook)):
            if phonebook[i]['name'] == oldname:
                check = True
                phonebook[i]['name'] = newname
                new_info = phonebook[i]
        if not check:
            print('no one here with such name')

    # here we will delete previous contact and add a new one

# function to delete a contact
def delete(db_name):
    db = json.load(open(db_name))
    options = ['name', 'city', 'number']
    users_option = input('you wanna update name, city or number?  ')
    phonebook = db.get('contacts')









if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    add_contact(DEFAULT_DATABASE_NAME)