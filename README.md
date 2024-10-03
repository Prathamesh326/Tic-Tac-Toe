# Tic-Tac-Toe Game

This repository contains a **Tic-Tac-Toe** game written in Python. The game allows two players to compete in a series of Tic-Tac-Toe games while tracking their scores.

## How the game works
1. The game alternates between two players, with one player being "X" and the other "O".
2. The players take turns selecting a position on the 3x3 grid.
3. The first player to get three in a row (horizontally, vertically, or diagonally) wins the game.
4. If all nine boxes are filled and no player has won, the game is declared a draw.
5. A scoreboard keeps track of the players' victories in the series.

## How to Run the Game

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Prathamesh326/Tic-Tac-Toe.git
   ```

2. **Navigate to the directory**:

   ```bash
   cd Tic-Tac-Toe
   ```

3. **Run the game**:

   ```bash
   python3 main.py
   ```

## Features

- **Multiplayer Support**: Two players can play the game locally by taking turns.
- **Scoreboard**: A scoreboard keeps track of how many games each player has won.
- **Input Validation**: The game includes input validation to ensure players provide valid moves.
- **End Game Options**: Players can quit the game at any point and view the final scores.

## Functions Overview

- **print_board(values)**: Prints the Tic-Tac-Toe board after each move.
- **print_scoreboard(score_board)**: Displays the current score between the two players.
- **check_win(player_pos, cur_player)**: Checks if the current player has won.
- **check_draw(player_pos)**: Checks if the game has ended in a draw.
- **single_game(cur_player)**: Runs a single game, handling player moves, checking for wins, and drawing the board.

## Example Gameplay

- Players enter their names.
- One player chooses to be "X" or "O".
- Players take turns selecting positions on the grid.
- After each game, the winner is declared, or the game ends in a draw.
- The scoreboard is updated after each round, and players can continue playing until they choose to quit.

## Future Improvements
- Implement an AI-based single-player mode.
- Add a graphical user interface (GUI) using libraries like `tkinter` or `pygame`.
- Enhance input validation and error handling for smoother gameplay.

## Contributions
Feel free to open issues and submit pull requests if you'd like to improve the code.

For those interested in learning more about game development in Python, check out resources like:
- [Python Game Development Tutorials](https://realpython.com/tutorials/game-development/)
- [An Introduction to Pygame](https://www.pygame.org/docs/)

For deeper research into game algorithms, you may explore the **Minimax Algorithm** for building AI for Tic-Tac-Toe:
- **[Research paper on Minimax Algorithm](https://arxiv.org/abs/1305.1124)**
