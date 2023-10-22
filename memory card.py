from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,  QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox,QButtonGroup

app = QApplication([])

mw = QWidget()
mw.resize(500,400)
mw.setWindowTitle('Memory card')

question = QLabel('В якому році канал отримав золоту кнопку на ютубі?')
rb1 = QRadioButton('2005')
rb2 = QRadioButton('2010')
rb3 = QRadioButton('2015')
rb4 = QRadioButton('2020')

main_Layout = QVBoxLayout()
H1_layout = QHBoxLayout()
H2_layout = QHBoxLayout()

H2_layout.addWidget(rb1,alignment=Qt.AlignCenter)
H2_layout.addWidget(rb2,alignment=Qt.AlignCenter)
H1_layout.addWidget(rb3,alignment=Qt.AlignCenter)
H1_layout.addWidget(rb4,alignment=Qt.AlignCenter)

main_Layout.addWidget(question,alignment=Qt.AlignCenter)
main_Layout.addLayout(H2_layout)
main_Layout.addLayout(H1_layout)

def victory_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно!')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Ні,в 2015 році')
    victory_win.exec_()


rb1.clicked.connect(show_lose)
rb2.clicked.connect(show_lose)
rb3.clicked.connect(victory_win)
rb4.clicked.connect(show_lose)


mw.setLayout(main_Layout)


mw.show()
app.exec_()

