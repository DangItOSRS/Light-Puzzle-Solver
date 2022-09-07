# LightPuzzleSolver.py

from LightPuzzle import LightPuzzle
import random
import copy

class LightPuzzleSolver:

    def __init__(self, userPuzzle=LightPuzzle()):
        self.userPuzzle = userPuzzle

    def solvePuzzle(self):
        bestSolution = []
        #userPuzzle = LightPuzzle(1,1,1,1,1,1,1,0)

        for i in range(0, 1000):
            lightPuzzle = copy.deepcopy(self.userPuzzle)
            solution = self.bruteForceSolve(lightPuzzle)
            if len(bestSolution) == 0 or len(solution) < len(bestSolution):
                bestSolution = solution

        formattedSolution = self.formatSolution(bestSolution)
        return(formattedSolution)

    def formatSolution(self, solution):
        solutionMatrix = [[0, 0, 0], [0, None, 0], [0, 0, 0]]
        for coordinate in solution:
            solutionMatrix[coordinate[0]][coordinate[1]] = 1
        return solutionMatrix
        
    def bruteForceSolve(self, lightPuzzle):
        solution = []
        while not lightPuzzle.isPuzzleSolved():
            while True:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if x == 1 and y == 1:
                    continue
                else:
                    break
            lightPuzzle.pressIndicies(x, y)
            solution.append([x, y])
        return solution

#lightPuzzleExample = LightPuzzle(1,0,1,0,0,1,0,0)
#exampleSolver = LightPuzzleSolver(lightPuzzleExample)
#exampleSolver.solvePuzzle()
