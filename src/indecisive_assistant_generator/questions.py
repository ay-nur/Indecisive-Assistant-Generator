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

class QuestionsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indecisive Assistant Generator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 350)

        layout = QVBoxLayout()
        title_label = QLabel("Yes or No")
        title_label.setContentsMargins(0,0,0,12)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Get user input
        self.question_input = QLineEdit(placeholderText="Question")

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
        self.instructions = "Ask a Yes or No question then click the generator to get your answer."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)
        self.answer_label = QLabel()

        self.output_label.setContentsMargins(10,10,10,10)
        self.answer_label.setContentsMargins(10,10,10,10)
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # TODO: add stylesheets
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.output_label.setStyleSheet("font-size: 14px;")
        self.answer_label.setStyleSheet("font-size: 20px;")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.question_input)
        layout.addLayout(button_layout)
        layout.addWidget(self.answer_label)
        

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        self.setLayout(layout)

    
    def get_input(self):
        """Get the text from the food inputs and generate a random output"""
        output = ""

        # Random Generator
        num = random.randint(1,2)

        # Outputs
        if num == 1:
            output = f'Yes.'
        elif num == 2:
            output = f'No.'

        self.answer_label.setText(output)

    def clear_inputs(self):
        """Clear the text in the inputs and reset the output label"""
        self.answer_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuestionsWindow()
    window.show()

    app.exec()

