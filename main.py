import os
from supporter import check_turn, check_for_win, draw_board, no_ai, bestMove
switch = input("Press t to Play Double Player tic-tac-toe: ")

while switch == 't':
    # Declaring all variables
    boxes = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}
    playing, complete = True, False
    turn = 0
    prev_turn = -1

    # the main loop
    while playing:
        # Reset
        # os.system('cls' if os.name == 'nt' else 'clear')
        # draw the current game board
        draw_board(boxes)

        # if invalid display the message
        if prev_turn == turn:
            print("Invalid selection, pick another box.")

        prev_turn = turn
        print("Player " + str(check_turn((turn % 2) + 1)) + " 's turn: Select your box or press q to quit")

        # Get valid input
        selection = input()
        # exit case
        if selection == 'q':
            playing = False
            switch = 'q'
        elif str.isdigit(selection) and int(selection) in boxes:
            # check if box is empty or NOT
            if not boxes[int(selection)] in {"X", "O"}:  # player 1  ==> X
                turn += 1
                boxes[int(selection)] = check_turn(turn)

        # check if Game is ended and/or someone has won
        if check_for_win(boxes): playing, complete = False, True
        if turn > 8:
            playing = False
            switch = 'q'

    # Update the Board last time
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(boxes)
    # if there is a winner
    if complete:
        if check_turn(turn) == 'X':
            print("Player 1 is WINNER!!!\n  Next Round? ")
        else:
            print("Player 2 is WINNER!!!\n  Next Round? ")
        switch = input("Press 't' to try again else press q to exit...")
    else:
        # Tie
        print("No one is Winner Try Again!\n  Next Round? ")


"""" Single Player tic tac to against the minMAX algorithm """

while switch == 'a':
    boxes = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}
    playing, complete = True, False
    turn = 0
    prev_turn = -1

    # choose
    choos = input("Press 1 for 'O' and 2 for 'X': ")
    if choos != '1' and choos != '2':
        choos = '1'
    human_player = int(choos) - 1  # if 1 => 0  ie X  |  if 2 => 1 ie O
    # the loop
    while playing:
        # reset
        os.system('cls')
        # draw the current game
        draw_board(boxes)
        # if invalid
        if prev_turn == turn:
            print("Invalid selection, pick another box.")

        prev_turn = turn

        if ((turn % 2) + 1) % 2 == human_player:  # Human Player's turn
            print("Player " + str(check_turn(human_player)) + " 's turn: Select your box or press q to quit")
            # Get input
            selection = input()
            if selection == 'q':
                playing = False
                switch = 'q'
            elif str.isdigit(selection) and int(selection) in boxes:
                # check box is empty or not
                if not boxes[int(selection)] in {'X', 'O'}:
                    turn += 1
                    boxes[int(selection)] = check_turn(turn)

            if check_for_win(boxes): playing, complete = False, True
            if turn > 8: playing = False
        else:
            ##print("Player " + str(check_turn(human_player + 1)) + " 's turn: Select your box or press q to quit")
            # --------------------------------------------------------------------------------------------------------
            ## Get input
            # selection = no_ai(boxes)
            selection = bestMove(boxes, check_turn(human_player + 1), check_turn(human_player))  # boxes, ai, human
            # --------------------------------------------------------------------------------------------------------

            turn += 1
            boxes[int(selection)] = check_turn(turn)

            if check_for_win(boxes): playing, complete = False, True
            if turn > 8:
                playing = False
                switch = 'q'

            # best move

        # Update the Board last time
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(boxes)
    # if there is a winner
    if complete:
        if check_turn(turn) == 'X':
            print("Player X is WINNER!!!\n  Next Round? ")
        else:
            print("Player O is WINNER!!!\n  Next Round? ")
        switch = input("Press 'a' to try again else press q to exit...")
    else:
        # Tie
        print("No one is Winner Try Again!\n  Next Round? ")


# """my game"""
#
# while switch=='b':
#     boxes = {1: 'O', 2: 'X', 3: 'O', 4: 'X', 5: 'O', 6: 'X',
#              7: '7', 8: '8', 9: '9'}
#     playing, complete = True, False
#     turn = 0
#     prev_turn = -1
#
#     # choose
#     choos = input("Press 1 for 'O' and 2 for 'X': ")
#     if choos != '1' and choos != '2':
#         choos = '1'
#     human_player = int(choos) - 1  # if 1 => 0  ie X  |  if 2 => 1 ie O
#     # the loop
#     while playing:
#         # reset
#         os.system('cls')
#         # draw the current game
#         draw_board(boxes)
#         # if invalid
#         if prev_turn == turn:
#             print("Invalid selection, pick another box.")
#
#         prev_turn = turn
#
#         if ((turn % 2) + 1) % 2 == human_player:  # Human Player's turn
#             flag = 0
#
#             print("Player " + str(check_turn(human_player)) + " 's turn: Select your box to add or press q to quit")
#             # Get input1
#             selection1 = input()
#             if selection1 == 'q':
#                 playing = False
#                 switch = 'q'
#             elif str.isdigit(selection1) and int(selection1) in boxes:
#                 # check box is empty or not
#                 if not boxes[int(selection1)] in {'X', 'O'}:
#                     flag += 1
#
#             print("Player " + str(check_turn(human_player)) + " 's turn: Select your box to remove")
#             # get input2
#             selection2 = input()
#             if str.isdigit(selection2) and int(selection2) in boxes:
#                 if boxes[int(selection2)] in {'X', 'O'}:
#                     flag +=1
#
#             if flag == 2:
#                 turn += 1
#                 boxes[int(selection1)] = check_turn(turn)
#                 boxes[int(selection2)] = int(selection2)
#
#             if check_for_win(boxes): playing, complete = False, True
#         else:
#             ## Get input1
#             selection1 = bestMove(boxes, check_turn(human_player + 1), check_turn(human_player))  # boxes, ai, human
#             ##Get input2
#             selection2 = bestRemove(boxes, check_turn(human_player + 1), check_turn(human_player))
#             # --------------------------------------------------------------------------------------------------------
#
#             turn += 1
#             boxes[int(selection1)] = check_turn(turn)
#             boxes[int(selection2)] = int(selection2)
#             print(selection2)
#
#             if check_for_win(boxes): playing, complete = False, True
#
#
#         # Update the Board last time
#     os.system('cls' if os.name == 'nt' else 'clear')
#     # if there is a winner
#     if complete:
#         if check_turn(turn) == 'X':
#             print("Player X is WINNER!!!\n  Next Round? ")
#         else:
#             print("Player O is WINNER!!!\n  Next Round? ")
#         switch = input("Press 'a' to try again else press q to exit...")
#     else:
#         # Tie
#         print("Try Again!\n  Next Round? ")


print("Thanks for playing!")


