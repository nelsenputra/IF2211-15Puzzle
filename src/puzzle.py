# puzzle.py
# Source code program utama 15-Puzzle

# IMPORT LIBRARY
import heapq as pq
import copy

# KELAS PUZZLE
class Puzzle:
    # Inisialisasi
    puzzle = [] # Puzzle sebagai array kosong
    solution = [] # Solusi dari puzzle
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)] # Arah perpindahan: kanan, atas, kiri, bawah
    tempKurang = [0 for i in range(16)] # Nilai fungsi kurang untuk tiap iterasi
    visited = [] # List nodes yang sudah pernah dikunjungi
    valueX = 0 # Nilai dari X awal
    total = 0 # Banyaknya simpul yang dibangkitkan
    minimumCost = (10 ** 9) + 7 # Minimum cost

    '''
    /* *** __INIT__ *** */
    ** Konstruktor untuk inisialisasi atribut dari kelas Puzzle
    ** param: self
    ** param: fileName (nama file .txt yang menjadi input)
    '''
    def __init__(self, fileName):
        self.puzzle = [] 
        self.solution = [] 
        self.tempKurang = [0 for i in range(16)] 
        self.visited = []
        self.valueX = 0 
        self.total = 0
        self.minimumCost = 1e9 + 7 
        self.getPuzzle(fileName)

    '''
    /* *** GET PUZZLE *** */
    ** Getter puzzle dari masukan file input .txt
    ** param: self
    ** param: fileName (nama file .txt yang menjadi input)
    '''
    def getPuzzle(self, fileName):
        tempPuzzle = []
        puzzleSet = set({})
        with open(fileName) as f:
            lines = f.readlines()
            if (len(lines) == 4):
                for line in lines:
                    if (len(line.split()) == 4):
                        tempPuzzle.append([int(i) for i in line.split()])
                        for i in line.split():
                            puzzleSet.add(int(i))
                    else:
                        return
            else:
                return
        if (puzzleSet != {i for i in range(16)}):
            return
        self.puzzle = tempPuzzle

    '''
    /* *** SUM OF KURANG *** */
    ** Fungsi yang mengembalikan hasil penjumlahan dari KURANG(i) + valueX pada puzzle
    ** param: self
    ** return: kurang (hasil penjumlahan dari KURANG(i) + valueX pada puzzle)
    '''
    def sumOfKurang(self):
        cost = 0
        flat = [i for j in self.puzzle for i in j]
        for i in range(len(flat)):
            temp = 0
            if ((flat[i] == 0) and ((((i // 4) % 2 == 1) and (i % 2 == 0)) or (((i // 4) % 2 == 0) and (i % 2 == 1)))):
                self.valueX = 1
            for j in range(i + 1, len(flat)):
                if (((flat[i] > flat[j]) or (flat[i] == 0)) and (flat[j] != 0)):
                    temp += 1
                    cost += 1
            self.tempKurang[flat[i]] = temp
        kurang = cost + self.valueX
        return kurang
    
    '''
    /* *** SUM OF COST *** */
    ** Fungsi yang mengembalikan total cost yang diperlukan oleh puzzle
    ** param: self
    ** param: puzzle (puzzle yang ingin dihitung cost-nya)
    ** return: cost (total cost untuk puzzle)
    '''
    def sumOfCost(self, puzzle):
        flat = [i for j in puzzle for i in j]
        cost = 0
        for i in range(len(flat)):
            if ((i + 1) % 16 != flat[i]):
                cost += 1
        return cost

    '''
    /* *** GET ZERO POSITION *** */
    ** Fungsi yang mengembalikan koordinat dari sel kosong (nilai elemen = 0) pada puzzle
    ** param: self
    ** param: puzzle (puzzle yang ingin dicari koordinat sel kosongnya)
    ** return: koordinat sel kosong pada puzzle
    '''
    def getZeroPos(self, puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if (puzzle[i][j] == 0):
                    return (i, j)
        return (-1, -1)
    
    '''
    /* *** SOLVE *** */
    ** Fungsi yang mengembalikan sum of fungsi kurang, memecahkan puzzle dengan algoritma Branch and Bound
    ** param: self
    ** return: kurang (sum of kurang function, solution)
    '''
    def solve(self): 
        kurang = self.sumOfKurang()
        if ((kurang % 2) == 0):
            heap = []
            cost = self.sumOfCost(self.puzzle)
            pq.heappush(heap, (cost, 0, copy.deepcopy(self.puzzle), []))
            while (len(heap) > 0):
                currentCost, depth, currentPuzzle, path = pq.heappop(heap)
                self.visited.append(currentPuzzle)
                self.total += 1
                if ((currentCost <= self.minimumCost) and (currentCost != depth)):
                    # Transisi
                    x0, y0 = self.getZeroPos(currentPuzzle)
                    for dx, dy in self.direction:
                        if ((0 <= x0+dx <4) and (0 <= y0+dy <4)): # Kasus koordinat tidak valid
                            newPuzzle = copy.deepcopy(currentPuzzle)
                            newPuzzle[x0][y0], newPuzzle[x0+dx][y0+dy] = newPuzzle[x0+dx][y0+dy], newPuzzle[x0][y0]
                            newPath = copy.deepcopy(path)
                            newPath.append((dx, dy))
                            cost = self.sumOfCost(newPuzzle)
                            if (not newPuzzle in self.visited):
                                pq.heappush(heap, (cost + depth + 1, depth + 1, newPuzzle, newPath))
                else:
                    if (currentCost > self.minimumCost): # Bound
                        continue
                    if (currentCost == depth): # Solusi ditemukan
                        if (currentCost < self.minimumCost):
                            self.minimumCost = currentCost
                            self.solution = path
                        continue
        return kurang