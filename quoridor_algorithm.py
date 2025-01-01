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
            if playground_original[row1][column1 - 1] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
            elif 0 <= column1 - 2 <= 16  :
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
            if playground_original[row2][column2 - 1] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
            elif 0 <= column2 - 2 <= 16 :
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
            if playground_original[row1][column1 + 1] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
            elif 0 <= column1 + 2 <= 16 :
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
            if playground_original[row2][column2 + 1] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
            elif 0 <= column2 + 2 <= 16 :
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
            if playground_original[row1 - 1][column1] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
            elif 0 <= row1 - 2 <= 16 :
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
            if playground_original[row2 - 1][column2] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
            elif 0 <= row2 - 2 <= 16 :
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
            if playground_original[row1 + 1][column1] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(1,command)
            elif 0 <= row1 + 2 <= 16 :
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
            if playground_original[row2 + 1][column2] == 0 :
                print(colored("Move blocked by wall, please try again :","red"))
                while True:
                    command = input(f"player {turn} move: ").lower()
                    if command == "u" or command == "d" or command == "l" or command == "r" :
                        break
                    else:
                        print(colored("Invalid command, please  try again :","red"))
                check_move(2,command)
            elif 0 <= row2 + 2 <= 16 :
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

    def place_wall(list_command):
        list_command = [list_command[0] * 2 - 1 , list_command[1] * 2 - 1 , list_command[2]]
        playground_original[list_command[0]][list_command[1]] = 0
        if list_command[2] == "h":
            playground_original[list_command[0]][list_command[1] - 1] = 0
            playground_original[list_command[0]][list_command[1] + 1] = 0
        elif list_command[2] == "v":
            playground_original[list_command[0] - 1][list_command[1]] = 0
            playground_original[list_command[0] + 1][list_command[1]] = 0

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
            if wall_command[2] == "h":
                if playground_original[wall_command[0] * 2 - 1][wall_command[1] - 1] != 0 and playground_original[wall_command[0] * 2 - 1][wall_command[1] * 2] != 0 and playground_original[wall_command[0] * 2 - 1][wall_command[1] * 2 - 2] != 0:
                    check_wall_command = True
                else:
                    check_wall_command = False
            elif wall_command[2] == "v":
                if playground_original[wall_command[0] * 2 - 1][wall_command[1] * 2 - 1]!= 0 and playground_original[wall_command[0] * 2][wall_command[1] * 2 - 1]!= 0 and playground_original[wall_command[0] * 2 - 2][wall_command[1] * 2 - 1]!= 0:
                    check_wall_command = True
                else:
                    check_wall_command = False


    if check_wall_command:
        wall_command = [int(wall_command[0]),int(wall_command[1]),wall_command[2]]
        place_wall(wall_command)
    else :
        print(colored("Invalid wall, please  try again :","red"))
        wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
        check_wall(wall_command)
       
def refresh_screen():
    clear()
    for row in range(17):
        for col in range(17):
            if playground[row][col] == 2 :
                print(colored(playground[row][col],"red"),end=" ")
            elif playground[row][col] == 1 :
                print(colored(playground[row][col],"blue"),end=" ")
            elif playground_original[row][col] == 0 :
                print(colored(playground[row][col],"yellow"),end=" ")
            else:
                print(colored(playground[row][col],"black"),end=" ")
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
        elif command == "wall":
            wall_command = input("Enter wall command ( center row , center column , direction(h/v) ): ").lower()
            check_wall(wall_command)
            refresh_screen()
            break
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