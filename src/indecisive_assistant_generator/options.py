"""
basic_app.py
by Ayca Erdogan
A basic calculator GUI app that takes the initial price of the game and the sale to calculate the new price of the game. 
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indecisive Assistant Generator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 350)

        layout = QVBoxLayout()
        title_label = QLabel("Food")
        title_label.setContentsMargins(0,0,0,12)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Get user input
        input_layout = QVBoxLayout()
        self.f1_input = QLineEdit(placeholderText="Option 1")
        self.f2_input = QLineEdit(placeholderText="Option 2")
        self.f3_input = QLineEdit(placeholderText="Option 3")

        input_layout.setContentsMargins(20,20,20,0)

        input_layout.addWidget(self.f1_input)
        input_layout.addWidget(self.f2_input)
        input_layout.addWidget(self.f3_input)

        # add buttons
        button_layout = QHBoxLayout()
        generate_button = QPushButton("Generate")
        clear_button = QPushButton("Clear")

        generate_button.clicked.connect(self.get_input)
        clear_button.clicked.connect(self.clear_inputs)

        button_layout.setContentsMargins(20,20,20,20)

        button_layout.addWidget(generate_button)
        button_layout.addWidget(clear_button)

        # TODO: add instructions
        self.instructions = "Enter your top 3 places to eat out at or your top 3 choices to cook."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)
        self.answer_label = QLabel()

        self.answer_label.setContentsMargins(10,10,10,10)
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # TODO: add stylesheets
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.output_label.setStyleSheet("font-size: 14px;")
        self.answer_label.setStyleSheet("font-size: 14px;")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.answer_label)
        

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    def get_input(self):
        """Get the text from the food inputs and generate a random output"""
        output = ""
        f1 = self.f1_input.text()
        f2 = self.f2_input.text()
        f3 = self.f3_input.text()

        # Random Generator
        num = random.randint(1,3)

        # Outputs
        if num == 1:
            output = f'You should eat {f1}.'
        elif num == 2:
            output = f'You should eat {f2}.'
        else:
            output = f'You should eat {f3}.'

        self.answer_label.setText(output)

    def clear_inputs(self):
        """Clear the text in the inputs and reset the output label"""
        self.f1_input.clear()
        self.f2_input.clear()
        self.f3_input.clear()
        self.answer_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

