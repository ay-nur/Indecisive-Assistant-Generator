"""
basic_app.py
by Ayca Erdogan
A basic calculator GUI app that takes the initial price of the game and the sale to calculate the new price of the game. 
"""

import sys
from options import OptionsWindow
from questions import QuestionsWindow
from PySide6.QtCore import Qt
#from Pyside6.QtGui import QFont
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

stylesheet = """
QMainWindow {
    background-color: #EFE8C4;
    }
QLineEdit {
    background-color: #F0DFAD;
    color: #6C3B18;
    }
QPushButton {
    background-color: #D8BF90;
    color: #6C3B18;
    }
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indecisive Assistant Generator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(440, 600)

        self.main_layout = QStackedLayout()
        layout = QVBoxLayout()
        self.title_label = QLabel("Indecisive Assistant Generator")
        self.title_label.setContentsMargins(0,0,0,12)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add buttons
        self.button_layout = QHBoxLayout()
        self.food_button = QPushButton("Food")
        self.food_button.clicked.connect(self.get_options)
        self.movie_button = QPushButton("Movies")
        self.movie_button.clicked.connect(self.get_options)
        self.activity_button = QPushButton("Activities")
        self.activity_button.clicked.connect(self.get_options)
        self.question_button = QPushButton("Ask")
        self.question_button.clicked.connect(self.ask_question)

        self.button_layout.setContentsMargins(20,20,20,20)
        self.button_layout.setProperty("cssClass", "buttons")

        self.button_layout.addWidget(self.food_button)
        self.button_layout.addWidget(self.movie_button)
        self.button_layout.addWidget(self.activity_button)
        self.button_layout.addWidget(self.question_button)

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
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #AA4465")
        self.output_label.setStyleSheet("font-size: 14px; color: #6C3B18")

        # add widgets & layouts to main layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.output_label)
        layout.addLayout(self.button_layout)
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

    app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()

    app.exec()