import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QPushButton,
    QMessageBox
)
from PyQt5.QtGui import QIntValidator, QFont , QIcon
from PyQt5.QtCore import Qt


class SudokuCell(QLineEdit):
    def __init__(self, value=0, read_only=False):
        super().__init__()
        self.setFixedSize(40, 40)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Arial", 14))
        self.setValidator(QIntValidator(1, 9))
        self.setStyleSheet("background-color: #f2f2f2;")
        if value != 0:
            self.setText(str(value))
           
        if read_only:
            self.setReadOnly(True)
            self.setStyleSheet("background-color: lightgray;")


class SudokuBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku with Pre-filled Puzzle")
        self.grid_layout = QGridLayout()
        self.cells = [[None for _ in range(9)] for _ in range(9)]

        self.puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        for i in range(9):
            for j in range(9):
                val = self.puzzle[i][j]
                read_only = val != 0
                cell = SudokuCell(val, read_only)
                self.cells[i][j] = cell
                self.grid_layout.addWidget(cell, i, j)

        self.check_button = QPushButton("Check")
        self.check_button.clicked.connect(self.check_board)
        self.grid_layout.addWidget(self.check_button, 9, 0, 1, 9)
        self.setLayout(self.grid_layout)
        self.setStyleSheet("background-color: #white;")
        self.setWindowIcon(QIcon("SudokuLogo.png"))

    def get_board(self):
        board = []
        for row in self.cells:
            board_row = []
            for cell in row:
                text = cell.text()
                board_row.append(int(text) if text else 0)
            board.append(board_row)
        return board

    def check_board(self):
        board = self.get_board()
        if self.is_valid_sudoku(board):
            QMessageBox.information(self, "Sudoku", "Valid Sudoku!")
        else:
            QMessageBox.warning(self, "Sudoku", "Invalid Sudoku!")

    def is_valid_sudoku(self, board):
        def is_valid_unit(unit):
            nums = [num for num in unit if num != 0]
            return len(nums) == len(set(nums))

        for i in range(9):
            if not is_valid_unit(board[i]) or not is_valid_unit([board[j][i] for j in range(9)]):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [board[r][c]
                       for r in range(box_row, box_row + 3)
                       for c in range(box_col, box_col + 3)]
                if not is_valid_unit(box):
                    return False

        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuBoard()
    window.show()
    sys.exit(app.exec_())
