# LightPuzzle.py

'''
[[x0y0,  x1y0,   x2y0],
 [x0y1, null, x2y1],
 [x0y2,  x1y2,   x2y2]]
'''

class LightPuzzle:

    def __init__(self, x0y0 = 0, x1y0 = 0, x2y0 = 0, x0y1 = 0, x2y1 = 0, x0y2 = 0, x1y2 = 0, x2y2 = 0):
        self.puzzle = [[x0y0,  x1y0,   x2y0], [x0y1, None, x2y1], [x0y2,  x1y2, x2y2]]

    def isPuzzleSolved(self):
        for i in range(0, len(self.puzzle)):
            for j in range(0, len(self.puzzle[i])):
                if self.puzzle[i][j] == 0:
                    return False
        return True
    
    def resetPuzzle(self):
        self.puzzle = [[0, 0, 0], [0, None, 0], [0, 0, 0]]

    def toggleIndex(self, x, y):
        self.puzzle[x][y] = 1 - self.puzzle[x][y]

    def pressIndicies(self, x, y):
        self.puzzle[x][y] = 1 - self.puzzle[x][y]
        if x < 2 and self.puzzle[x + 1][y] != None:
            self.puzzle[x + 1][y] = 1 - self.puzzle[x + 1][y]
        if y < 2 and self.puzzle[x][y + 1] != None:
            self.puzzle[x][y + 1] = 1 - self.puzzle[x][y + 1]
        if x > 0 and self.puzzle[x - 1][y] != None:
            self.puzzle[x - 1][y] = 1 - self.puzzle[x - 1][y]
        if y > 0 and self.puzzle[x][y - 1] != None:
            self.puzzle[x][y - 1] = 1 - self.puzzle[x][y - 1]

    def printPuzzle(self):
        for i in self.puzzle:
            print(i)
        return
        
