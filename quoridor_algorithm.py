# Amirhossein Goodarzi / Ali Ghenatgar / Mobina Shokohi / Niousha Gilani

import json
from termcolor import colored
import os
import pygame
import copy

# -------------- saving game info
def game(player1: str, player2: str, place1: list, place2: list, walls: list, turn: int, result: bool, game_ID: str): 
    new_game_data = {   
        "player1": player1,
        "player2": player2,
        "place1": place1,
        "place2": place2,
        "walls": walls,
        "turn": turn,
        "result": result
    }

    if not os.path.exists('game_info.json'):

        with open('game_info.json', 'w') as file:
            json.dump({game_ID: new_game_data}, file, indent=4)
    else:
        with open('game_info.json', 'r+') as file:
            data = json.load(file)
            data[game_ID] = new_game_data 
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
# --------------

# -------------- saving user info
def user(user_name: str, win: int, loss: int):
    new_user_data = {
        user_name: {
            'win': win,
            'loss': loss
        }
    }

    if not os.path.exists('user_info.json'):
        with open('user_info.json', 'w') as file:
            json.dump([new_user_data], file, indent=4)
    else:
        with open('user_info.json', 'r+') as file:
            data = json.load(file)
            data.append(new_user_data)
            file.seek(0)
            json.dump(data, file, indent=4)


    if not os.path.exists('user_info.json'):
        with open('user_info.json', 'w') as file:
            json.dump([new_user_data], file, indent=4)
    else:
        with open('user_info.json', 'r+') as file:
            data = json.load(file)
            data.append(new_user_data)
            file.seek(0)
            json.dump(data, file, indent=4)
# --------------

