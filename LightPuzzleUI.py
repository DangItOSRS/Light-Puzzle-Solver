import base64

import tkinter
from LightPuzzle import LightPuzzle
from LightPuzzleSolver import LightPuzzleSolver

lightPuzzle = LightPuzzle()

def togglex0y0():
    lightPuzzle.toggleIndex(0, 0)
    colorButtons()

def togglex1y0():
    lightPuzzle.toggleIndex(1, 0)
    colorButtons()

def togglex2y0():
    lightPuzzle.toggleIndex(2, 0)
    colorButtons()

def togglex0y1():
    lightPuzzle.toggleIndex(0, 1)
    colorButtons()

def togglex2y1():
    lightPuzzle.toggleIndex(2, 1)
    colorButtons()

def togglex0y2():
    lightPuzzle.toggleIndex(0, 2)
    colorButtons()

def togglex1y2():
    lightPuzzle.toggleIndex(1, 2)
    colorButtons()

def togglex2y2():
    lightPuzzle.toggleIndex(2, 2)
    colorButtons()

def reset():
    lightPuzzle.resetPuzzle()
    colorButtons()

def showSolution():
    puzzleSolver = LightPuzzleSolver(lightPuzzle)
    solution = puzzleSolver.solvePuzzle()
    showSolutionWindow(solution, window.geometry())

def colorButtons():
    x0y0button.configure(bg = "tan" if lightPuzzle.puzzle[0][0] == 0 else "yellow")
    x1y0button.configure(bg = "tan" if lightPuzzle.puzzle[1][0] == 0 else "yellow")
    x2y0button.configure(bg = "tan" if lightPuzzle.puzzle[2][0] == 0 else "yellow")
    x0y1button.configure(bg = "tan" if lightPuzzle.puzzle[0][1] == 0 else "yellow")
    x2y1button.configure(bg = "tan" if lightPuzzle.puzzle[2][1] == 0 else "yellow")
    x0y2button.configure(bg = "tan" if lightPuzzle.puzzle[0][2] == 0 else "yellow")
    x1y2button.configure(bg = "tan" if lightPuzzle.puzzle[1][2] == 0 else "yellow")
    x2y2button.configure(bg = "tan" if lightPuzzle.puzzle[2][2] == 0 else "yellow")

    

def showSolutionWindow(solution, mainWindowGeometry):
    solutionWindow = tkinter.Tk()
    solutionWindow.title("TOA Light Puzzle Solution")
    solutionWindow.geometry(mainWindowGeometry)
    solutionWindow.configure(bg='grey')

    x0y0button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[0][0] == 1 else "tan",
        fg="black"
    )
    x0y0button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

    x1y0button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[1][0] == 1 else "tan",
        fg="black"
    )
    x1y0button.grid(row=3, column=0, padx=(20, 20), pady=(20, 20))

    x2y0button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[2][0] == 1 else "tan",
        fg="black"
    )
    x2y0button.grid(row=5, column=0, padx=(20, 20), pady=(20, 20))

    x0y1button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[0][1] == 1 else "tan",
        fg="black"
    )
    x0y1button.grid(row=0, column=3, padx=(20, 20), pady=(20, 20))

    x2y1button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[2][1] == 1 else "tan",
        fg="black"
    )
    x2y1button.grid(row=5, column=3, padx=(20, 20), pady=(20, 20))

    x0y2button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[0][2] == 1 else "tan",
        fg="black"
    )
    x0y2button.grid(row=0, column=5, padx=(20, 20), pady=(20, 20))

    x1y2button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[1][2] == 1 else "tan",
        fg="black"
    )
    x1y2button.grid(row=3, column=5, padx=(20, 20), pady=(20, 20))

    x2y2button = tkinter.Button(
        solutionWindow,
        width=10,
        height=5,
        bg="lime" if solution[2][2] == 1 else "tan",
        fg="black"
    )
    x2y2button.grid(row=5, column=5, padx=(20, 20), pady=(20, 20))

    solutionWindow.mainloop()



window = tkinter.Tk()
window.title("TOA Light Puzzle Solver")
window.geometry("360x480")
window.configure(bg='grey')

x0y0button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex0y0
)
x0y0button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

x1y0button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex1y0
)
x1y0button.grid(row=3, column=0, padx=(20, 20), pady=(20, 20))

x2y0button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex2y0
)
x2y0button.grid(row=5, column=0, padx=(20, 20), pady=(20, 20))

x0y1button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex0y1
)
x0y1button.grid(row=0, column=3, padx=(20, 20), pady=(20, 20))

x2y1button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex2y1
)
x2y1button.grid(row=5, column=3, padx=(20, 20), pady=(20, 20))

x0y2button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex0y2
)
x0y2button.grid(row=0, column=5, padx=(20, 20), pady=(20, 20))

x1y2button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex1y2
)
x1y2button.grid(row=3, column=5, padx=(20, 20), pady=(20, 20))

x2y2button = tkinter.Button(
    window,
    width=10,
    height=5,
    bg="tan",
    fg="black",
    command=togglex2y2
)
x2y2button.grid(row=5, column=5, padx=(20, 20), pady=(20, 20))

resetButton = tkinter.Button(
    window,
    text="Reset",
    width=15,
    height=5,
    bg="cyan",
    fg="black",
    command=reset
)
resetButton.grid(row=8, column=0, columnspan=2)

solutionButton = tkinter.Button(
    window,
    text="Show Solution",
    width=15,
    height=5,
    bg="lime",
    fg="black",
    command=showSolution
)
solutionButton.grid(row=8, column=5, columnspan=2)

window.mainloop()
