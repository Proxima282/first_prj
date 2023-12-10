from main import*
import json
from PyQt5.QtWidgets import QMessageBox 


notes = dict()
try:
    with open("data.json","r",encoding="utf - 8") as file:
        notes = json.load(file)
    listNotes.addItems(notes)
except:
    print("Такого файлу не існує ")

def show_note():
    textEdit.clear()
    listTags.clear()
    key = listNotes.selectedItems()[0].text() #Отримати назву замітки,яку треба відобразити 
    textEdit.setText(notes[key]["текст"])#За ключами отримати текст замітки і вставити у її віджет
    listTags.addItems(notes[key["теги"]])


def add_note():
    note_name, ok = QInputDialog.getText(mw,"Додати замітку","Назва замітки")#Діалогове вікно створення нової замітки 
    if ok and note_name != "": #чи ми ввели назву замітки і натиснули ок
        notes[note_name] = {"текст":"","теги":[]}#Створюється струткура заітки з назвою
        listNotes.addItem(note_name)#назва замітки поміщається у віджет списку заміток
        listTags.addItems(notes[note_name]["теги"])#теги замітки поміщається у список тегів
        print(notes)

def save_note():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()#отриууємо назви замітки яку ми отримаємо
        notes[key]["текст"] = textEdit.toPlainText()#отримуємо текст замітки
        with open("data.json","w",encoding="utf-8")as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
    else:
        print("Ви не вибрали замітку")
        message.setText("Ви не вибрали замітку")
        message.exec_()

def del_note():
    if listNotes.selectedItems:
        key = listNotes.selectedItems()[0].text()#отримуємо назву замітки 
        del notes[key]#Видаляємо елементи словника за ключем
        listNotes.clear
        listTags.clear()
        textEdit.clear()
        #Оновлюємо віджет
        listNotes.addItems(notes)
        with open("data.json","w",encoding="utf-8") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
    else:
        print("Ви не вибрали замітку!")
def add_tag():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()#Отримаємо назву замітки яку ми обираємо
        tag = linEdit.text()#Новий тег
        if not tag in notes[key]["теги"]:#перевірка наявності тегу в списку тегів
            notes[key]["теги"].append(tag)#Додаємо в кінець списку новий тег
            listTags.addItems(tag)#Додаємо у віджет новий віджет
            linEdit.clear
            with open("data.json","w",encoding="utf-8") as file:
                json.dump(notes,file,sort_keys=True,ensure_ascii=False)
    else:
        print("Ви не вибрали замітку для додавання тега")
def del_tag():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()#Отримуємо назву замітки
        tag = listTags.selectedItems()[0].text()#Отримаємо назву тегу
        notes[key]["теги"].remove(tag)#Видаляємо тег з словника
        listTags.clear()
        listTags.addItems(notes[key]["теги"])#Додавання заміток у віджет з оновленими тегами
        with open("data.json","w",encoding="utf-8") as file:
                json.dump(notes,file,sort_keys=True,ensure_ascii=False)#Оновлюємо файл 
    else:
        print("Ви не вибрали конкретну замітку для видалення тегу!")
        message.setText("Ви не ввели тег для пошуку")
        message.setWindowTitle("Назва тегу")

def search_tag():
    tag = linEdit.text()#Отримаємо назву тегу 
    if btn_searchNote.text() == "Шукати замітку по тегу" and tag:#Перевріка введення тегу 
        note_filtered = dict()#словник фільтрється 
        for note in notes: #Перебираємо всі замітки у словнику
            if tag in notes[note]["теги"]: #Якщо знайшли потрібний тег,то записуємо цю замітку у новий словник 
                note_filtered[note] = notes[note]
        btn_searchNote.setText("Скинути пошук")
        listNotes.clear()
        listTags.clear()
        listNotes.addItems(note_filtered) #Додаємо до віджета список відфільтрованих заміток
    elif btn_searchNote.text() == "Скинути пошук":
        listNotes.clear()
        listTags.clear()
        listNotes.addItems(notes) #Додаємл всі замітки до віджета
        btn_searchNote.setText("Шукати замітку по тегу")
    elif tag == "":
        message.setWindowTitle("Назва тегу")
        message.setText("Ви не ввели тег для пошуку")
        message.exec_()

def save_in_txt():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                text = textEdit.toPlainText()
                with open(str[index]+".txt","w") as file:
                    file.write(note[0]+"\n")
                    file.write(text[1]+"\n")
                    for tag in notes[key]["теги"]:
                        file.write(tag+" ")
                    file.write("\n")
            index += 1 
    else:
        message.setWindowTitle("Назва замітки ")
        message.setText("Ви не отримали замітку для збереження")
        message.exec_()


btn_searchNote.clicked.connect(search_tag)
btn_addToNote.clicked.connect(add_tag)
btn_unpickFromNote.clicked.connect(del_tag)
btn_createNote.clicked.connect(add_note)
btn_saveNote.clicked.connect(save_note)
btn_deleteNote.clicked.connect(del_note)
listNotes.itemClicked.connect(show_note)
btn_saveTotxt.clicked.connect(save_in_txt)

mw.show()
app.exec()
