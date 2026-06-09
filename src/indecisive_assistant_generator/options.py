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

class OptionsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indecisive Assistant Generator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 350)

        layout = QVBoxLayout()
        self.options_label = QLabel("")
        self.options_label.setProperty("cssClass", "options_title")
        self.options_label.setContentsMargins(0,0,0,12)
        self.options_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Get user input
        self.input_layout = QVBoxLayout()

        self.f1_input = QLineEdit(placeholderText="Option 1")
        self.f2_input = QLineEdit(placeholderText="Option 2")
        self.f3_input = QLineEdit(placeholderText="Option 3")

        self.input_layout.setContentsMargins(20,20,20,0)
        self.input_layout.setProperty("cssClass", "options_input")

        self.input_layout.addWidget(self.f1_input)
        self.input_layout.addWidget(self.f2_input)
        self.input_layout.addWidget(self.f3_input)

        # add buttons
        button_layout = QHBoxLayout()
        generate_button = QPushButton("Generate")
        clear_button = QPushButton("Clear")
        #back_button = QPushButton("Back")

        generate_button.clicked.connect(self.get_input)
        clear_button.clicked.connect(self.clear_inputs)
        #back_button.clicked.connect(controller.)

        button_layout.setContentsMargins(20,20,20,20)

        button_layout.addWidget(generate_button)
        button_layout.addWidget(clear_button)

        # TODO: add instructions
        self.instructions = ""
        self.output_label = QLabel(self.instructions)
        self.output_label.setContentsMargins(10,10,10,10)
        self.output_label.setWordWrap(True)
        self.answer_label = QLabel()

        self.answer_label.setContentsMargins(10,10,10,10)
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # TODO: add stylesheets
        self.options_label.setStyleSheet("font-size: 30px; font-weight: bold; color: #AA4465")
        self.output_label.setStyleSheet("font-size: 14px; color: #6C3B18")
        self.answer_label.setStyleSheet("font-size: 14px; color: #AA4465")

        # add widgets & layouts to main layout
        layout.addWidget(self.options_label)
        layout.addWidget(self.output_label)
        layout.addLayout(self.input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.answer_label)
        

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        self.setLayout(layout)

    
    def get_input(self):
        """Get the text from the food inputs and generate a random output"""
        self.output = ""

        # Random Generator
        num = random.randint(0,2)
        input_list = [self.f1_input, self.f2_input, self.f3_input]
        self.output = input_list[num].text()
        
        self.answer_label.setText(f'{self.output}')

    def clear_inputs(self):
        """Clear the text in the inputs and reset the output label"""
        self.f1_input.clear()
        self.f2_input.clear()
        self.f3_input.clear()
        self.answer_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OptionsWindow()
    window.show()

    app.exec()

