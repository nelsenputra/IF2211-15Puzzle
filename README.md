# Tucil Stima 3 by Nelsen Putra
> 15-Puzzle solver written in Python. Based on the concept of Branch and Bound algorithm.


## Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Library](#library)
* [Contact](#contact)


## Introduction
Hello, everyone! Welcome to my GitHub Repository!

This project was created by:
| Name | Student ID | Class |
| :---: | :---: | :---: |
| Nelsen Putra | 13520130 | IF2211-01


## General Information
15-Puzzle is a game using a board containing the numbers 1 to 15 spread over 16 tiles. There is one empty tile that you can move up, down, left, and right to indirectly move the position of the other tiles. The goal of this game is to arrange the numbers 1 to 15 in order from left to right and top to bottom by sliding or moving the empty tile.

One approach to solve the 15-Puzzle problem is to use and implement the Branch and Bound algorithm. Branch and Bound algorithm is one of the algorithm strategies used to solve optimization problems. This algorithm uses a state space tree to search for the best solution. The journey in searching the solution state of the above problem uses the most optimal effort.

In implementing the Branch and Bound algorithm, the bound value of each node is the sum of the costs required to arrive at a node x from the root, with the estimated cost of node x to get to the goal. The estimated cost used is the number of non-empty tiles that are not in place according to the final arrangement (goal state).


## Technologies Used
The whole program was written in Python.


## Setup
### Installation
- Download and install [Python](https://www.python.org/downloads/)
- Install the whole modules and [libraries](#library) used in the source code
- Download the whole folders and files in this repository or do clone the repository

### Execution
1. Clone this repository in your own local directory

    `git clone https://github.com/nelsenputra/IF2211-15Puzzle.git`

2. Open the command line and change the directory to 'IF2211-15Puzzle' folder

    `cd IF2211-15Puzzle`
    
3. Run `python gui.py` on the command line


## Usage
### Interface
The 15-Puzzle solver were made using a Graphical User Intercafe (GUI) whose input and output can be directly done on the GUI. The program can also export a .txt file that is the result of the puzzle solving steps. The buttons on the GUI include:
1. Select File: select the .txt input file from the user directory
2. Solve: direct the user to the solution from the input given by the user
3. Export Solution: export/save step-by-step solutions
4. Show Details: show the details of the results of program execution such as the value of kurang function in each iteration, the sum of kurang function, the generated nodes, and the program execution time.
5. Visualize: visualize the resulting solution steps in the form of empty tile shifting on the puzzle
6. Reset: reset the shape of the puzzle arrangement to the initial arrangement (according to the puzzle form from user input)

### File Input
The input file has the following rules:
1. The contents of the file consist of exactly 4 lines
2. Each line contains exactly 4 numbers separated by spaces
3. The number contained in the input is a permutation of 0..15
4. The empty cells in the puzzle are represented by the number 0 in the input file


## Project Status
Project is: _complete_

All the specifications were implemented, including bonus.


## Room for Improvement
- A faster or more efficient algorithm to make the program run quicker
- A better interface development to satisfy the users


## Acknowledgements
- This project was based on [Spesifikasi Tugas Kecil 3 Stima](http://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2021-2022/Tugas-Kecil-3-(2022).pdf)
- Thanks to God
- Thanks to Mrs. Masayu Leylia Khodra, Mrs. Nur Ulfa Maulidevi, and Mr. Rinaldi as our lecturers
- Thanks to academic assistants
- This project was created to fulfill our Small Project for IF2211 Algorithm Strategies


## Library
- [heapq](https://docs.python.org/3/library/heapq.html)
- [copy](https://docs.python.org/3/library/copy.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [os](https://docs.python.org/3/library/os.html)
- [time](https://docs.python.org/3/library/time.html)


## Contact
Created by Nelsen Putra. 2022 All Rights Reserved.
