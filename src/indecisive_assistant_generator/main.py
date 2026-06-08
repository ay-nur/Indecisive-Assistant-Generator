"""
basic_app.py
by Ayca Erdogan
A basic calculator GUI app that takes the initial price of the game and the sale to calculate the new price of the game. 
"""

import sys
from options import OptionsWindow
from questions import QuestionsWindow
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
    QStackedLayout

)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indecisive Assistant Generator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 300)

        self.main_layout = QStackedLayout()
        layout = QVBoxLayout()
        title_label = QLabel("Indecisive Assistant Generator")
        title_label.setContentsMargins(0,0,0,12)

        # add buttons
        button_layout = QVBoxLayout()
        food_button = QPushButton("Food")
        food_button.clicked.connect(self.get_options)
        movie_button = QPushButton("Movies")
        movie_button.clicked.connect(self.get_options)
        activity_button = QPushButton("Activities")
        activity_button.clicked.connect(self.get_options)
        question_button = QPushButton("Ask")
        question_button.clicked.connect(self.ask_question)

        button_layout.setContentsMargins(20,20,20,20)

        button_layout.addWidget(food_button)
        button_layout.addWidget(movie_button)
        button_layout.addWidget(activity_button)
        button_layout.addWidget(question_button)

        # TODO: add instructions
        self.instructions = "Pick a topic that is closest to the genre of your indecisive factor."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)

        # add stacked layouts
        self.options = OptionsWindow()
        self.main_layout.addWidget(self.options)
        self.questions = QuestionsWindow()
        self.main_layout.addWidget(self.questions)
        self.main_layout.setCurrentWidget(self.options)

        # TODO: add stylesheets
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.output_label.setStyleSheet("font-size: 14px;")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.output_label)
        layout.addLayout(button_layout)
        layout.addLayout(self.main_layout)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def ask_question(self):
        self.main_layout.setCurrentWidget(self.questions)

    def get_options(self):
        clicked_button = self.sender().text()

        match clicked_button:
            case "Activities":
                self.options.options_label.setText("Activities")
                self.options.output_label.setText("Enter your top 3 choices for activities.")
            case "Movies":
                self.options.options_label.setText("Movies")
                self.options.output_label.setText("Enter your top 3 choices for movies or TV shows.")
            case "Food":
                self.options.options_label.setText("Food")
                self.options.output_label.setText("Enter your top 3 places to eat out at or your top 3 choices to cook.")


        self.main_layout.setCurrentWidget(self.options)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()