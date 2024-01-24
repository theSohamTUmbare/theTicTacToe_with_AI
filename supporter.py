def draw_board(boxes):
    board = (f" | {boxes[1]} | {boxes[2]} | {boxes[3]} |\n"
             f" | {boxes[4]} | {boxes[5]} | {boxes[6]} |\n"
             f" | {boxes[7]} | {boxes[8]} | {boxes[9]} |")
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def check_for_win(boxes):
    # Horizontally
    if (boxes[1] == boxes[2] == boxes[3]) \
            or (boxes[4] == boxes[5] == boxes[6]) \
            or (boxes[7] == boxes[8] == boxes[9]):
        return True
    # Vertically
    elif (boxes[1] == boxes[4] == boxes[7]) \
            or (boxes[2] == boxes[5] == boxes[8]) \
            or (boxes[3] == boxes[6] == boxes[9]):
        return True
    # Diagonal
    elif (boxes[1] == boxes[5] == boxes[9]) \
            or (boxes[3] == boxes[5] == boxes[7]):
        return True
    else:
        return False


def winner(boxes):
    winner = None
    if check_for_win:
        if (boxes[1] == boxes[2] == boxes[3]) \
                or (boxes[1] == boxes[4] == boxes[7]) \
                or (boxes[1] == boxes[5] == boxes[9]):
            winner = boxes[1]
        elif (boxes[4] == boxes[5] == boxes[6]) \
                or (boxes[2] == boxes[5] == boxes[8]) \
                or (boxes[3] == boxes[5] == boxes[7]):
            winner = boxes[5]
        elif (boxes[7] == boxes[8] == boxes[9]) \
                or (boxes[3] == boxes[6] == boxes[9]):
            winner = boxes[9]

    return winner

##-just marking boxes serially------------------------------------------------------------------------------------------
def no_ai(boxes):
    for i in boxes:
        if boxes[i] != 'X' and boxes[i] != 'O':
            return i
#-----------------------------------------------------------------------------------------------------------------------

def bestMove(boxes, ai, human):
    print(ai)
    bestMove = 0
    # who is first - who is Maximizer?        ## 'X'-is-1st=&='O'-is-2nd ##       # first_Player is Maximizer
    if ai == 'X':
        first_Player = ai
        second_Player = human
    else:
        first_Player = human   # X
        second_Player = ai     # O


    if first_Player == ai:
        # AI to make moves
        bestScore = -9999999999

        for i in boxes:
            # is spot available
            if boxes[i] != 'X' and boxes[i] != 'O':
                boxes[i] = ai
                score = minimax(boxes, 0, False, first_Player, second_Player)           # first_Player == Maximizer
                     ## Here we called minimax(..., False, ...) because first_Player[Maximizer] played its move now its
                     ## 2nd players move so it is  False the minimizer
                boxes[i] = i
                if score > bestScore:    # >
                    bestScore = score
                    bestMove = i
    else:
        bestScore = 9999999999
        for i in boxes:
            # is spot available
            if boxes[i] != 'X' and boxes[i] != 'O':
                boxes[i] = ai
                score = minimax_AI_O(boxes, 0, True, first_Player, second_Player)           # first_Player == Maximizer
                     ## Here we called minimax(..., False, ...) because first_Player[Maximizer] played its move now its
                     ## 2nd players move so it is  False the minimizer
                boxes[i] = i
                if score < bestScore:
                    bestScore = score
                    bestMove = i
    return bestMove



scores = {'X': 1000, 'O': -1000, 'tie': 0}


""""this is the minimax function when ai makes 1st 
    it is easy because here ai only think about best move for itself 
    ai doesn't need to defend because he have 1st turn but it will not work if ai have 2nd turn in game"""
def minimax(boxes, dept, isMaximizing, first_Player, second_Player):
    result = winner(boxes)
    if result != None:
        return(scores[result])

    if isMaximizing:
        bestScore = -9999999999
        for i in boxes:
            if boxes[i] != 'X' and boxes[i] != 'O':
                boxes[i] = first_Player
                score = minimax(boxes, dept + 1, False, first_Player,
                                second_Player)  # after the maximizing players turn its minimizing players turn
                boxes[i] = i
                if score > bestScore:
                    bestScore = score

        return bestScore
    else:
        bestScore = 9999999999
        for i in boxes:
            if boxes[i] != 'X' and boxes[i] != 'O':
                boxes[i] = second_Player
                score = minimax(boxes, dept + 1, True, first_Player,
                                second_Player)  # after the minimizing players turn its maximizing players turn
                boxes[i] = i
                if score < bestScore:
                    bestScore = score

        return bestScore


""" this is minimax fuction when ai has second move that is O 
    so now ai is minimizer"""


