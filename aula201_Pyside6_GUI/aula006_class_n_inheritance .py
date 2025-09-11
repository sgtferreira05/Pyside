# The basic of Signal and Slot (events and documentation)

import sys

from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("My first window")

        self.button1 = self.button_maker("Hello World 1")
        self.button1.clicked.connect(self.second_checked_action)


        self.button2 = self.button_maker("Hello World 2")

        self.button3 = self.button_maker("Hello World 3")

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button1, 1, 1)
        self.grid_layout.addWidget(self.button2, 2, 1)
        self.grid_layout.addWidget(self.button3, 3, 1)

        #StatusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("It's Ok!")

        #menuBar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.first_action = self.file_menu.addAction("New")
        self.first_action.triggered.connect(self.change_statusBar_message)



        self.new_action2 = self.file_menu.addAction("New Action 2")
        self.new_action2.setCheckable(True)
        self.new_action2.toggled.connect(self.second_checked_action)
        self.new_action2.hovered.connect(self.second_checked_action)

    @Slot()
    def change_statusBar_message(self):
        self.status_bar.showMessage("My slot was called!")


    @Slot()
    def second_checked_action(self):
        print('Checked:', self.new_action2.isChecked())

    def button_maker(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("font-size: 40px;")
        return btn


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()
    app.exec() #Appilication loop


