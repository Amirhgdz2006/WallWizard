from termcolor import colored
import copy
import os
                    
playground = [[" ","|"," ","|"," ","|"," ","|", 2 ,"|"," ","|"," ","|"," ","|"," "],
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
              [" ","|"," ","|"," ","|"," ","|", 1 ,"|"," ","|"," ","|"," ","|"," "]]

playground_original = [[" "," "," "," "," "," "," "," ", 2 ," "," "," "," "," "," "," "," "],
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
                       [" "," "," "," "," "," "," "," ", 1 ," "," "," "," "," "," "," "," "]]

def clear():
    os.system('cls||clear')


row1 , column1 = 16 , 8
row2 , column2 = 0 , 8

wall_player_1 = 10
wall_player_2 = 10
    
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
                
            elif 0 <= row1 - 2 <= 16 :
                if row2 + 2 == row1 and column2  == column1:
                    playground[row1][column1] = " "
                    playground_original[row1][column1] = " "
                    row1 -= 4
                    playground[row1][column1] = 1
                    playground_original[row1][column1] = 1
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
            elif 0 <= row2 - 2 <= 16 :
                if row1 + 2 == row2 and column2  == column1:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    row2 -= 4
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
        return playground

    def move_down():
        global row1,column1,row2,column2
        if pawn == 1:
            if row1 != 16:
                if row1 != 16 and playground_original[row1 + 1][column1] == 0 :
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
                        else:
                            print(colored("Invalid command, please  try again","red"))
                elif 0 <= row1 + 2 <= 16 :
                    if row1 + 2 == row2 and column2  == column1:
                        playground[row1][column1] = " "
                        playground_original[row1][column1] = " "
                        row1 += 4
                        playground[row1][column1] = 1
                        playground_original[row1][column1] = 1
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
                        else:
                            print(colored("Invalid command, please  try again","red"))
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
            elif 0 <= row2 + 2 <= 16 :
                if row2 + 2 == row1 and column2  == column1:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    row2 += 4
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
        return playground

    def move_right():
        global row1,column1,row2,column2
        if pawn == 1:
            if column1 != 16 :
                if playground_original[row1][column1 + 1] == 0 :
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
                        else:
                            print(colored("Invalid command, please  try again","red"))
                elif 0 <= column1 + 2 <= 16 :
                    if column2  == column1 + 2 and row1 == row2:
                        playground[row1][column1] = " "
                        playground_original[row1][column1] = " "
                        column1 += 4
                        playground[row1][column1] = 1
                        playground_original[row1][column1] = 1
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
                        else:
                            print(colored("Invalid command, please  try again","red"))
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
        elif pawn == 2:
            if column2 != 16 :
                if playground_original[row2][column2 + 1] == 0 :
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
                        else:
                            print(colored("Invalid command, please  try again","red"))
                elif 0 <= column2 + 2 <= 16 :
                    if column2 + 2 == column1 and row1 == row2:
                        playground[row2][column2] = " "
                        playground_original[row2][column2] = " "
                        column2 += 4
                        playground[row2][column2] = 2
                        playground_original[row2][column2] = 2
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
                        else:
                            print(colored("Invalid command, please  try again","red"))
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
        return playground

    def move_left():
        global row1,column1,row2,column2
        if pawn == 1:
            if playground_original[row1][column1 - 1] == 0 :
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
            elif 0 <= column1 - 2 <= 16  :
                if column2 + 2 == column1 and row1 == row2:
                    playground[row1][column1] = " "
                    playground_original[row1][column1] = " "
                    column1 -= 4
                    playground[row1][column1] = 1
                    playground_original[row1][column1] = 1
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
        elif pawn == 2:
            if playground_original[row2][column2 - 1] == 0 :
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
            elif 0 <= column2 - 2 <= 16 :
                if column1 + 2 == column2 and row1 == row2:
                    playground[row2][column2] = " "
                    playground_original[row2][column2] = " "
                    column2 -= 4
                    playground[row2][column2] = 2
                    playground_original[row2][column2] = 2
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
                    else:
                        print(colored("Invalid command, please  try again","red"))
        return playground



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
    print(colored('|—————————————————————————————————|',"light_green"))
    print(colored('|   player 1 walls : ',"light_green"),colored(f"{wall_player_1:02}","light_yellow"),colored('         |',"light_green"))
    print(colored('|   player 2 walls : ',"light_green"),colored(f"{wall_player_2:02}","light_yellow"),colored('         |',"light_green"))
    print(colored(' ————————————————————————————————— ',"light_green"))



def victory_text(pawn):
    print(colored(' ——————————————————————————————— ',"black","on_yellow"),)
    print(colored(f'|        Player {pawn} wins !        |',"black","on_yellow"))
    print(colored(' ——————————————————————————————— ',"black","on_yellow"))

refresh_screen()
turn = 1
is_running = True
while is_running:
    print()
    if turn == 1:
        print(colored(f"         Player one's turn         ", "blue" , "on_light_cyan" , attrs = ["bold"]))
    else :
        print(colored(f"         Player two's turn         ", "white" , "on_red" , attrs = ["bold"]))

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
        else:
            print(colored("Invalid command, please  try again","red"))
    if turn == 1 :
        turn = 2
    else :
        turn = 1
    if row1 == 0 :
        victory_text(1)
        is_running = False
    elif row2 == 16 :
        victory_text(2)
        is_running = False