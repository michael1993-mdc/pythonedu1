# User management
#import json and hashlib

import json
import hashlib

def register_user(username, password):
    """
    Registers a new user by storing their username and hashed password in a JSON file.
    Args:
        username (str): The username of the user to register.
        password (str): The password of the user to register.
    Returns:
        bool: True if the user was successfully registered, False if the username already exists.
    Raises:
        FileNotFoundError: If the JSON file does not exist, it will be created.
    Notes:
        - The function hashes the password using SHA-256 before storing it.
        - If the JSON file does not exist, it initializes an empty dictionary to store users.
        - If the username already exists in the JSON file, registration will fail.
        - Successfully registered users are saved in the 'user.json' file.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    #create an exception for when looking into json file
    #the exception should allow to create molre users

    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    #figure out if the user already has an account
    if username in users:
        print("This Username already exists.")
        return False
    
    #Create a way to Save a new account to your json file
    users[username] = {'password': hashed_password}
    with open('user.json', 'w') as file:
        json.dump(users, file)

     #print that the user has succesfully registered
    print(f"User '{username}' registered successfully, congrats mate.")
    return True

#now we have to define the login user, after they registered.
def login_user(username, password):

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    #Use json file to look up registered users tomatch login users
    #use filenotfounderror to inform user they have not registered
    try:
        with open('user.json', 'r') as file:
            users =json.load(file)
    except FileNotFoundError:
        print("Not yet registered, please register.")
        return False
    
    #now Authenticate user. Give them some pleasantries if they are already registered
    if username in users and users[username]['password'] == hashed_password:
        print(f"Greetings! {username}")
        return True
    else:
        print("Incorrect username or password, try again or resgister.")
        return False
    
#Ensure that the inputs are valid
def valid_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input empty, please input!")

#tests
if __name__ == "__main__":
    print("Welcome to the finest banking app in the business!")
    options = input("Select from either option: [Register/Login]: ").strip().lower()
    
    if options == "register":
        username = valid_input("Input username: ")
        password = valid_input("Input password: ")
        register_user(username, password)
    elif options == "login":
        username = valid_input("Input username: ")
        password = valid_input("Input password: ")
        login_user(username, password)
    else:
        print("There are only two options, 'Register' or 'Login'.")
