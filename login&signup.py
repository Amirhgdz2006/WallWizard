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
        choice = input(colored("pleas select one of the options:\n\nA) NEW GAME\n\nB) Continue previous game\n\nC) WINNER CHART\n\nD) GAMES DATA\n\nF) EXIT\n\n","black"))
        clear()
        if choice.upper() == 'A':
          print(colored("Starting a new game...","blue")) 
          new_game(users) 
        elif choice.upper() == 'B':
          print(colored("Continuing previous game...\n","blue"))
          
        elif choice.upper() == 'C':
          print(colored("Displaying winner chart...\n","blue"))
          
        elif choice.upper() == 'D':
          print(colored("loading data of the game...\n","blue"))
          
        elif choice.upper() == 'F':  
          print(colored("Exiting menu.","red"))  
          exit()
          clear()
        else:
            print(colored("Error\nPleas try again.\n","red"))


def new_game(users):
    username =input(colored("player 2 username: ","black"))

    def check_username(username):
        if username=="0":
            exit()

        elif len(username) <= 2 :
            print(colored("your username does not valid\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            username = input(colored("player 2 username: ","black"))
            check_username(username)

        elif username not in users:
            print(colored("your username does not exist\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            username = input(colored("player 2 username: ","black"))
            check_username(username)

    check_username(username)
    clear()
    password=input(colored("player 2 password: ","black"))

    def check_password(password):

        if password=="0":
            exit()

        elif len(password) < 8 :
            print(colored("your password does not valid\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            password = input(colored("player 2 password: ","black"))
            check_password(password)
    check_password(password)
    clear()

    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]:
            print(colored("ENJOY THE GAME","light_yellow"))
            
        else:
            print(colored("Incorrect password","red"))


def login(users):
    username = input(colored("username:\n","black"))
    def check_username(username):
        if username=="0":
            exit()

        elif len(username)<= 2 :
             print(colored("your username does not valid\nPleas try again","light_red"))
             time.sleep(1)
             clear()
             username = input(colored("username:\n","black"))
             check_username(username)

        elif username not in users:
            print(colored("your username does not exist\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            username = input(colored("username:\n","black"))
            check_username(username)

    check_username(username)
    clear()

    password = input(colored("password:\n","black"))
    
    def check_password(password):

        if password=="0":
            exit()

        elif len(password)< 8 :
            print(colored("your password does not valid\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            password = input(colored("password: ","black"))
            check_password(password)
        
    check_password(password)
    clear()
    
    email = input(colored("email:\n","black"))
    def check_email(email):
    
          if email=="0":
            exit()
          elif validate_email(email) == False:
            print(colored("Email is not valid please enter valid email","light_red"))
            time.sleep(1)
            clear()
            email = input(colored("email:\n","black"))
            check_email(email)
          
    check_email(email)
    clear()   
    while True:
     if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]['email'] == email:
            print(colored("login succsseful\nEnjoy the game\n","light_yellow"))
            game(users)

        else:

            print(colored("Incorrect email or password","light_red"))
            time.sleep(1)
            clear()
            email = input(colored("email:\n","black"))
            check_email(email)
     check_email(email)

    

def signup(users):
    username = input(colored("username:\n","black"))

    def check_username(username):
        if username=="0":
            exit()

        elif len(username)<= 2 :
             print(colored("your username does not valid\nPleas try again","light_red"))
             time.sleep(1)
             clear()
             username = input(colored("username:\n","black"))
             check_username(username)

        elif username in users:
            print(colored("your username is already exist\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            username = input(colored("username:\n","black"))
            check_username(username)

    check_username(username)
    clear()

    password = input(colored("password:\n","black"))
    
    def check_password(password):

        if password=="0":
            exit()

        elif len(password)< 8 :
            print(colored("your password does not valid\nPleas try again","light_red"))
            time.sleep(1)
            clear()
            password = input(colored("password: ","black"))
            check_password(password)
    check_password(password)
    clear()

    email = input(colored("email:\n","black"))
    def check_email(email):
        if email=="0":
            exit()
        elif validate_email(email) == False:
            print(colored("Email is not valid please enter valid email","light_red"))
            time.sleep(1)
            clear()
            email = input(colored("email:\n","black"))
            check_email(email)
    check_email(email)
    clear()    
      
    if not validate_email(email):
        print(colored("Email is not valid","light_red"))
        return

    for user in users.values():
        if user['email'] == email:
            print(colored("Email is already exist\nPlease try again.\n","blue"))
            return
        
    username_id= str(uuid.uuid4())
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users[username] = {'id':username_id,'email': email, 'password': hashed_password}
    save_users(users)
    print(colored("Sign Up successful!\n","yellow"))
    game(users)

def main():
    clear()
    users = load_users()
    
    while True:
        clear()

        choice = input(colored("pleas select one of the options:\n\n0) EXIT\n\n1) Login\n\n2) Signup\n\n","black"))
        clear()
        if choice == '1':
            login(users)

        elif choice == '2':
            signup(users)

        elif choice == '0':
            break

        else:
            print(colored("Error\n\nPleas try again.","red"))
            time.sleep(1)

main()