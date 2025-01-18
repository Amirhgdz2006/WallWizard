# Amirhossein Goodarzi / Ali Ghenatgar / Mobina Shokohi / Niousha Gilani

import subprocess
import sys

# -------------- to download the required modules 
required_modules = ["pygame", "termcolor" , "bcrypt" , "uuid"]

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"installing : {module} \n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
# --------------
import json
import re
import bcrypt
import uuid
import os
from termcolor import colored
import quoridor_algorithm
import time

players = {}
global player_1 , player_2 , previous_game_value


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


def load_info_game():
    try:
        with open('info.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_info_game(info):
    with open('info.json', 'w') as file:
        json.dump(info, file)


def validate_email(email):
    regex = r'[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}'
    return re.match(regex, email) is not None


def game(users, current_user):
    
    playing = True

    while playing:
        choice = input(colored("Please select one of the options:\n\nA) NEW GAME\n\nB) Continue previous game\n\nC) WINNER CHART\n\nF) EXIT\n\n", "black"))
        clear()

        if choice.upper() == 'A':
            print(colored("Starting a new game...", "blue"))
            new_game(users, current_user)
            
            quoridor_algorithm.run_game()
            exit()

        elif choice.upper() == 'B':
            print(colored("Continuing previous game...\n", "blue"))
            
            previous_game_id = input(colored("Which game do you want to play? : ", "black"))
            
            with open('previous_game_info.json', 'w') as file:
                json.dump([previous_game_id],file)

            quoridor_algorithm.run_game()
            exit()

        elif choice.upper() == 'C':
            print(colored("Displaying winner chart...\n", "blue"))
            calculate_and_sort()

        elif choice.upper() == 'F':
            print(colored("Exiting menu...", "red"))
            clear()
            exit()
        else:
            print(colored("Error\nPlease try again.\n", "red"))


def new_game(users, current_user):
    global player_1 , player_2 , main_user
    username = input(colored("Player 2 username: ", "black"))

    
    def check_username(username):
        if username.lower() == "back":
            clear()
            game(users, current_user)

        elif len(username) <= 2:
            print(colored("Your username is not valid\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            username = input(colored("Player 2 username: ", "black"))
            check_username(username)

        elif username not in users:
            print(colored("Your username does not exist\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            username = input(colored("Player 2 username: ", "black"))
            check_username(username)
    check_username(username)
    clear()


    player_1 = main_user
    player_2 = username

    with open('p1_p2.json', 'w') as file:
        json.dump([player_1,player_2], file)

    password = input(colored("Player 2 password: ", "black"))
    def check_password(password):
        
        if password.lower() == "back":
            clear()
            game(users, current_user)
       
        elif len(password) < 8:
            print(colored("Your password is not valid\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            password = input(colored("Player 2 password: ", "black"))
            check_password(password)
    check_password(password)
    clear()
    if username in users:
        hashed_password = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]:
            print(colored("ENJOY THE GAME", "light_yellow"))
            players[current_user] = username
        else:
            print(colored("Incorrect password", "red"))


def login(users):
    global main_user
    username = input(colored("Username:\n", "black"))
    def check_username(username):
        if username.lower() == "back":
            main()
        
        elif len(username) <= 2:
            print(colored("Your username is not valid\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            username = input(colored("Username:\n", "black"))
            check_username(username)
        
        elif username not in users:
            print(colored("Your username does not exist\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            username = input(colored("Username:\n", "black"))
            check_username(username)
    check_username(username)
    clear()
    
    password = input(colored("Password:\n", "black"))
    def check_password(password):
        if password.lower() == "back":
            main()
        
        elif len(password) < 8:
            print(colored("Your password is not valid\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            password = input(colored("Password: ", "black"))
            check_password(password)
    check_password(password)
    clear()
    
    email = input(colored("Email:\n", "black"))
    def check_email(email):
        if email.lower() == "back":
            main()
        
        elif not validate_email(email):
            print(colored("Email is not valid\nPlease enter valid email", "light_red"))
            time.sleep(1)
            clear()
            email = input(colored("Email:\n", "black"))
            check_email(email)
    check_email(email)
    clear()
    
    while True:
        if username in users:
            hashed_password = users[username]['password'].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password) and users[username]['email'] == email:
                print(colored("Login successful\nEnjoy the game\n", "light_yellow"))
                main_user = username
                game(users, username)
            else:
                print(colored("Incorrect email or password", "light_red"))
                time.sleep(1)
                clear()
                password = input(colored("Password:\n", "black"))
                check_password(password)
                clear()
                email = input(colored("Email:\n", "black"))
                check_email(email)
                clear()
        check_email(email)


def signup(users, info):
    
    username = input(colored("Username:\n", "black"))
    def check_username(username):
        if username.lower() == "back":
            main()
        
        elif len(username) <= 2:
            print(colored("Your username is not valid\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            username = input(colored("Username:\n", "black"))
            check_username(username)
        
        elif username in users:
            print(colored("Your username already exists\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            username = input(colored("Username:\n", "black"))
            check_username(username)
    check_username(username)
    clear()
    
    password = input(colored("Password:\n", "black"))
    def check_password(password):
        if password.lower() == "back":
            main()
        
        elif len(password) < 8:
            print(colored("Your password is not valid\nPlease try again", "light_red"))
            time.sleep(1)
            clear()
            password = input(colored("Password: ", "black"))
            check_password(password)
    check_password(password)
    clear()
    
    email = input(colored("Email:\n", "black"))
    def check_email(email):
        if email.lower() == "back":
            main()
        
        elif not validate_email(email):
            print(colored("Email is not valid\nPlease enter valid email", "light_red"))
            time.sleep(1)
            clear()
            email = input(colored("Email:\n", "black"))
            check_email(email)
    check_email(email)
    clear()
    
    if not validate_email(email):
        print(colored("Email is not valid", "light_red"))
        return
    
    for user in users.values():
        if user['email'] == email:
            print(colored("Email already exists\nPlease try again.\n", "blue"))
            return
    
    username_id = str(uuid.uuid4())
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users[username] = {'id': username_id, 'email': email, 'password': hashed_password}
    save_users(users)
    info[username] = {'winner': 0, 'loser': 0}
    save_info_game(info)
    print(colored("Sign up successful!\n", "yellow"))
    game(users, username)


def calculate_and_sort():
    clear()

    with open('info.json', 'r') as file:
        data = json.load(file)

    sorted_data = dict(sorted(data.items(), key=lambda item: (item[1]['winner'] - item[1]['loser']), reverse=True))


    lst_show = []
    for item in sorted_data:
        lst_show.append(f"{colored(item ,'yellow')} : [ win : {colored(data[item]['winner'] , 'green')} , loss : {colored(data[item]['loser'] , 'red')} ]")

    for person in lst_show:
        print(person)

    entry_e = input(colored('Type anything to back in Menu : ' , 'yellow')) 
    if entry_e.upper() == 'EXIT':
        main()
    else:
        main()


def main():
    clear()
    users = load_users()
    info = load_info_game()
    
    while True:
        clear()
        choice = input(colored("Please select one of the options:\n\n0) EXIT\n\n1) Login\n\n2) Sign up\n\n", "black"))
        clear()
        if choice == '1':
            login(users)
        elif choice == '2':
            signup(users, info)
        elif choice == '0':
            exit()
            break
        else:
            print(colored("Error\nPlease try\n\n"))


main()            
