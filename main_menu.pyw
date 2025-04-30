import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

# Import the game windows
from tictactoe import TicTacToe
from sudoku import SudokuBoard

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Launcher")
        self.setFixedSize(300, 200)

        self.layout = QVBoxLayout()

        self.tic_btn = QPushButton("Play Tic Tac Toe")
        self.sudoku_btn = QPushButton("Play Sudoku")
        self.third_btn = QPushButton("Play third game")

        self.tic_btn.setFixedHeight(50)
        self.sudoku_btn.setFixedHeight(50)
        self.third_btn.setFixedHeight(50)

        self.tic_btn.clicked.connect(self.open_tic_tac_toe)
        self.sudoku_btn.clicked.connect(self.open_sudoku)
        self.third_btn.clicked.connect(self.open_sudoku)

        self.layout.addWidget(self.tic_btn)
        self.layout.addWidget(self.sudoku_btn)
        self.layout.addWidget(self.third_btn)

        self.setLayout(self.layout)

        self.tic_window = None
        self.sudoku_window = None
        self.third_window = None
        
        self.setWindowIcon(QIcon("logo.png"))

    def open_tic_tac_toe(self):
        self.tic_window = TicTacToe()
        self.tic_window.show()

    def open_sudoku(self):
        self.sudoku_window = SudokuBoard()
        self.sudoku_window.show()
        
    def open_third_game(self):
        self.sudoku_window = SudokuBoard()
        self.sudoku_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MainMenu()
    menu.show()
    sys.exit(app.exec_())
