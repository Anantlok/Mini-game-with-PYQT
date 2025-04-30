import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QIcon

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(300, 350)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.grid_layout = QGridLayout()
        self.buttons = [[QPushButton() for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.setFixedSize(80, 80)
                btn.setStyleSheet("font-size: 24px")
                btn.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                self.grid_layout.addWidget(btn, i, j)

        # Reset button
        self.reset_button = QPushButton("Reset")
        self.reset_button.setFixedHeight(40)
        self.reset_button.clicked.connect(self.reset_game)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.grid_layout)
        main_layout.addWidget(self.reset_button)
		
        self.setLayout(main_layout)
        self.setWindowIcon(QIcon("TTTLogo.png"))

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            if self.check_winner():
                QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
                self.disable_board()
            elif self.is_draw():
                QMessageBox.information(self, "Game Over", "It's a draw!")
                self.disable_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        lines = (
            [b[i] for i in range(3)] +                            # Rows
            [[b[i][j] for i in range(3)] for j in range(3)] +     # Columns
            [[b[i][i] for i in range(3)], [b[i][2 - i] for i in range(3)]]  # Diagonals
        )
        return any(line == [self.current_player]*3 for line in lines)

    def is_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def disable_board(self):
        for row in self.buttons:
            for btn in row:
                btn.setEnabled(False)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.setText("")
                btn.setEnabled(True)
        self.current_player = "X"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
