import json
import re
import bcrypt
import uuid
import os
from termcolor import colored
import time


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
        choice = input(colored("pleas select one of the options:\nA)NEW GAME\nB)Continue previous game\nC)WINNER CHART\nD)GAMES DATA\nF)EXIT\n"))
        clear()
        if choice.upper() == 'A':
          print(colored("Starting a new game...","blue")) 
          new_game(users) 
        elif choice.upper() == 'B':
          print(colored("Continuing previous game...","blue"))
        elif choice.upper() == 'C':
          print(colored("Displaying winner chart...","blue")) 
        elif choice.upper() == 'D':
          print(colored("loading data of the game...","blue"))
        elif choice.upper() == 'F':  
          print(colored("Exiting menu.","red"))  
          break
        else:
            print(colored("Error\nPleas try again.","red"))


def new_game(users):
    username =input(colored("playr2 username: ","white","on_dark_grey"))
    clear()
    password=input(colored("player2 password: ","white","on_dark_grey"))
    clear()

    username =input("player 2 username: ")
    password=input("player 2 password: ")

    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]:
            print(colored("ENJOY THE GAME","light_yellow"))
            
        else:
            print(colored("Incorrect password","red"))
    else:
        print(colored("your username does not exist\nSIGN UP IF YOU DID NOT\nSIGN UP: ","light_red"))      
    signup(users)

    

def login(users):
    username = input(colored("username: ","white","on_dark_grey"))
    if username=="0":
        exit()
    clear()        
    password = input(colored("password: ","white","on_dark_grey"))
    if password=="0":
        exit()
    clear()    
    email = input(colored("email: ","white","on_dark_gray"))
    if email == "0":
        exit()
    clear()    

    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]['email'] == email:
            print(colored("login succsseful\n Enjoy the game","light_yellow"))
            game(users)
        else:
            print(colored("Incorrect email or password","light_red"))
            time.sleep(1)
            clear()
            game(users)
            
    else:
        print(colored("your username does not exist\nPleas try again","light_red"))



def signup(users):
    username = input(colored("username: ","white","on_dark_grey"))
    if username== "0":
        exit()
    clear()    
    email = input(colored("email: ","white","on_dark_grey0"))
    if email=="0":
        exit()
    clear()    
    password = input(colored("password: ","white","on_dark_grey"))
    if password== "0":
        exit()
    clear()    

    if username in users:

        print(colored("username is already exist\nPlease try again.","light_red"))
        return main
    
    if not validate_email(email):
        print(colored("Email is not valid","light_red"))
        return

    for user in users.values():
        if user['email'] == email:
            print(colored("Email is already exist\nPlease try again.","blue"))
            return
    username_id= str(uuid.uuid4())
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users[username] = {'id':username_id,'email': email, 'password': hashed_password}
    save_users(users)
    print(colored("Sign Up successful!","yellow","on_dark_grey"))
    game(users)

def main():
    clear()
    users = load_users()
    
    while True:
        clear()

        choice = input(colored("pleas select one of the options: 0)EXIT 1)Login 2)Signup ","black","on_dark_grey"))
        clear()
        if choice == '1':
            
            login(users)
        elif choice == '2':
            
            signup(users)
        elif choice == '0':
            break
        else:
        
            print(colored("Error\nPleas try again.","red"))

main()



