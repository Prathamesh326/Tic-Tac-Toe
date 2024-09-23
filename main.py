# Function to print board
def print_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("--------------------------------")
    print("            SCOREBOARD       ")
    print("--------------------------------")

    players = list(score_board.keys())
    print("   ", players[0], "    ", score_board[players[0]])
    print("   ", players[1], "    ", score_board[players[1]])

    print("--------------------------------\n")


# function to check if any player has won
def check_win(player_pos, cur_player):
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]

    for i in soln:
        if all(y in player_pos[cur_player] for y in i):
            return True
    return False


def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


# Function for a single game
def single_game(cur_player):
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    while True:
        print_board(values)

        try:
            move = int(input(f'Player {cur_player} turn. Which box? : '))
        except ValueError:
            print("Wrong Input!! Try again")
            continue

        if move < 1 or move > 9:
            print("Wrong Input!! Try again")
            continue

        if values[move - 1] != ' ':
            print("The place is already filled, Try again!!!")

        # Update game information
        values[move - 1] = cur_player
        player_pos[cur_player].append(move)

        # Check win or draw
        if check_win(player_pos, cur_player):
            print_board(values)
            print(f"Player {cur_player} has won the game!")
            print("\n")
            return cur_player

        if check_draw(player_pos):
            print_board(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player move
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == '__main__':
    print("Player 1")
    P1 = input("Enter your name : ")
    print("\n")

    print("Player 2")
    P2 = input("Enter your name : ")
    print("\n")

    # Stores the player who chooses X and O
    cur_player = P1

    # Stores the choice of players
    player_choice = {'X': "", "O": ""}

    # Stores the option
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {P1: 0, P2: 0}
    print_scoreboard(score_board)

    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit
    while True:
        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] == cur_player
            if cur_player == P1:
                player_choice['O'] == P2
            else:
                player_choice['O'] == P1

        elif choice == 2:
            player_choice['O'] == cur_player
            if cur_player == P1:
                player_choice['X'] == P2
            else:
                player_choice['X'] == P1

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice !!! Try again\n")

        # Store the winner of a single game
        winner = single_game(options[choice - 1])

        # edit the scoreboard acc'n to winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == P1:
            cur_player = P2
        else:
            cur_player = P1
