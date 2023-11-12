from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QButtonGroup, QPushButton
from random import shuffle

i = 0

questions_list = [
    ["Какая столица Франции?",
     "Париж",
     "Милан",
     "Берлин",
     "Лондон"],
    
    ["Сколько планет в Солнечной системе?",
     "Восемь",
     "Семь",
     "Девять",
     "Шесть"],
    
    ["Кто написал роман 'Война и мир'?",
     "Лев Толстой",
     "Фёдор Достоевский",
     "Иван Тургенев",
     "Александр Пушкин"],
    
    ["Какой химический элемент обозначается символом 'H'?",
     "Водород",
     "Гелий",
     "Кислород",
     "Углерод"],

    ["Какое животное является символом бренда Ferrari?",
     "Лошадь",
     "Бык",
     "Скорпион",
     "Дельфин"],
    
    ["Сколько долей в целом составляют две половины?",
     "Одну",
     "Три",
     "Четыре",
     "Две"],
    
    ["Какой год был объявлен Годом Олимпиады в Токио?",
     "2020",
     "2016",
     "2022",
     "2018"],
    
    ["Какой самый крупный материк на Земле?",
     "Африка",
     "Европа",
     "Азия",
     "Австралия"],
     
    ["Какая планета известна как 'Красная планета'?",
     "Марс",
     "Венера",
     "Юпитер",
     "Уран"],
    
    ["Какое животное является символом года в китайском календаре в 2023 году?",
     "Кролик",
     "Дракон",
     "Тигр",
     "Змея"]
]

app = QApplication([])
mw = QWidget()
mw.resize(500, 400)
mw.setWindowTitle('Memorycard')

def start():
    start_layout.deleteLater()
    mw.setLayout(start_layout)
    new_question(i)

def new_question(i):
    global buttons
    global question
    shuffle(buttons)
    buttons[0].setText(questions_list[i][1])
    buttons[1].setText(questions_list[i][2])
    buttons[2].setText(questions_list[i][3])
    buttons[3].setText(questions_list[i][4])
    question.setText(questions_list[i][0])

def answer():
    global i
    if i <= len(questions_list):
        mess = QMessageBox()
        if rb_group.checkedButton() is buttons[0]:
            mess.setText("правильно")
        else:
            mess.setText("неправильно")
        

        mess.exec_()
        new_question()
        i += 1

   # elif i > 9:
      #  i = 0

def result(total_qustion, right_ans):
    mess = QMessageBox()
    mess.setText(f"Тест завершений\nРезультат, правильних відповідей:{round(right_ans/total_qustion*100, 2)}%")
    mess.exec_()



'''def win():
    ms_win = QMessageBox()
    ms_win.setText("правильно")
    ms_win.exec_()

def lose():
    ms_lose = QMessageBox()
    ms_lose.setText("неправильно")
    ms_lose.exec_()'''



start_lable = QLabel('Програма для тесту\nНажми кнопку, для початку')
start_button = QPushButton('Початок')
start_layout = QVBoxLayout()
start_layout.addWidget(start_lable, alignment=Qt.AlignCenter)
start_layout.addWidget(start_button, alignment=Qt.AlignCenter)


question = QLabel(questions_list[i][0])
rb_group = QButtonGroup()

rb1 = QRadioButton(questions_list[0][1])
rb2 = QRadioButton(questions_list[0][2])
rb3 = QRadioButton(questions_list[0][3])
rb4 = QRadioButton(questions_list[0][4])

rb_group.addButton(rb1)
rb_group.addButton(rb2)
rb_group.addButton(rb3)
rb_group.addButton(rb4)

main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()

h2_layout.addWidget(rb1, alignment=Qt.AlignCenter)
h2_layout.addWidget(rb2, alignment=Qt.AlignCenter)
h1_layout.addWidget(rb3, alignment=Qt.AlignCenter)
h1_layout.addWidget(rb4, alignment=Qt.AlignCenter)

main_layout.addWidget(question, alignment=Qt.AlignCenter)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h1_layout)

mw.setLayout(start_layout)

rb_group.buttonClicked.connect(answer)
start_button.clicked.connect(start)
 
buttons = rb_group.buttons()

mw.show()
app.exec_()
