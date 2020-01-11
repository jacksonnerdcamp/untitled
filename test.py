from graphics import *

# step 1: set up board
board = GraphWin('Board', 400, 400)
board.setBackground('white')

tilex = []
tiley = []
for y in range(9):
    for x in range(9):
        tilex.append(Rectangle(Point(x * 50, y * 50), Point(x * 50 + 50, y * 50 + 50)))
        tilex[x].draw(board)
        if (x + y) % 2 == 1:
            tilex[x].setFill('black')
    tiley.append(tilex)
    tilex.clear()

board.getMouse()


class Pawn:
    color = 'white'
    moves = [1, 0]
    pawn = GraphicsObject()
    def pawn(self, ):
    Rectangle(Point(0, 20), Point(10, 40)).draw(pawn)
    Oval(Point(0, 0), Point(10, 0)).draw(pawn)


board.draw(Pawn.pawn)
