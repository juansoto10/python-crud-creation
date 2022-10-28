

clients = 'Maja, Kate, Emma, '


def _print_welcome():
    '''
    Prints a welcome message.
    '''
    print(f'\n{"*" * 50}')
    print(f'\n\t\tWELCOME TO VCAU SHOP')
    print(f'\n{"*" * 50}')
    print('\n\tWhat would you like to do today?')
    print('\n\t\t[C]reate client')
    print('\n\t\t[R]ead clients list')
    print('\n\t\t[U]pdate client')
    print('\n\t\t[D]elete client')
    print('\n\t\t[S]earch client')
    print('\n\tSelect an option from above C/R/U/D/S:\n')


def _get_client_name():
    '''
    Obtains the name of a client and returns it capitalized.
    '''
    return input('\tWhat is the client name? ').title()


def search_client(client_name):
    '''
    Receives the name of a client as an argument and verifies if it is in the clients list or not.
    
    Returns True or False depending on the case.
    '''
    global clients
    
    if client_name in clients:
        return True
    else:
        return False


def _client_not_found(client_name):
    '''
    Returns a message when a client is not found in the clients list.
    '''
    print(f'\tClient {client_name} is not in clients list\n')


def _add_comma():
    '''
    Adds a comma and a space to separate the substrings
    '''
    global clients
    
    clients += ', '


def create_client(client_name):
    '''
    Adds a client to the clients list.
    '''
    # Specifying that the global variable -clients- is going to be used in this function 
    global clients
    
    if search_client(client_name):
        print('\tClient is already in clients list\n')
    else:
        clients += client_name
        _add_comma()


def list_clients():
    '''
    Prints the clients list
    '''
    global clients
    
    print('\tCurrent clients list:')
    print(f'\t>>> {clients}\n')

 
def update_client(client_name):
    '''
    Updates the information of a client.
    '''
    global clients
    
    if search_client(client_name):
        updated_client_name = input('\tWhat is the updated client name? ').title()
        clients = clients.replace(client_name + ', ', updated_client_name + ', ')
    else:
        _client_not_found(client_name)
        
        
def delete_client(client_name):
    '''
    Deletes a client from the clients list.
    '''
    global clients
    
    if search_client(client_name):
        clients = clients.replace(client_name + ', ', '')
    else:
        _client_not_found(client_name)
 
    
def run():
    _print_welcome()

    command = input().upper()
    print('')

    if command == 'C':
        client_name = _get_client_name()
        print('')
        create_client(client_name)
        list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)
        print('')
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        print('')
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        print('')
        if search_client(client_name):
            print(f'\tThe client {client_name} is in the clients list\n')
        else:
            _client_not_found(client_name)
    else:
        print('\tInvalid command. Try again.\n')


if __name__ == '__main__':
    run()
        