def minimax_AI_O(boxes, dept, isMaximizing, first_Player, second_Player):
    result = winner(boxes)

    # Immediate win or loss takes priority
    if result != None:
        return scores[result]


    # Check for immediate wins, blocks, and forks
    if isMaximizing:
        bestScore = -9999999999
        for i in boxes:
            if boxes[i] != 'X' and boxes[i] != 'O':
                boxes[i] = first_Player
                score = minimax_AI_O(boxes, dept + 1, False, first_Player, second_Player)
                boxes[i] = i

                # Prioritize immediate wins, blocks, and forks
                if check_for_win(boxes):
                    return 1000  # Very high score for immediate win
                elif check_win_threat(boxes, second_Player):
                    bestScore = 900  # High score for blocking a win
                elif check_fork(boxes, first_Player):
                    bestScore = 800  # High score for creating a fork

                if (bestScore == score):
                    bestScore = bestScore - 0.1
                else:
                    bestScore = max(score, bestScore)

        return bestScore
    else:
        bestScore = 9999999999
        if the_Tie(boxes):
            bestScore = 0
        for i in boxes:
            if boxes[i] != 'X' and boxes[i] != 'O':
                # print("Y")
                boxes[i] = second_Player
                score = minimax_AI_O(boxes, dept + 1, True, first_Player, second_Player)
                boxes[i] = i

                # Prioritize immediate wins, blocks, and forks
                # if check_for_win(boxes):
                #     return -1000  # Very high score for immediate win
                if check_win_threat(boxes, first_Player):
                    bestScore = -900  # High score for blocking a win
                elif check_fork(boxes, second_Player):
                    bestScore = -800  # High score for creating a fork

                if(bestScore == score):
                    bestScore = bestScore + 0.1
                else:
                    bestScore = min(score, bestScore)
                print(str(i)+" "+str(bestScore))
        return bestScore

def check_immediate(boxes, a, b, c, oppenant):   # you can add player in argument of this function
    flag_O = 0
    flag_X = 0
    if boxes[a] == 'X':
        flag_X += 1
    elif boxes[a] == 'O':
        flag_O += 1

    if boxes[b] == 'X':
        flag_X += 1
    elif boxes[b] == 'O':
        flag_O += 1

    if boxes[c] == 'X':
        flag_X += 1
    elif boxes[c] == 'O':
        flag_O += 1

    if oppenant == 'O':        ##X is making decision
        if flag_O == 2 and flag_X == 1:
            return True
    else:
        if flag_X == 2 and flag_O == 1:
            return True

    return False


def check_fork_helper(boxes, a,b,c,plyer, oppe):
    flag_plyer = 0
    if boxes[a] == oppe:
        return 0
    elif boxes[a] == plyer:
        flag_plyer += 1

    if boxes[b] == oppe:
        return 0
    elif boxes[b] == plyer:
        flag_plyer += 1

    if boxes[c] == oppe:
        return 0
    elif boxes[c] == plyer:
        flag_plyer += 1

    if flag_plyer == 2:
        return 1
    return 0


def check_win_threat(boxes, second_Player):

    if check_immediate(boxes, 1, 2, 3, second_Player) or check_immediate(boxes, 4,5,6, second_Player) \
            or check_immediate(boxes, 7,8,9,second_Player) or check_immediate(boxes, 1,4,7, second_Player) \
            or check_immediate(boxes, 2,5,8, second_Player) or check_immediate(boxes,3,6,9, second_Player) \
            or check_immediate(boxes,1,5,9, second_Player) or check_immediate(boxes,3,5,7,second_Player):
        return True
    else: return False


def check_fork(boxes, first_Player):
    if first_Player == 'X':
        oppen = 'O'
    else:
        oppen = 'X'
    fork =check_fork_helper(boxes,1, 2, 3, first_Player, oppen) + check_fork_helper(boxes, 4,5,6,first_Player, oppen) +\
          check_fork_helper(boxes, 7,8,9, first_Player, oppen) + check_fork_helper(boxes, 1,4,7, first_Player, oppen) +\
          check_fork_helper(boxes, 2,5,8, first_Player, oppen) + check_fork_helper(boxes,3,6,9, first_Player, oppen) +\
          check_fork_helper(boxes, 1, 5, 9, first_Player, oppen) + check_fork_helper(boxes,3,5,7,first_Player, oppen)

    if fork >= 2:
        return True
    return False

def the_Tie(boxes):
    if not (check_for_win(boxes)):
        flag = 0
        for i in boxes:
            if boxes[i] != 'X' and boxes[i] != 'O':  ## some place empty
                flag = 1
        if flag == 0:
            return True

    return False


# ----------------------------------NOT tic-tac-toe---------------------------------------------------------------------
