import uuid
import hashlib

# Завдання 2. Написати програму для реєстрації та авторизації користувача
# з таким функціоналом:
# отримання в інтерактивному режимі логіна і пароля користувача;
# верифікація пароля та його шифрування за алгоритмом, обраним алгоритмом
# шифрування;
# авторизація користувача за логіном і паролем.

print('--- Task 2 ---')


# Variable to define login.
username = ''
database = []


# Username encryption.
def get_hash_username(username):
    salt = uuid.uuid4().hex
    return hashlib.sha256(
        salt.encode() + username.encode()).hexdigest() + ':' + salt


# Verification username.
def check_username(hashed_username, user):
    username, salt = hashed_username.split(':')
    return username == hashlib.sha256(
        salt.encode() + user.encode()).hexdigest()


def create_username():
    global username
    username = input('Enter an username [not less than 5 symbols]: ')
    hashed_username = get_hash_username(username)

    if len(username) >= 5:
        print(f'Username "{username}" is now being checked...')

        # Verification username.
        old_username = input('\nPlease enter the username again to check: ')
        if old_username == username:
            print('Successfully!')
            print(f'Username has been encryption as: {hashed_username}')
            database.append(username)
        else:
            print('Username does not match. Try again!')
            create_username()
        print(f'Users database {database}')
    else:
        print('Username should be not less than 5 symbols.\n')
        create_username()


# Password encryption.
def get_hash_password(password):
    # uuid is used to generate a random number of the specified password
    salt = uuid.uuid4().hex
    return hashlib.sha256(
        salt.encode() + password.encode()).hexdigest() + ':' + salt


# Verification password.
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(
        salt.encode() + user_password.encode()).hexdigest()


# Enter password.
def create_password():
    password = input('\nEnter a password [not less than 5 symbols]: ')
    hashed_password = get_hash_password(password)

    if len(password) >= 5:
        print('Password is now being checked...')

        # Verification password.
        old_pass = input('\nPlease enter the password again to check: ')
        if old_pass == password:
            print('Successfully!')
            print(f'Password has been encryption as: {hashed_password}')
            database.append(password)
            print('User database:', database)
            print('\nYou have been registered!')
        else:
            print('Password do not match. Try again!')
            create_password()
    else:
        print('Password should be not less than 5 symbols.')
        create_password()


def main():
    create_username()
    create_password()


if __name__ == "__main__":
    main()
