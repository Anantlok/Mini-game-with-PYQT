import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit,
    QPushButton, QLabel, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtGui import QIcon


class NumberedCell(QLineEdit):
    def __init__(self, number=0, letter="", parent=None):
        super().__init__(parent)
        self.number = number
        self.setMaxLength(1)
        self.setFont(QFont("Arial", 18, QFont.Bold))
        self.setAlignment(Qt.AlignCenter)
        self.correct_letter = letter.upper()
        self.set_square_size(60)  # make each cell square
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #555;
                border-radius: 8px;
                background: white;
            }
        """)

    def set_square_size(self, size):
        self.setFixedSize(size, size)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.number > 0:
            painter = QPainter(self)
            painter.setFont(QFont("Arial", 8))
            painter.drawText(4, 12, str(self.number))
            painter.end()


class CrosswordGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crossword Puzzle")
        self.setStyleSheet("background-color: #f4f4f4;")
        self.grid_size = 5

        # Puzzle solution
        self.crossword_pattern = [
            ["C", "A", "T", "S", ""],
            ["A", "P", "E", "S", ""],
            ["R", "O", "S", "E", ""],
            ["T", "E", "A", "R", ""],
            ["S", "E", "E", "D", ""]
        ]

        # Numbering
        self.numbering = [
            [1, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [3, 0, 4, 0, 0],
            [5, 0, 0, 0, 0],
            [6, 0, 0, 0, 0]
        ]

        # Hints
        self.hints_across = {
            1: "pets that meow",
            2: "rise of the planets of the __",
            3: "A flower",
            5: "Rip or pull apart",
            6: "Small hard part of a fruit"
        }
        self.hints_down = {
            1: "shopping ____",
            4: "Large body of water bigger than lake but smaller than ocean"
        }

        self.initUI()
        self.setWindowIcon(QIcon("crossword.png"))

    def initUI(self):
        main_layout = QHBoxLayout()

        # Crossword grid
        grid_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(3)
        self.cells = []

        for row in range(self.grid_size):
            cell_row = []
            for col in range(self.grid_size):
                letter = self.crossword_pattern[row][col]
                if letter != "":
                    cell = NumberedCell(self.numbering[row][col], letter)
                else:
                    cell = QLineEdit()
                    cell.setReadOnly(True)
                    cell.setFixedSize(60, 60)  # square empty cells
                    cell.setStyleSheet("background-color: #dcdcdc; border-radius: 8px;")
                grid_layout.addWidget(cell, row, col)
                cell_row.append(cell)
            self.cells.append(cell_row)

        grid_widget.setLayout(grid_layout)

        # Hints
        hints_widget = QWidget()
        hints_layout = QVBoxLayout()

        hints_layout.addWidget(QLabel("<b>Across:</b>"))
        for num, hint in self.hints_across.items():
            hints_layout.addWidget(QLabel(f"{num}. {hint}"))

        hints_layout.addSpacing(10)
        hints_layout.addWidget(QLabel("<b>Down:</b>"))
        for num, hint in self.hints_down.items():
            hints_layout.addWidget(QLabel(f"{num}. {hint}"))

        # Check button
        check_button = QPushButton("Check")
        check_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 8px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        check_button.clicked.connect(self.check_answers)
        hints_layout.addSpacing(15)
        hints_layout.addWidget(check_button)

        hints_widget.setLayout(hints_layout)

        main_layout.addWidget(grid_widget)
        main_layout.addSpacing(20)
        main_layout.addWidget(hints_widget)

        self.setLayout(main_layout)
        self.resize(600, 400)

    def check_answers(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = self.cells[row][col]
                if isinstance(cell, NumberedCell):
                    if cell.text().upper() == cell.correct_letter:
                        cell.setStyleSheet("""
                            QLineEdit {
                                border: 2px solid green;
                                border-radius: 8px;
                                background: #d4edda;
                            }
                        """)
                    else:
                        cell.setStyleSheet("""
                            QLineEdit {
                                border: 2px solid red;
                                border-radius: 8px;
                                background: #f8d7da;
                            }
                        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = CrosswordGame()
    game.show()
    sys.exit(app.exec_())

    sys.exit(app.exec_())