# -------------- main playground
playground = [[" ","|"," ","|"," ","|"," ","|", " " ,"|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," "],
              ["—","+","—","+","—","+","—","+","—","+","—","+","—","+","—","+","—"],
              [" ","|"," ","|"," ","|"," ","|", " " ,"|"," ","|"," ","|"," ","|"," "]]
# --------------

# -------------- playground for walls
playground_original = [[" "," "," "," "," "," "," "," ", " " ," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," ", " " ," "," "," "," "," "," "," "," "]]
# --------------

def clear():
    os.system('cls||clear')

clear()

# -------------- placing default positions
row1 , column1 = 16 , 8
row2 , column2 = 0 , 8
playground[row1][column1] = 1
playground_original[row1][column1] = 1
playground[row2][column2] = 2
playground_original[row2][column2] = 2
wall_player_1 = 10
wall_player_2 = 10
# --------------

# -------------- for loading previous games
def previous_game():
    global playground_original, playground, row1, column1, row2, column2 , previous_game_value

    if not os.path.exists('game_info.json'):
        with open('game_info.json', 'w') as file:
            json.dump({}, file)


    if not os.path.exists('previous_game_info.json'):
        with open('previous_game_info.json', 'w') as file:
            json.dump([], file)
    
    with open('previous_game_info.json', 'r') as file:
        data2 = json.load(file)


    if data2 != []:

        previous_game_id = data2[0]

        with open('game_info.json', 'r') as file:
            data = json.load(file)


        playground_original[row1][column1] = " "
        playground_original[row2][column2] = " "
        playground[row1][column1] = " "
        playground[row2][column2] = " "

        row1 = data[previous_game_id]["place1"][0]
        column1 = data[previous_game_id]["place1"][1]
        row2 = data[previous_game_id]["place2"][0]
        column2 = data[previous_game_id]["place2"][1]

        playground_original[row1][column1] = 1
        playground_original[row2][column2] = 2
        playground[row1][column1] = 1
        playground[row2][column2] = 2

        playground_original = data[previous_game_id]['walls']

        with open('previous_game_info.json', 'w') as file:
            json.dump([],file)
# --------------

# -------------- sounds
def sound(file):

    pygame.mixer.init()

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.quit()
# --------------

# -------------- saving game info
def save():

    global  row1 , column1 , row2 , column2 ,playground_original , turn ,result ,  is_running 
    is_running = False
    clear()
    game_id = input('enter your game ID: ')

    with open('p1_p2.json', 'r') as file:
        data = json.load(file)
    player_1 , player_2 = data[0] , data[1]
    game(player_1,player_2,[row1,column1],[row2,column2],playground_original,turn,result , game_id)
    exit()

    with open('p1_p2.json', 'w') as file:
        file.write('')
# --------------

# -------------- screen refresh and colors 
def refresh_screen():

    num_bar = [" "," ","1"," ","2"," ","3"," ","4"," ","5"," ","6"," ","7"," ","8"," "]

    playground_copy = copy.deepcopy(playground)
    count_1 = 0
    for item in playground_copy:
        if playground_copy.index(item) % 2 != 0:
            item.insert(0,str(count_1))
        else:
            item.insert(0,' ')
            count_1 = count_1 + 1
    
    playground_copy.insert(0,num_bar)
     
    playground_original_copy = copy.deepcopy(playground_original)
    count_2 = 0
    for item in playground_original_copy:
        if playground_original_copy.index(item) % 2 != 0:
            item.insert(0,str(count_2))
        else:
            item.insert(0,' ')
            count_2 = count_2 + 1
    
    playground_original_copy.insert(0,num_bar)
    clear()
    for row in range(18):
        for col in range(18):
            if playground_copy[row][col] == 2 :
                print(colored(playground_copy[row][col],"red"),end=" ")
            elif playground_copy[row][col] == 1 :
                print(colored(playground_copy[row][col],"blue"),end=" ")
            elif playground_original_copy[row][col] == 0 :
                print(colored(playground_copy[row][col],"yellow"),end=" ")
            else:
                print(colored(playground_copy[row][col],"black"),end=" ")
        print()
    print()
    print(colored(' ————————————————————————————————— ',"light_green"))
    print(colored('|   Up:u Down:d Left:l Right:r    |',"light_green"))
    print(colored('|   Move mode: move               |',"light_green"))
    print(colored('|   Wall mode: wall               |',"light_green"))
    print(colored('|—————————————————————————————————|',"light_green"))
    print(colored('|   player 1 walls : ',"light_green"),colored(f"{wall_player_1:02}","light_yellow"),colored('         |',"light_green"))
    print(colored('|   player 2 walls : ',"light_green"),colored(f"{wall_player_2:02}","light_yellow"),colored('         |',"light_green"))
    print(colored(' ————————————————————————————————— ',"light_green"))
    print()
# --------------

# -------------- for moving pawn
def check_move(pawn,command):
    global wall_player_1,wall_player_2

    def move_up():
        global row1,column1,row2,column2
        if pawn == 1:
            if playground_original[row1 - 1][column1] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= row1 - 2 <= 16 :
                if row2 + 2 == row1 and column2  == column1 :
                    if row1 - 4 >= 0 :
                        if playground_original[row1 - 3][column1] == 0 :
                            if column1 == 0 and playground_original[row1 - 2][column1 + 1] != 0 :
                                playground[row1][column1] = " "
                                playground_original[row1][column1] = " "
                                row1 -= 2
                                column1 += 2
                                playground[row1][column1] = 1
                                playground_original[row1][column1] = 1
                            elif column1 == 16 and playground_original[row1 - 2][column1 - 1] != 0 :
                                playground[row1][column1] = " "
                                playground_original[row1][column1] = " "
                                row1 -= 2
                                column1 -= 2
                                playground[row1][column1] = 1
                                playground_original[row1][column1] = 1
                            elif 2 <= column1 <= 14 and ( playground_original[row1 -2][column1+1] != 0 or playground_original[row1 -2][column1-1] ) != 0:
                                diagonal_command = input("Enter diagonal move command ( r , l ): ")
                                if diagonal_command == "r" :
                                    if playground_original[row1 - 2][column1 + 1] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 -= 2
                                        column1 += 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "l" :
                                    if playground_original[row1 - 2][column1 - 1] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 -= 2
                                        column1 -= 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(1,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(1,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row1][column1] = " "
                            playground_original[row1][column1] = " "
                            row1 -= 4
                            playground[row1][column1] = 1
                            playground_original[row1][column1] = 1
                            
                            
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(1,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row1][column1] = " "
                    playground_original[row1][column1] = " "
                    row1 -= 2
                    playground[row1][column1] = 1
                    playground_original[row1][column1] = 1
                    

                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

        elif pawn == 2:
            if playground_original[row2 - 1][column2] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(2,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
            elif 0 <= row2 - 2 <= 16 :
                if row1 + 2 == row2 and column2  == column1 :
                    if row2 - 4 >= 0 :
                        if playground_original[row2 - 3][column2] == 0 :
                            if column2 == 0 and playground_original[row2 - 2][column2 + 1] != 0 :
                                playground[row2][column2] = " "
                                playground_original[row2][column2] = " "
                                row2 -= 2
                                column2 += 2
                                playground[row2][column2] = 2
                                playground_original[row2][column2] = 2
                            elif column2 == 16 and playground_original[row2 - 2][column2 - 1] != 0 :
                                playground[row2][column2] = " "
                                playground_original[row2][column2] = " "
                                row2 -= 2
                                column2 -= 2
                                playground[row2][column2] = 2
                                playground_original[row2][column2] = 2
                            elif 2 <= column2 <= 14 and ( playground_original[row2 -2][column2+1] != 0 or playground_original[row2 -2][column2-1]) != 0:
                                diagonal_command = input("Enter diagonal move command ( r , l ): ")
                                if diagonal_command == "r" :
                                    if playground_original[row2 - 2][column2 + 1] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 -= 2
                                        column2 += 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "l" :
                                    if playground_original[row2 - 2][column2 - 1] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 -= 2
                                        column2 -= 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(1,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(2,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row2][column2] = " "
                            playground_original[row2][column2] = " "
                            row2 -= 4
                            playground[row2][column2] = 2
                            playground_original[row2][column2] = 2
                           
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(2,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    row2 -= 2
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
                   

                    
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(2,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

    def move_down():
        global row1,column1,row2,column2
        if pawn == 1:
            if row1 + 1 <= 16 and playground_original[row1 + 1][column1] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= row1 + 2 <= 16 :
                if row2 - 2 == row1 and column2  == column1 :
                    if row1 + 4 <= 16 :
                        if playground_original[row1 + 3][column1] == 0 :
                            if column1 == 0 and playground_original[row1 + 2][column1 + 1] != 0 :
                                playground[row1][column1] = " "
                                playground_original[row1][column1] = " "
                                row1 += 2
                                column1 += 2
                                playground[row1][column1] = 1
                                playground_original[row1][column1] = 1
                            elif column1 == 16 and playground_original[row1 + 2][column1 - 1] != 0 :
                                playground[row1][column1] = " "
                                playground_original[row1][column1] = " "
                                row1 += 2
                                column1 -= 2
                                playground[row1][column1] = 1
                                playground_original[row1][column1] = 1
                            elif 2 <= column1 <= 14 and ( playground_original[row1 + 2][column1+1] != 0 or playground_original[row1 + 2][column1-1] ) != 0:
                                diagonal_command = input("Enter diagonal move command ( r , l ): ")
                                if diagonal_command == "r" :
                                    if playground_original[row1 + 2][column1 + 1] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 += 2
                                        column1 += 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "l" :
                                    if playground_original[row1 + 2][column1 - 1] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 += 2
                                        column1 -= 2
                                        playground[row1][column1] = 2
                                        playground_original[row1][column1] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(1,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(1,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row1][column1] = " "
                            playground_original[row1][column1] = " "
                            row1 += 4
                            playground[row1][column1] = 1
                            playground_original[row1][column1] = 1
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(1,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row1][column1] = " "
                    playground_original[row1][column1] = " "
                    row1 += 2
                    playground[row1][column1] = 1
                    playground_original[row1][column1] = 1
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

        elif pawn == 2:
            if playground_original[row2 + 1][column2] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(2,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
            elif 0 <= row2 + 2 <= 16 :
                if row1 - 2 == row2 and column2  == column1 :
                    if row2 + 4 <= 16 :
                        if playground_original[row2 + 3][column2] == 0 :
                            if column2 == 0 and playground_original[row2 + 2][column2 + 1] != 0 :
                                playground[row2][column2] = " "
                                playground_original[row2][column2] = " "
                                row2 += 2
                                column2 += 2
                                playground[row2][column2] = 2
                                playground_original[row2][column2] = 2
                            elif column2 == 16 and playground_original[row2 + 2][column2 - 1] != 0 :
                                playground[row2][column2] = " "
                                playground_original[row2][column2] = " "
                                row2 += 2
                                column2 -= 2
                                playground[row2][column2] = 2
                                playground_original[row2][column2] = 2
                            elif 2 <= column2 <= 14 and ( playground_original[row2 + 2][column2+1] != 0 or playground_original[row2 + 2][column2-1] != 0 ) :
                                diagonal_command = input("Enter diagonal move command ( r , l ): ")
                                if diagonal_command == "r" :
                                    if playground_original[row2 + 2][column2 + 1] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 += 2
                                        column2 += 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "l" :
                                    if playground_original[row2 + 2][column2 - 1] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 += 2
                                        column2 -= 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(1,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(2,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row2][column2] = " "
                            playground_original[row2][column2] = " "
                            row2 += 4
                            playground[row2][column2] = 2
                            playground_original[row2][column2] = 2
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(2,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    row2 += 2
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(2,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

    def move_right():
        global row1,column1,row2,column2
        if pawn == 1:
            if column1 + 1 <= 16 and playground_original[row1][column1 + 1] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= column1 + 2 <= 16 :
                if column1 + 2 == column2 and row2  == row1 :
                    if column1 + 4 <= 16 :
                        if playground_original[row1][column1 + 3] == 0 :
                            if 2 <= row1 <= 14 and (playground_original[row1 + 1][column1 + 2] != 0 or playground_original[row1 - 1][column1 + 2] != 0):
                                diagonal_command = input("Enter diagonal move command ( u , d ): ")
                                if diagonal_command == "u" :
                                    if playground_original[row1 - 1][column1 + 2] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 -= 2
                                        column1 += 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "d" :
                                    if playground_original[row1 + 1][column1 + 2] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 += 2
                                        column1 += 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(1,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(1,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row1][column1] = " "
                            playground_original[row1][column1] = " "
                            column1  += 4
                            playground[row1][column1] = 1
                            playground_original[row1][column1] = 1
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(1,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row1][column1] = " "
                    playground_original[row1][column1] = " "
                    column1 += 2
                    playground[row1][column1] = 1
                    playground_original[row1][column1] = 1
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

        elif pawn == 2:
            if column2 + 1 <= 16 and playground_original[row2][column2 + 1] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= column2 + 2 <= 16 :
                if column2 + 2 == column1 and row1  == row2 :
                    if column2 + 4 <= 16 :
                        if playground_original[row2][column2 + 3] == 0 :
                            if 2 <= row2 <= 14 and playground_original[row2 + 1][column2 + 2] != 0 or playground_original[row2 - 1][column2 + 2] != 0:
                                diagonal_command = input("Enter diagonal move command ( u , d ): ")
                                if diagonal_command == "u" :
                                    if playground_original[row2 - 1][column2 + 2] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 -= 2
                                        column2 += 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "d" :
                                    if playground_original[row2 + 1][column2 + 2] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 += 2
                                        column2 += 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(2,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(2,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row2][column2] = " "
                            playground_original[row2][column2] = " "
                            column2 += 4
                            playground[row2][column2] = 2
                            playground_original[row2][column2] = 2
                            
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(1,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                        
                else:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    column2 += 2
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(2,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

    def move_left():
        global row1,column1,row2,column2
        if pawn == 1:
            if column1 - 1 >= 0 and playground_original[row1][column1 - 1] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= column1 - 2 <= 16 :
                if column1 - 2 == column2 and row2  == row1 :
                    if column1 - 4 >= 0 :
                        if playground_original[row1][column1 - 3] == 0 :
                            if 2 <= row1 <= 14 and playground_original[row1 + 1][column1 - 2] != 0 or playground_original[row1 - 1][column1 - 2] != 0:
                                diagonal_command = input("Enter diagonal move command ( u , d ): ")
                                if diagonal_command == "u" :
                                    if playground_original[row1 - 1][column1 - 2] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 -= 2
                                        column1 -= 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "d" :
                                    if playground_original[row1 + 1][column1 - 2] != 0 :
                                        playground[row1][column1] = " "
                                        playground_original[row1][column1] = " "
                                        row1 += 2
                                        column1 -= 2
                                        playground[row1][column1] = 1
                                        playground_original[row1][column1] = 1
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(1,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(1,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(1,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row1][column1] = " "
                            playground_original[row1][column1] = " "
                            column1 -= 4
                            playground[row1][column1] = 1
                            playground_original[row1][column1] = 1
                            
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(1,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row1][column1] = " "
                    playground_original[row1][column1] = " "
                    column1 -= 2
                    playground[row1][column1] = 1
                    playground_original[row1][column1] = 1
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))

        elif pawn == 2:
            if column2 - 1 >= 0 and playground_original[row2][column2 - 1] == 0 :
                print(colored("Move blocked by wall, please try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(1,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= column2 - 2 <= 16 :
                if column2 - 2 == column1 and row1  == row2 :
                    if column2 - 4 >= 0 :
                        if playground_original[row2][column2 - 3] == 0:
                            if 2 <= row2 <= 14 and playground_original[row2 + 1][column2 - 2] != 0 or playground_original[row2 - 1][column2 - 2] != 0:
                                diagonal_command = input("Enter diagonal move command ( u , d ): ")
                                if diagonal_command == "u" :
                                    if playground_original[row2 - 1][column2 - 2] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 -= 2
                                        column2 -= 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))

                                elif diagonal_command == "d" :
                                    if playground_original[row2 + 1][column2 - 2] != 0 :
                                        playground[row2][column2] = " "
                                        playground_original[row2][column2] = " "
                                        row2 += 2
                                        column2 -= 2
                                        playground[row2][column2] = 2
                                        playground_original[row2][column2] = 2
                                    else:
                                        print(colored("Move blocked by wall, please try again","red"))
                                        while True:
                                            command = input(f"Enter move command: ").lower()
                                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                                check_move(2,command)
                                                break
                                            elif command == "wall":
                                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                                check_wall(wall_command)
                                                break
                                            elif command == "save" :
                                                save()
                                            else:
                                                print(colored("Invalid command, please  try again","red"))
                                else:
                                    print(colored("Invalid command, please  try again","red"))
                                    while True:
                                        command = input(f"Enter move command: ").lower()
                                        if command == "u" or command == "d" or command == "l" or command == "r" :
                                            check_move(2,command)
                                            break
                                        elif command == "wall":
                                            wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                            check_wall(wall_command)
                                            break
                                        elif command == "save" :
                                            save()
                                        else:
                                            print(colored("Invalid command, please  try again","red"))
                            else:
                                print(colored("Move blocked by wall, please try again","red"))
                                while True:
                                    command = input(f"Enter move command: ").lower()
                                    if command == "u" or command == "d" or command == "l" or command == "r" :
                                        check_move(2,command)
                                        break
                                    elif command == "wall":
                                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                        check_wall(wall_command)
                                        break
                                    elif command == "save" :
                                        save()
                                    else:
                                        print(colored("Invalid command, please  try again","red"))
                        else:    
                            playground[row2][column2] = " "
                            playground_original[row2][column2] = " "
                            column2 -= 4
                            playground[row2][column2] = 2
                            playground_original[row2][column2] = 2
                            
                    else:
                        print(colored("Invalid move, please try again","red"))
                        while True:
                            command = input(f"Enter move command: ").lower()
                            if command == "u" or command == "d" or command == "l" or command == "r" :
                                check_move(2,command)
                                break
                            elif command == "wall":
                                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                                check_wall(wall_command)
                                break
                            elif command == "save" :
                                save()
                            else:
                                print(colored("Invalid command, please  try again","red"))
                else:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    column2 -= 2
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
                    
            else:
                print(colored("Invalid move, please  try again","red"))
                while True:
                    command = input(f"Enter move command: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        check_move(2,command)
                        break
                    elif command == "wall":
                        wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        break
                    elif command == "save" :
                        save()
                    else:
                        print(colored("Invalid command, please  try again","red"))



    if command.lower() == "u":
        move_up()
    elif command.lower() == "d" :
        move_down()
    elif command.lower() == "l" :
        move_left()
    elif command.lower() == "r" :
        move_right()
    elif command.lower() == "wall":
        if turn == 1:
            if wall_player_1 > 0:
                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                check_wall(wall_command)
            else:
                print(colored("No walls remaining","red"))
                command = input(f"Enter move command: ").lower()
                check_move(turn,command)
        elif turn == 2:
            if wall_player_2 > 0:
                wall_command = input("Enter wall command ( center row, center column, direction(h/v) ): ").lower()
                check_wall(wall_command)
            else:
                print(colored("No walls remaining","red"))
                command = input(f"Enter move command: ").lower()
                check_move(turn,command)
# --------------

# -------------- for placing walls
def check_wall(wall_command):
    global turn
    global wall_player_1,wall_player_2

    def place_wall(list_command):
        playground_original[list_command[0]][list_command[1]] = 0   
        if list_command[2] == "h":
            playground_original[list_command[0]][list_command[1] - 1] = 0
            playground_original[list_command[0]][list_command[1] + 1] = 0
        elif list_command[2] == "v":
            playground_original[list_command[0] - 1][list_command[1]] = 0
            playground_original[list_command[0] + 1][list_command[1]] = 0


        def check_dfs():
            global row1_copy, row2_copy, column1_copy, column2_copy, dfs, visited1, visited2, max_try, try_

            dfs = True
            row1_copy = row1
            row2_copy = row2
            column1_copy = column1
            column2_copy = column2
            playground_original_copy1 = copy.deepcopy(playground_original)
            playground_original_copy2 = copy.deepcopy(playground_original)
            visited1 = []
            visited2 = []

            visited1.append([row1_copy, column1_copy])
            visited2.append([row2_copy, column2_copy])
            max_try = 10000
            try_ = 0

            while row1_copy != 0 and dfs == True:
                def check_dfs_1():
                    global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                    try_ += 1

                    def up():
                        global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                        if  0 < row1_copy <= 16 and playground_original_copy1[row1_copy - 1][column1_copy] != 0:
                            if [row1_copy - 2, column1_copy] not in visited1:
                                row1_copy -= 2
                                visited1.append([row1_copy, column1_copy])
                            else:
                                right()
                        else:
                            right()
                    

                    def right():
                        global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                        if 0 <= column1_copy < 16 and playground_original_copy1[row1_copy][column1_copy + 1] != 0:
                            if [row1_copy, column1_copy + 2] not in visited1:
                                column1_copy += 2
                                visited1.append([row1_copy, column1_copy])
                            else:
                                left()
                        else:
                            left()
                
                    
                    def left():
                        global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                        if 0 < column1_copy <= 16 and playground_original_copy1[row1_copy][column1_copy - 1] != 0:
                            if [row1_copy, column1_copy - 2] not in visited1:
                                column1_copy -= 2
                                visited1.append([row1_copy, column1_copy])
                            else:
                                down()
                        else:
                            down()
                    
                    
                    def down():
                        global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                        if 0 <= row1_copy < 16 and playground_original_copy1[row1_copy + 1][column1_copy] != 0:
                            if [row1_copy + 2, column1_copy] not in visited1:
                                row1_copy += 2
                                visited1.append([row1_copy, column1_copy])
                            else:
                                wall()
                        else:
                            wall()

                    
                    def wall():
                        global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                        if playground_original_copy1[row1_copy - 1][column1_copy] == 0 and playground_original_copy1[row1_copy][column1_copy + 1] == 0 and playground_original_copy1[row1_copy][column1_copy - 1] == 0 and playground_original_copy1[row1_copy + 1][column1_copy] == 0:
                            dfs = False
                        else:
                            back_track()
                    
                    
                    def back_track():
                        global row1_copy, column1_copy, dfs, visited1, try_ , max_try
                        if len(visited1) != 0:
                            playground_original_copy1[visited1[-1][0]][visited1[-1][1]] = 0
                            visited1.pop()
                            row1_copy, column1_copy = visited1[-1]
                            check_dfs_1()

                    up()
                    
                    if try_ >= max_try:
                        dfs = False


                check_dfs_1()
                    
            while row2_copy != 16 and dfs == True:
                def check_dfs_2():
                    global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                    try_ += 1


                    def down():
                        global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                        if 0 <= row2_copy < 16 and playground_original_copy2[row2_copy + 1][column2_copy] != 0:
                            if [row2_copy + 2, column2_copy] not in visited2:
                                row2_copy += 2
                                visited2.append([row2_copy, column2_copy])
                            else:
                                right()
                        else:
                            right()

                    
                    def right():
                        global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                        if 0 <= column2_copy < 16 and playground_original_copy2[row2_copy][column2_copy + 1] != 0:
                            if [row2_copy, column2_copy + 2] not in visited2:
                                column2_copy += 2
                                visited2.append([row2_copy, column2_copy])
                            else:
                                left()
                        else:
                            left()
                    
                    
                    def left():
                        global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                        if 0 < column2_copy <= 16 and playground_original_copy2[row2_copy][column2_copy - 1] != 0:
                            if [row2_copy, column2_copy - 2] not in visited2:
                                column2_copy -= 2
                                visited2.append([row2_copy, column2_copy])
                            else:
                                up()
                        else:
                            up()
                    
                    
                    def up():
                        global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                        if  0 < row2_copy <= 16 and playground_original_copy2[row2_copy - 1][column2_copy] != 0:
                            if [row2_copy - 2, column2_copy] not in visited2:
                                row2_copy -= 2
                                visited2.append([row2_copy, column2_copy])
                            else:
                                wall()
                        else:
                            wall()
                    

                    def wall():
                        global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                        if playground_original_copy2[row2_copy - 1][column2_copy] == 0 and playground_original_copy2[row2_copy][column2_copy + 1] == 0 and playground_original_copy2[row2_copy][column2_copy - 1] == 0 and playground_original_copy2[row2_copy + 1][column2_copy] == 0:
                            dfs = False
                        else:
                            back_track()
                    
                    
                    def back_track():
                        global row2_copy, column2_copy, dfs, visited2, try_ , max_try
                        if len(visited2) != 0:
                            playground_original_copy2[visited2[-1][0]][visited2[-1][1]] = 0
                            visited2.pop()
                            row2_copy, column2_copy = visited2[-1]
                            check_dfs_2()

                    down()
                    
                    if try_ >= max_try:
                        dfs = False


                check_dfs_2()
        check_dfs()
    
        if dfs == False:
            
            playground_original[list_command[0]][list_command[1]] = ' '   
            if list_command[2] == "h":
                playground_original[list_command[0]][list_command[1] - 1] = ' '
                playground_original[list_command[0]][list_command[1] + 1] = ' '
            elif list_command[2] == "v":
                playground_original[list_command[0] - 1][list_command[1]] = ' '
                playground_original[list_command[0] + 1][list_command[1]] = ' '

            print(colored("Can't place a wall there ,please  try again","red"))
            wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
            check_wall(wall_command)

    if wall_command == "move":
        while True:
            command = input(f"Enter move command: ").lower()
            if command == "u" or command == "d" or command == "l" or command == "r" :
                check_move(turn,command)
                refresh_screen()
                break
            elif command == "wall":
                if turn == 1:
                    if wall_player_1 > 0:
                        wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        refresh_screen()
                        break
                    else:
                        print(colored("No walls remaining","red"))
                        command = input(f"Enter move command: ").lower()
                        check_move(turn,command)

                elif turn == 2:
                    if wall_player_2 > 0:
                        wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        refresh_screen()
                        break
                    else:
                        print(colored("No walls remaining","red"))
                        command = input(f"Enter move command: ").lower()
                        check_move(turn,command)
            elif command == "save" :
                save()
            else:
                print(colored("Invalid command, please  try again","red"))
    else:
        wall_command = wall_command.split()
        if len(wall_command) != 3:
            check_wall_command = False
        else:
            if (wall_command[0].isdigit()) and (wall_command[1].isdigit()) and (wall_command[2] == "h" or wall_command[2] == "v") :
                wall_command = [int(wall_command[0]),int(wall_command[1]),wall_command[2]]
                check_wall_command = True
            else:
                check_wall_command = False

            if check_wall_command:
                if 1 <= wall_command [0] <= 8 and 1 <= wall_command[1] <= 8:
                    check_wall_command = True
                else:
                    check_wall_command = False
                    
            if check_wall_command:
                wall_command = [(wall_command[0]) * 2 - 1 , wall_command[1] * 2 - 1 , wall_command[2]]
                if wall_command[2] == "h":
                    if playground_original[wall_command[0]][wall_command[1]] != 0 and playground_original[wall_command[0]][wall_command[1]-1] != 0 and playground_original[wall_command[0]][wall_command[1]+1] != 0:
                        check_wall_command = True
                    else:
                        check_wall_command = False
                elif wall_command[2] == "v":
                    if playground_original[wall_command[0]][wall_command[1]] != 0 and playground_original[wall_command[0]-1][wall_command[1]] != 0 and playground_original[wall_command[0]+1][wall_command[1]] != 0:
                        check_wall_command = True
                    else:
                        check_wall_command = False

        if check_wall_command:
            wall_command = [int(wall_command[0]),int(wall_command[1]),wall_command[2]]
            if turn == 1:
                wall_player_1 -= 1
            elif turn == 2:
                wall_player_2 -= 1
            place_wall(wall_command)
        else :
            print(colored("Invalid wall, please  try again","red"))
            wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
            check_wall(wall_command)
# --------------    

# -------------- showing victory 
def victory_text(pawn):
    print(colored(' ——————————————————————————————— ',"black","on_yellow"),)
    print(colored(f'|        Player {pawn} wins !        |',"black","on_yellow"))
    print(colored(' ——————————————————————————————— ',"black","on_yellow"))
# --------------

result = 0
# -------------- main function
def run_game():
    global turn , is_running , result
    previous_game()
    refresh_screen()
    turn = 1
    is_running = True
    while is_running:
        print()
        if turn == 1:
            print(colored(f"         Player one's turn         ", "blue" , "on_light_cyan" , attrs = ["bold"]))
        else :
            print(colored(f"         Player two's turn         ", "white" , "on_red" , attrs = ["bold"]))
        sound('sound.mp3')
        while True:
            command = input(f"Enter move command: ").lower()
            if command == "u" or command == "d" or command == "l" or command == "r" :
                check_move(turn,command)
                refresh_screen()
                break
            elif command == "wall":
                if turn == 1:
                    if wall_player_1 > 0:
                        wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        refresh_screen()
                        break
                    else:
                        print(colored("No walls remaining","red"))
                        command = input(f"Enter move command: ").lower()
                        check_move(turn,command)

                elif turn == 2:
                    if wall_player_2 > 0:
                        wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
                        check_wall(wall_command)
                        refresh_screen()
                        break
                    else:
                        print(colored("No walls remaining","red"))
                        command = input(f"Enter move command: ").lower()
                        check_move(turn,command)
            elif command == "save" :
                save()
            else:
                print(colored("Invalid command, please  try again","red"))
        if turn == 1 :
            turn = 2
        else :
            turn = 1
        if row1 == 0 :
            victory_text(1)
            is_running = False

            result = 1

            with open('p1_p2.json', 'r') as file:
                data = json.load(file)
            player_1 , player_2 = data[0] , data[1]

            with open('info.json', 'r') as file:
                data = json.load(file)

            win_num = data[player_1]['winner']

            data[player_1]['winner'] = win_num + 1

            loss_num = data[player_2]['loser']

            data[player_2]['loser'] = loss_num + 1


            with open('info.json', 'w') as file:
                json.dump(data, file) 

            sound('ftadaa.mp3')

        elif row2 == 16 :
            victory_text(2)
            is_running = False

            result = 2            

            with open('p1_p2.json', 'r') as file:
                data = json.load(file)

            player_1 , player_2 = data[0] , data[1]
        
            with open('info.json', 'r') as file:
                data = json.load(file)

            win_num = data[player_2]['winner']

            data[player_2]['winner'] = win_num + 1

            loss_num = data[player_1]['loser']

            data[player_1]['loser'] = loss_num + 1

            with open('info.json', 'w') as file:
                json.dump(data, file) 

            sound('tadaa.mp3')
# --------------

if __name__ == "__main__":
    from login_signup import run_game
    run_game()
