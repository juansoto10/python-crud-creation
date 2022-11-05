import sys
import time


clients = [
    {
        'name': 'Maja',
        'company': 'Google',
        'email': 'maja@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Kate',
        'company': 'Facebook',
        'email': 'kate@meta.com',
        'position': 'Data engineer',
    },
    {
        'name': 'Emma',
        'company': 'Disney',
        'email': 'emma@disney.com',
        'position': 'Content producer',
    }
]


def _print_welcome():
    """
    Prints a welcome message.
    """
    print(f'\n{"*" * 50}')
    print(f'\n\t\tWELCOME TO VCAU SHOP')
    print(f'\n{"*" * 50}')
    print('\n\tWhat would you like to do this time?')
    print('\n\t\t[C]reate client')
    print('\n\t\t[R]ead clients list')
    print('\n\t\t[U]pdate client')
    print('\n\t\t[D]elete client')
    print('\n\t\t[S]earch client')
    print('\n\t\t[E]xit')
    print('\n\tSelect an option from above C/R/U/D/S/E:\n')
    print('\tYou can type <Exit> at any time to close the program.\n')


def _get_client_field(field_name):
    field = input(f'\n\tWhat is the client\'s {field_name}? ').title().strip()

    while not field:
        print(f'\n\tYou have not entered the {field_name}. Try again or type <Exit> to close the program')
        field = input(f'\n\tWhat is the client\'s {field_name}? ').title().strip()

    return field


# def _get_client_name():
    # """
    # Obtains the name of a client and returns it capitalized.
    # """
    # client_name = None
    # client_name = input('\n\tWhat is the client\'s name? ').title().strip()
    
    # while not client_name:
        # print('\n\tYou have not entered the client\'s name. Please enter a name or type <Exit> to close the program')
        # client_name = input('\n\tWhat is the client\'s name? ').title().strip()
    
    # if client_name == 'Exit':
        # print('\n\tGood Bye!')
        # time.sleep(1)
        # sys.exit()
    
    # return client_name


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
    print(f"\n\tClient {client_name} is not in clients list\n")


def create_client(client):
    """
    Adds a client to the clients list.
    """
    # Specifying that the global variable -clients- is going to be used in this function 
    global clients
    
    if search_client(client['name']):
        print('\n\tClient is already in clients list\n')
    else:
        clients.append(client)


def list_clients():
    """
    Prints the clients list
    """
    print('\n\tCurrent clients list:\n')

    for idx, client in enumerate(clients):
        print(f"\t{idx}: {client['name']}")


def update_client(client):
    """
    Updates the information of a client.
    """
    global clients
    
    if search_client(client['name']):
        updated_client_name = input('\n\tWhat is the updated client\'s name? ').title().strip()
        
        while not updated_client_name:
            print('\n\tYou have not entered the updated client\'s name.')
            print('\tPlease enter a name or type <Exit> to close the program.')
            updated_client_name = input('\n\tWhat is the updated client\'s name? ').title().strip()
        
        if updated_client_name == 'Exit':
            print('\n\tGood Bye!')
            sys.exit()
        
        index = clients.index(client)
        clients[index] = updated_client_name
    else:
        _client_not_found(client['name'])
        
        
def delete_client(client):
    """
    Deletes a client from the clients list.
    """
    global clients
    
    if search_client(client['name']):
        clients.remove(client)
    else:
        _client_not_found(client['name'])
 
    
def run():
    _print_welcome()

    command = input().upper().strip()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_name = _get_client_field('name')
        update_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_field('name')
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')

        if search_client(client_name):
            print(f"\n\tThe client {client_name} is in the clients list\n")
        else:
            _client_not_found(client_name)
    elif command == 'E' or command == 'EXIT':
        print('\n\tGood Bye!\n')
        time.sleep(1)
        sys.exit()
    else:
        print('\n\tInvalid command. Try again.\n')
        time.sleep(1.2)
        run()


if __name__ == '__main__':
    run()
