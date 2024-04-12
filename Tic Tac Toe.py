from random import randint

def display_board(row1, row2, row3):
    print(f'{row1}\n{row2}\n{row3}')

def main():

    player = randint(1,2)
    play = True

    while play:
        print(f"Welcome to Tic Tac Toe! Loser's soul goes to the shadow realm. It is your turn now Player {player}")
        row1 = list(range(1,4))
        row2 = list(range(4, 7))
        row3 = list(range(7, 10))
        game(row1,row2,row3,player)
        play = keep_going()


def game(row1, row2, row3, player):
    
    winner = False
    unavailable = set()
    inputs = ['O', 'X']

    while winner == False:

        if len(unavailable) == 9:
            print("Unfortunately it was a draw")
            break

        display_board(row1, row2, row3)
        
        wantedGrid = player_input(player)

        if wantedGrid in unavailable:
            print("Grid already taken, don't be stupid")
        else:
            match wantedGrid:
                case 1:
                    if row1[0] not in inputs:
                        row1[0] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 2:
                    if row1[1] not in inputs:
                        row1[1] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 3:
                    if row1[2] not in inputs:
                        row1[2] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 4:
                    if row2[0] not in inputs:
                        row2[0] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 5:
                    if row2[1] not in inputs:
                        row2[1] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 6:
                    if row2[2] not in inputs:
                        row2[2] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 7:
                    if row3[0] not in inputs:
                        row3[0] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 8:
                    if row3[1] not in inputs:
                        row3[1] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case 9:
                    if row3[2] not in inputs:
                        row3[2] = x_or_o(player)
                        unavailable.add(wantedGrid)
                case _ :
                    print("Nope")

            winner = check_win(row1, row2, row3)

            if not winner:
                player = change_player(player)
            else:
                unavailable.clear()
                print(f"Congratulations Player {player} for winning and not going to the Shadow Realm!")              

def player_input(player):

    grids = range(1,10)
    output = None

    while True:
        try:
            output = int(input(f"Please pick the grid you want Player {player} (1 - 9 only): "))
            if output in grids:
                break
            else:
                print("Please only enter digits between 1 to 9")
        except ValueError:
            print("Please only enter DIGITS between 1 to 9")

    print(f"fOR TEST THEY PUT IN {output}")
    return output

def x_or_o(player):
    if player == 2:
        return 'O'
    else:
        return 'X'

def change_player(player):
    if player == 1:
        return 2
    else:
        return 1
    
def check_win (row1, row2, row3):
    player2win = ['O', 'O', 'O']
    player1win = ['X','X','X']
    
    if row1 == player2win or row2 == player2win or row3 == player2win or row1 == player1win or row2 == player1win or row3 == player1win:
        return True
    elif row1[0] == row2[1] == row3[2]:
        return True
    elif row1[2] == row2[1] == row3[0]:
        return True
    else:
        return False
    
def keep_going():

    while True:
        res = input("Do you want to keep playing? (Y or N): ").upper()
        if res == 'Y':
            return True
        elif res == 'N':
            return False
        else:
            print("Please only key in acceptable responses.")

main()
