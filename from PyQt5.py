from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Randomizer')
mw.resize(300,200)

L1 = QLabel(text='Натисни кнопку,щоб обрати переможця')
winer = QLabel(text='???')
button = QPushButton(text='Переможець')

layout =  QVBoxLayout()

layout.addWidget(L1,alignment=Qt.AlignCenter)
layout.addWidget(winer,alignment=Qt.AlignCenter)
layout.addWidget(button,alignment=Qt.AlignCenter)

mw.setLayout(layout)
mw.show()


def random_winer():
    rand_num = randint(1, 100)
    winer.setText(str(rand_num))

button.clicked.connect(random_winer)
print(random_winer)

app.exec_()