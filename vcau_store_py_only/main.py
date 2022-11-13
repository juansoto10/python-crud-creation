import sys
import os
import time
import csv


CLIENTS_TABLE = '.clients.csv'
CLIENTS_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENTS_TABLE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=CLIENTS_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table = f'{CLIENTS_TABLE}.tmp'
    with open(tmp_table, mode='w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENTS_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENTS_TABLE)
    os.rename(tmp_table, CLIENTS_TABLE)


def _get_client_field(field_name):
    """
    Obtains any field of the client's data and returns it capitalized.
    """
    field = input(f'\n\tWhat is the client\'s {field_name}? => ').title().strip()

    while not field:
        print(f'\n\tYou have not entered the {field_name}. Try again or type <Exit> to close the program.')
        field = input(f'\n\tWhat is the client\'s {field_name}? => ').title().strip()

    if field == 'Exit':
        print('\n\tGood Bye!')
        time.sleep(1)
        sys.exit()

    return field


def search_client(client_name):
    """
    Receives the name of a client as an argument and verifies if it is in the clients list or not.

    Returns True or False depending on the case.
    """
    for client in clients:
        if client['name'] == client_name:
            return True
        else:
            continue


def _client_not_found(client_name):
    """
    Returns a message when a client is not found in the clients list.
    """
    print(f"\n\tClient {client_name} is not in clients list.\n")


def create_client(client):
    """
    Adds a client to the clients list.
    """
    # Specifying that the global variable -clients- is going to be used in this function
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('\n\tClient is already in clients list.')


def list_clients():
    """
    Prints the clients list
    """
    print('\n\tCurrent clients list:\n')
    print('\t  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION  ')
    print(f'\t{"-" * 50}')

    for idx, client in enumerate(clients):
        print(f"\t{idx} | {client['name']} | {client['company']} | {client['email']} | {client['position']}")


def search_index(name):
    for client in clients:
        if client['name'] == name:
            index = clients.index(client)
            return index


def update_client(client_name):
    """
    Updates the information of a client.
    """
    global clients

    index = search_index(client_name)

    print('\n\tWhat is the client\'s data you want to modify?')
    data_to_update = input('\n\t[N]ame | [C]ompany | [E]mail | [P]osition | [A]ll | [Exit] => ').title().strip()

    match data_to_update:
        case 'N':
            updated_name = _get_client_field('name')
            clients[index]['name'] = updated_name
        case 'C':
            updated_company = _get_client_field('company')
            clients[index]['company'] = updated_company
        case 'E':
            updated_email = _get_client_field('email').lower()
            clients[index]['email'] = updated_email
        case 'P':
            updated_position = _get_client_field('position')
            clients[index]['position'] = updated_position
        case 'A':
            client = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email').lower(),
                'position': _get_client_field('position'),
            }

            clients[index] = client
            print(clients)
        case 'Exit':
            print('\n\tGood Bye!')
            time.sleep(1)
            sys.exit()
        case _:
            print('\n\tPlease enter a valid command.')
            update_client(client_name)


def delete_client(client_name):
    """
    Deletes a client from the clients list.
    """
    global clients

    index = search_index(client_name)
    return clients.pop(index)


def exit_question():
    answer = input('\n\tDo you want to do something else? (y/n) => ').lower().strip()
    time.sleep(0.4)

    if answer == 'y':
        _print_options()
    elif answer == 'n':
        print('\n\tGood Bye!\n')
        time.sleep(1)
        sys.exit()
    else:
        print('\n\tInvalid command.')
        exit_question()


def _print_options():
    print(f"\n{'*'*60}")
    print('\n\tWhat would you like to do this time?')
    print('\n\t\t[C]reate client')
    print('\n\t\t[R]ead clients list')
    print('\n\t\t[U]pdate client')
    print('\n\t\t[D]elete client')
    print('\n\t\t[S]earch client')
    print('\n\t\t[E]xit')
    print('\n\tSelect an option from above C/R/U/D/S/E:\n')
    print('\tYou can type <Exit> at any time to close the program.\n')

    command = input('\t=> ').upper().strip()
    command_actions(command)


def _print_welcome():
    """
    Prints a welcome message
    """
    print(f'\n{"*" * 60}')
    print(f'\n\t\tWELCOME TO VCAU SHOP')
    print(f'\n{"*" * 60}')
    print('\n\tWhat would you like to do this time?')
    print('\n\t\t[C]reate client')
    print('\n\t\t[R]ead clients list')
    print('\n\t\t[U]pdate client')
    print('\n\t\t[D]elete client')
    print('\n\t\t[S]earch client')
    print('\n\t\t[E]xit')
    print('\n\tSelect an option from above C/R/U/D/S/E:\n')
    print('\tYou can type <Exit> at any time to close the program.\n')


def command_actions(command):
    """
    Executes the different actions of the program depending on the command provided
    """
    if command == 'C':
        client_name = _get_client_field('name')

        if search_client(client_name):
            print(f'\n\tThe client {client_name} is already in the clients list.')
            time.sleep(1)
            run()
        else:
            client = {
                'name': client_name,
                'company': _get_client_field('company'),
                'email': _get_client_field('email').lower(),
                'position': _get_client_field('position'),
            }

            create_client(client)
            print(f'\n\t>>> Client created successfully.')

        time.sleep(1)
        _save_clients_to_storage()
        exit_question()
    elif command == 'R':
        list_clients()
        time.sleep(1)
        exit_question()
    elif command == 'U':
        client_name = _get_client_field('name')

        if search_client(client_name):
            update_client(client_name)
            print(f'\n\t>>> The client\'s data was updated.')
        else:
            _client_not_found(client_name)
            time.sleep(1)
            run()

        time.sleep(1)
        _save_clients_to_storage()
        exit_question()
    elif command == 'D':
        client_name = _get_client_field('name')

        if search_client(client_name):
            delete_client(client_name)
            print(f'\n\t>>> The client {client_name} was deleted.')
        else:
            _client_not_found(client_name)

        time.sleep(1)
        _save_clients_to_storage()
        exit_question()
    elif command == 'S':
        client_name = _get_client_field('name')

        if search_client(client_name):
            print(f"\n\tThe client {client_name} is in the clients list.")
        else:
            _client_not_found(client_name)

        time.sleep(1)
        exit_question()
    elif command == 'E' or command == 'EXIT':
        print('\n\tGood Bye!\n')
        time.sleep(1)
        sys.exit()
    else:
        print('\n\tInvalid command. Try again.\n')
        time.sleep(1.2)
        run()

    _save_clients_to_storage()


def run():
    _initialize_clients_from_storage()

    _print_welcome()
    time.sleep(0.5)

    command = input('\t=> ').upper().strip()

    command_actions(command)

    exit_question()


if __name__ == '__main__':
    run()
