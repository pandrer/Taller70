from typing import List


def is_name(name: str) -> bool:
    if len(name) < 6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
        return False
    elif len(name) > 12:
        print('El nombre de usuario no puede contener más de 12 caracteres')
        return False
    elif name.isalpha():
        return True
    else:
        print('El nombre de usuario puede contener solo letras y números')
        return False


def is_password(password: str) -> bool:
    special_characteres: List[str] = ['$', '@', '#', '%']
    val = True

    if len(password) < 8:
        print('el password debe ser contener mas de 8 caracteres')
        val = False

    if not any(char.isdigit() for char in password):
        print('el password debe contener al menos numero')
        val = False

    if not any(char.isupper() for char in password):
        print('el password debe contener al menos una letra mayuscula')
        val = False

    if not any(char.islower() for char in password):
        print('el password debe contener al menos una letra minuscula')
        val = False

    if not any(char in special_characteres for char in password):
        print('el password debe contener al menos uno de estos caracteres $@#')
        val = False

    return val
