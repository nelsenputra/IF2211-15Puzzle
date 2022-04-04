# gui.py
# Source code program untuk Graphical User Interface (GUI)

# IMPORT LIBRARY DAN PUZZLE
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter
import os
import time
from puzzle import *
from tkinter.messagebox import showinfo

# INISIALISASI VARIABEL GLOBAL
# Detail untuk memecahkan puzzle
tempKurang = []
valueKurang = 0
tempX = []
minimumCost = 0
duration = 0
total = 0

# File input
file = ""

# Default config untuk animasi puzzle
puzzleLabels = [[0 for i in range(4)] for j in range(4)]
puzzleInit = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
zeroPos = (3, 3)
tempMoves = []

'''
/* *** PUZZLE LABEL *** */
** Visualizer puzzle yang akan dijadikan sebagai interface untuk output dari GUI
'''
def puzzleLable():
    for i in range(4):
        for j in range(4):
            puzzleLabels[i][j] = Label(root, text = str(i * 4 + j + 1), font = ('Arial', 9),
                height = 1, width = 2, anchor = CENTER,
                borderwidth = 2, relief = "solid", bg = 'yellow')
            puzzleLabels[i][j].place(x = 110 + 20 * j, y = 120 + 20 * i)
    puzzleLabels[3][3].config(text = " ")

'''
/* *** SOLVE CALLER *** */
** Fungsi untuk mengeksekusi puzzle dengan memanggil fungsi solve yang dapat memecahkan 
** puzzle dengan menggunakan algoritma Branch and Bound
'''
def solveCaller():
    global puzzleInit, zeroPos, moves, puzzleLabels
    global tempKurang, valueKurang, X, minimumCost, duration, total

    visualize_button.place_forget()
    reset_button.place_forget()

    if (len(file) != 0):
        psolver = Puzzle(file)
        if (len(psolver.puzzle) != 0):
            showinfo('Solution', 'Please Wait...')
            root.update()
            start = time.time()
            # Memanggil fungsi solve untuk memecahkan puzzle menggunakan algoritma Branch and Bound
            valueKurang = psolver.solve()
            end = time.time()
            print('Done')
            duration = end - start
            if ((valueKurang % 2) == 0):    
                showinfo('Solution', 'The Solution has founded!')
                puzzleInit = copy.deepcopy(psolver.puzzle)
                moves = copy.deepcopy(psolver.solution)
                visualize_button.place(x = 110, y = 220)
                reset_button.place(x = 185, y = 255)
            else:
                showinfo('Solution', 'The puzzle doesn\'t have any solution!')
                puzzleInit = copy.deepcopy(psolver.puzzle)
                moves = []
            tempKurang = copy.deepcopy(psolver.tempKurang)
            X = psolver.valueX
            minimumCost = psolver.minimumCost
            total = psolver.total
            details_button.place(x = 35, y = 255)
            resetPuzzle()
        else:
            showinfo('Solution', 'File config invalid!')
            return
    else:
        showinfo('Solution', 'File config invalid!')
        return

'''
/* *** SELECT FILE *** */
** Fungsi untuk mengambil input file dari folder test yang ada di directory
'''
def selectFile():
    global file
    fileType = (('text files', '*.txt'), ('All files', '*.*'))
    name = fd.askopenfilename(title = 'Open a file', initialdir = './test/input', filetypes = fileType)
    filename_label.config(text = "File config: " + os.path.basename(name))
    file = name

