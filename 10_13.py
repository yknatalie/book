import json

try:
    with open('number.json') as f:
        fav_number = json.load(f)
        print(f"I know your fav name! It's {fav_number}")
except FileNotFoundError:
    number = input("What's your fav namber? ")
    with open('number.json', 'w') as f:
        json.dump(number, f)


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    while username:
        name = input(f'Is your name {username}? ')
        if name == 'yes'.lower():
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
        break


greet_user()
