
PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What\'s your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('Incorrect password')

    return wrapper


@password_required
def needs_password():
    print('The password is correct!')


# Otra forma de declarar decoradores: Cuando la función recibe parámetros en sí misma

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper
    

@upper
def say_my_name(name):
    return f'Hi, {name}'


if __name__ == '__main__':
    # needs_password()

    print(say_my_name('Juan'))

