from termcolor import colored
import os

playground = [[" ","|"," ","|"," ","|"," ","|", 1 ,"|"," ","|"," ","|"," ","|"," "],
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
              [" ","|"," ","|"," ","|"," ","|", 2 ,"|"," ","|"," ","|"," ","|"," "]]

playground_original = [[" "," "," "," "," "," "," "," ", 1 ," "," "," "," "," "," "," "," "],
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
                       [" "," "," "," "," س"," "," "," ", 2 ," "," "," "," "," "," "," "," "]]

def clear():
    os.system('cls||clear')

row1 , column1 = 0 , 8
row2 , column2 = 16 , 8
    
def check_move(pawn,command):

    def move_left():
        global row1,column1,row2,column2
        if pawn == 1:
            if 0 <= column1 - 2 <= 16 :
                playground[row1][column1] = " "
                playground_original[row1][column1] = " "
                column1 -= 2
                playground[row1][column1] = 1
                playground_original[row1][column1] = 1
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
        elif pawn == 2:
            if 0 <= column2 - 2 <= 16 :
                playground[row2][column2] = " "
                playground_original[row1][column1] = " "
                column2 -= 2
                playground[row2][column2] = 2
                playground_original[row1][column1] = 2
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
        return playground

    def move_right():
        global row1,column1,row2,column2
        if pawn == 1:
            if 0 <= column1 + 2 <= 16 :
                playground[row1][column1] = " "
                playground_original[row1][column1] = " "
                column1 += 2
                playground[row1][column1] = 1
                playground_original[row1][column1] = 1
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
        elif pawn == 2:
            if 0 <= column2 + 2 <= 16 :
                playground[row2][column2] = " "
                playground_original[row1][column1] = " "
                column2 += 2
                playground[row2][column2] = 2
                playground_original[row1][column1] = 2
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
        return playground

    def move_up():
        global row1,column1,row2,column2
        if pawn == 1:
            if 0 <= row1 - 2 <= 16 :
                playground[row1][column1] = " "
                playground_original[row1][column1] = " "
                row1 -= 2
                playground[row1][column1] = 1
                playground_original[row1][column1] = 1
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
        elif pawn == 2:
            if 0 <= row2 - 2 <= 16 :
                playground[row2][column2] = " "
                playground_original[row1][column1] = " "
                row2 -= 2
                playground[row2][column2] = 2
                playground_original[row1][column1] = 2
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
        return playground

    def move_down():
        global row1,column1,row2,column2
        if pawn == 1:
            if 0 <= row1 + 2 <= 16 :
                playground[row1][column1] = " "
                playground_original[row1][column1] = " "
                row1 += 2
                playground[row1][column1] = 1
                playground_original[row1][column1] = 1
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
        elif pawn == 2:
            if 0 <= row2 + 2 <= 16 :
                playground[row2][column2] = " "
                playground_original[row1][column1] = " "
                row2 += 2
                playground[row2][column2] = 2
                playground_original[row1][column1] = 2
            else:
                print(colored("Invalid move, please  try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
        return playground

    if command.lower() == "u":
        move_up()
    elif command.lower() == "d" :
        move_down()
    elif command.lower() == "l" :
        move_left()
    elif command.lower() == "r" :
        move_right()

def check_wall(wall_command):
    wall_command = wall_command.split()
    if len(wall_command) != 3:
        check_wall_command = False
    else:
        for i in range(3):
            check_wall_command = True
            if wall_command[i].isdigit():
                wall_command[i] = int(wall_command[i])
            else:
                check_wall_command = False
                break
        if check_wall_command:
            if 1 <= wall_command [0] <= 8 and 1 <= wall_command[1] <= 9 and 1 <= wall_command[2] <= 9:
                check_wall_command = True
            else:
                check_wall_command = False
        if abs( check_wall_command[1] - check_wall_command[2] ) != 1 :
            check_wall_command = False
    return check_wall_command

def place_wall(wall_command):
    pass        
def refresh_screen():
    clear()
    for row in playground:
        for col in row:
            if col == 2 :
                print(colored(col,"red"),end=" ")
            elif col == 1 :
                print(colored(col,"blue"),end=" ")
            else:
                print(colored(col,"black"),end=" ")
        print()
    print(colored(' ——————————————————————————————',"green"))
    print(colored('|  Up:u Down:d Left:l Right:r  |',"green"))
    print(colored(' ——————————————————————————————',"green"))

def victory_text(pawn):
    print(colored(' ———————————————————————————————',"yellow"))
    print(colored(f'|        Player {pawn} wins !        |',"yellow"))
    print(colored(' ———————————————————————————————',"yellow"))

refresh_screen()
turn = 1
is_running = True
while is_running:
    while True:
        command = input(f"player {turn} move: ").lower()
        if command == "u" or command == "d" or command == "l" or command == "r" :
            check_move(turn,command)
            refresh_screen()
            break
        elif command == "hw" :
            while True:
                wall_command = input(f"player {turn} wall 1 row & 2 columns: ").lower()
                if check_wall(wall_command) :
                    wall_command = list(map(int, wall_command.split()))
                    place_wall(wall_command)
        elif command == "vw" :
            while True:
                wall_command = input(f"player {turn} wall 1 column & 2 rows: ").lower()
        else:
            print(colored("Invalid command, please  try again :","red"))
    if turn == 1 :
        turn = 2
    else :
        turn = 1
    if row1 == 16 :
        victory_text(1)
        is_running = False
    elif row2 == 0 :
        victory_text(2)
        is_running = False