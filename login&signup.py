import json
import re
import bcrypt
import uuid
import os

def clear():
    os.system('cls||clear')
    
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

def validate_email(email):
    regex = r'[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}'
    return re.match(regex, email) is not None

def game(users):
    
    while True:
        choice = input("pleas select one of the options:\nA)NEW GAME\nB)Continue previous game\nC)WINNER CHART\nD)GAMES DATA\nF)EXIT\n")
        
        if choice.upper() == 'A':
          print("Starting a new game...") 
          new_game(users) 
        elif choice == 'B':
          print("Continuing previous game...")
        elif choice == 'C':
          print("Displaying winner chart...") 
        elif choice == 'D':
          print("loading data of the game...")
        elif choice == 'F':  
          print("Exiting menu.")  
          break
        else:
            print("Error\nPleas try again.")


def new_game(users):
    username =input("playr2 username: ")
    password=input("player2 password: ")

    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]:
            print("ENJOY THE GAME")
            
        else:
            print("Incorrect password")
    else:
        print("your username does not exist\nPleas try again")     


def login(users):
    username = input("username: ")
    password = input("password: ")
    email = input("email: ")

    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]['email'] == email:
            print("login succsseful\n Enjoy the game")
            game(users)
        else:
            print("Incorrect email or password")
    else:
        print("your username does not exist\nPleas try again")



def signup(users):
    username = input("username: ")
    email = input("email: ")
    password = input("password: ")

    if username in users:
        print("username is already exist\nPlease try again.")
        return main
    
    if not validate_email(email):
        print("Email is not valid")
        return

    for user in users.values():
        if user['email'] == email:
            print("Email is already exist\nPlease try again.")
            return
    username_id= str(uuid.uuid4())
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users[username] = {'id':username_id,'email': email, 'password': hashed_password}
    save_users(users)
    print("Sign Up successful!")
    game(users)

def main():
    clear()
    users = load_users()
    
    while True:
        clear()
        choice = input("pleas select one of the options: 0)EXIT 1)Login 2)Signup ")
        clear()
        if choice == '1':
            clear()
            login(users)
        elif choice == '2':
            clear()
            signup(users)
        elif choice == '0':
            break
        else:
            clear()
            print("Error\nPleas try again.")

main()

