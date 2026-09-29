
# Rock, Paper, Scissors Game

## 1. Project Overview

The Rock, Paper, Scissors Game is a simple interactive
game developed using Python.

In this game, the user plays against the computer.
The user chooses Rock, Paper, or Scissors, and the
computer randomly selects one of the three choices.

The program compares both choices and displays
whether the user wins, the computer wins, or the
game is a tie.

The user can play multiple rounds until choosing
to stop the game.

## 2. Project Objectives

- To understand basic Python programming.
- To learn how to create and use functions.
- To understand loops and conditional statements.
- To use the random module.
- To develop a simple interactive game.

## 3. Features

1. User can choose Rock, Paper, or Scissors.
2. Computer randomly selects its choice.
3. Emojis are used to display the choices.
4. The winner is determined automatically.
5. Invalid choices are handled by the program.
6. The user can play multiple rounds.
7. The game can be stopped whenever the user wants.

## 4. Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Module: random

## 5. Python Concepts Used

### 1. Modules

The random module is used to generate the
computer's random choice.

### 2. Functions

The program uses four functions:

- get_user_choice(): Takes and validates the
  user's choice.
- display_choices(): Displays the user's and
  computer's choices using emojis.
- determine_winner(): Compares both choices
  and displays the result.
- play_game(): Controls the main game and
  allows multiple rounds.

### 3. Loops

The while loop allows the user to enter a valid
choice and play the game repeatedly.

### 4. Conditional Statements

if, elif, and else statements are used to
check the choices and determine the winner.

### 5. Dictionary

The Emojis dictionary stores the emojis for
Rock, Paper, and Scissors.

### 6. Tuple

The Choices tuple stores the available choices:
r, p, and s.

### 7. User Input

The input() function takes choices and the
continue decision from the user.

## 6. Rules of the Game

- Rock beats Scissors.
- Paper beats Rock.
- Scissors beats Paper.
- If both choices are the same, it is a tie.

## 7. How to Run the Project

### Requirements

- Python 3 installed on your computer.
- Visual Studio Code or any Python editor.

No external libraries are required.

### Steps

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   python rock_paper_scissors.py

5. Enter r for Rock, p for Paper, or s for
   Scissors.
6. Enter y to continue playing or n to exit.

## 8. Sample Output

Rock, paper, or scissors? (r/p/s) r

You choose 📃
Computer choose ✂️

Computer wins

Continue? (y/n) y

Rock, paper, or scissors? (r/p/s) p

You choose 📃
Computer choose 🪨

You win

Continue? (y/n) n

## 9. Future Improvements

- Add a score counter for the user and computer.
- Display the total number of rounds played.
- Add a graphical user interface.
- Store game results for future reference.

## 10. Author

Name: Sanskriti Rauniayr(26BCE10167)

Course: B.Tech CSE Core

College: VIT Bhopal University

Project: Python Programming