'''
/* *** SAVE FILE *** */
** Fungsi untuk menyimpan hasil solusi dari problem 15-Puzzle berupa langkah-langkah penyelesaiannya
'''
def saveFile():
    puzzle = puzzleInit
    zeroPosY = zeroPos[0]
    zeroPosX = zeroPos[1]
    count = 0
    if (len(moves) > 0):
        f = fd.asksaveasfile(initialfile = 'Untitled.txt', defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
        f.write("SOLUTION STEPS: \n")
        f.write("\n")
        for dxy in moves:
            count += 1
            f.write(str(count) + " ")
            if ((dxy[0] == -1) and (dxy[1] == 0)):
                f.write("UP\n")
            elif ((dxy[0] == 0) and (dxy[1] == -1)):
                f.write("LEFT\n")
            elif ((dxy[0] == 1) and (dxy[1] == 0)):
                f.write("DOWN\n")
            elif ((dxy[0] == 0) and (dxy[1] == 1)):
                f.write("RIGHT\n")
            f.write("===============================\n")
            # SWAP
            temp = puzzle[zeroPosY][zeroPosX]
            puzzle[zeroPosY][zeroPosX] = puzzle[dxy[0] + zeroPosY][dxy[1] + zeroPosX]
            puzzle[dxy[0] + zeroPosY][dxy[1] + zeroPosX] = temp
            for i in range(len(puzzle)):
                for j in range(len(puzzle[i])):
                    f.write(str(puzzle[i][j]) + " ")
                f.write("\n")
            f.write("\n")
            zeroPosY = dxy[0] + zeroPosY
            zeroPosX = dxy[1] + zeroPosX
    else:
        showinfo('Warning', 'Input is invalid')

'''
/* *** RESET PUZZLE *** */
** Fungsi untuk me-reset hasil visualisasi dari langkah-langkah penyelesaian 15-Puzzle
'''
def resetPuzzle():
    global zeroPos
    for i in range(4):
        for j in range(4):
            if (puzzleInit[i][j] != 0):
                puzzleLabels[i][j].config(text = str(puzzleInit[i][j])) 
            else:
                zeroPos = (i, j)
                puzzleLabels[i][j].config(text = "")
    root.update()     

'''
/* *** VISUALIZE *** */
** Button untuk melakukan visualisasi dengan memanggil fungsi solveCaller
'''
def visualize():
    global puzzleLabels
    resetPuzzle()
    zero = copy.deepcopy(zeroPos)
    puzzle = copy.deepcopy(puzzleInit)
    for dxy in moves:
        time.sleep(1)
        dx, dy = dxy
        zx, zy = zero
        puzzle[zx][zy], puzzle[zx+dx][zy+dy] = puzzle[zx+dx][zy+dy], puzzle[zx][zy]
        puzzleLabels[zx+dx][zy+dy].config(text = "")
        puzzleLabels[zx][zy].config(text = str(puzzle[zx][zy]))
        zero = (zx + dx, zy + dy)
        root.update()

'''
/* *** SHOW DETAILS *** */
** Button untuk menampilkan detail dari solusi
'''
def showDetails():
    INFO = "====== KURANG(i) ======\n"
    for i in range(1, 17):
        if (i < 16):
            INFO += "Value of KURANG(" + str(i) + ")"  + ": " + str(tempKurang[i]) + "\n"
        else:
            INFO += "Value of KURANG(" + str(i) + ")"  + ": " + str(tempKurang[0]) + "\n"
    INFO += "Sum of KURANG(i): " + str(valueKurang) + "\n"
    INFO += "Nodes Generated: " + str(total) + "\n"
    INFO += "Time Execution: " + str(duration * 1000) + " ms\n" 
    showinfo(title = 'Details Solution', message = INFO)

'''
/* *** SAVE FILE BUTTON *** */
** Button untuk memanggil fungsi saveFile
'''
def saveFileButton():
    menu = tkinter.Menu(root)
    root.config(menu = menu)
    fileMenu = tkinter.Menu(menu, tearoff = 0)
    menu.add_cascade(label = 'Export Solution', menu = fileMenu)
    fileMenu.add_command(label = 'Save Puzzle', command = saveFile)

'''
/* *** SETTING *** */
** Fungsi untuk melakukan pengaturan terhadap setting dari GUI
'''
def setting():
    # Title and size
    root.title("15-Puzzle Solver by nelsenputra")
    root.geometry("300x300")

    # Label
    prompt_label.place(x = 81, y = 7)

    # Open button
    open_button.place(x = 110, y = 29)

    # Filename
    filename_label.place(x = 75, y = 57)

    # Solve button
    solve_button.place(x = 110, y = 78)

    # Kurang_label
    kurang_label.place(x = 20, y = 105)

if __name__ == "__main__":
    # Inisialisasi GUI
    root = Tk()
    root.geometry("1000x1000")
    root['background'] = 'blue'

    puzzleLabels = [[0 for i in range(4)] for j in range(4)]
    puzzleLable()
    prompt_label = Label(root, text = 'Please input your puzzle:', font = ('Arial', 9), bg = 'blue')
    open_button = ttk.Button(root, text = 'Select File', command = selectFile)
    filename_label = Label(root, text = 'File has not been selected', font = ('Arial', 9), bg = 'blue')
    solve_button = ttk.Button(root, text = 'Solve', command = solveCaller)
    kurang_label = Label(root, text = '', font = ('Arial', 8), bg = 'blue')
    visualize_button = ttk.Button(root, text = 'Visualize', command = visualize) 
    reset_button = ttk.Button(root, text = 'Reset', command = resetPuzzle)
    details_button = ttk.Button(root, text = 'Show Details', command = showDetails)

    setting()

    saveFileButton()

    root.mainloop()