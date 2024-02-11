#Завантажуємо графічні віджети 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow, QAction
#Завантажуємо два класи для показу зображення і іконок меню
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
#Завантажуємо модулі для редагування,збереження і завантаження картинок
from PIL import Image, ImageFilter
#дозволяє працювати з шляхами та папками 
from os import *
#окреме вікно яке дозволяє малювати 
from PaintWindow import*
import Styles 

app = QApplication([])
main_win = QMainWindow()
screen = QWidget()
main_win.setWindowTitle("Графічний редактор")
main_win.resize(1000, 600)

lb_picture = QLabel("Picture")
file_list = QListWidget()
btn_open_folder = QPushButton("Folder")
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_mirror = QPushButton("Mirror")
btn_sharpness = QPushButton("Sharpness")
btn_black_white = QPushButton("B/W")

main_layout = QHBoxLayout()

button_layout = QHBoxLayout()

col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

button_layout.addWidget(btn_left)
button_layout.addWidget(btn_right)
button_layout.addWidget(btn_mirror)
button_layout.addWidget(btn_sharpness)
button_layout.addWidget(btn_black_white)

col_1.addWidget(btn_open_folder)
col_1.addWidget(file_list)

col_2.addWidget(lb_picture)
col_2.addLayout(button_layout)

main_layout.addLayout(col_1, 20)
main_layout.addLayout(col_2, 80)
screen.setLayout(main_layout)

main_win.setCentralWidget(screen)

#Створення полотна для малювання
def create_Canvas():
    global col_2
    canvas = PaintWindow()
    col_2.addWidget(canvas)

workdir = ''
#Вибір робочої папки
def chooseWorkdir():
    global workdir 
    workdir = QFileDialog.getExistingDirectory()
#Відфільтровує файли,залишаючи тільки графічні
def filter(filenames, extensions):
    result = []
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
#Завантаження відфільтрованих файлів у графічний віджет списку
def showFilenamesList():
    chooseWorkdir()
    extensions = ['.jpg', '.png', '.gif', '.bmp']
    result = filter(listdir(workdir), extensions)
    file_list.clear()
    file_list.addItems(result)

#клас длл редагування картинок
class ImageProcessor():
    def __init__(self):
        self.image = None #Об'єкт картинки
        self.dir = None#робоча директорія,або папка
        self.filename = None#Назва файлу з яким ми зараз працюємо 
        self.save_dir = "Modified/"#Папка для збереження модифікованих файлів
    #завантаження картинки 
    def loadImage(self, filename):
        self.filename = filename
        file_path = path.join(workdir, filename) #об'єднання шляху до картинки з ім'ям картинки 
        self.image = Image.open(file_path) #Відкрити картинку за шляхом,яким ми вказали
    #відображення картинки
    def showImage(self, path):
        lb_picture.hide()#сховати полотно
        pixmapimage = QPixmap(path) #відкртити картинку 
        w, h = lb_picture.width(), lb_picture.height()#підігнати розміри картинки під розміри полотна 
        pixmapimage = pixmapimage.scaled(w,h, Qt.AspectRatioMode.KeepAspectRatio)#відключити деформацію картинки 
        lb_picture.setPixmap(pixmapimage)#встановлюємо картинку в полотно 
        lb_picture.show()#показати полотно 
    #збереження модифікованої картинки 
    def saveImage(self):
        save_path = path.join(workdir, self.save_dir)
        if not (path.exists(save_path) or path.isdir(save_path)): #якщо папка для збереження не існує
            mkdir(save_path)#створюємо папку для збереження
        file_path = path.join(save_path, self.filename)#об'днуємо шлях до папки та назву файлу картинки
        self.image.save(file_path)#збереження картинки
    #чороно-білий фільтр 
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    #поворот наліво
    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    #поворот направо 
    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    #відзеркалення
    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    #різкість 
    def sharpnen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
#об'єкт класу для обробки зображення
workimage = ImageProcessor()

#обрати зі списку картинку для обробки 
def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage(path.join(workdir, filename))

#створення меню бара
menubar = main_win.menuBar()
file_menu = menubar.addMenu("File")#створення меню файла
new_action = QAction("New", main_win)#створення дії Новий,яка створює нове полотно 
new_action.setShortcut("Ctrl+O")#відкрити один файл 
open_action = QAction("Open", main_win)
open_action.setShortcut("Ctrl+O")
save_action = QAction(QIcon("ImageEditor\save.png"), "Save", main_win)#зберегти в конкретну папку
save_action.setShortcut("Ctrl+S")
quit_action = QAction("Quit", main_win)
quit_action.setShortcut("Ctrl+Q")
#додаємо дії до меню файлу
file_menu.addAction(new_action)
file_menu.addAction(open_action)
file_menu.addAction(save_action)
file_menu.addAction(quit_action)

def save_file():
    file_name, _ = QFileDialog.getSaveFileName(main_win, "Save File", "", "JPEG (*.jpg);;PNG (*.png);;GIF (*.gif)")

    if file_name:
        image = Image.open(workdir + '/' + workimage.save_dir + '/' + file_list.currentItem().text())
        image.save(file_name, "JPEG")

def open_file():
    file_name, _ = QFileDialog.getOpenFileName(main_win, "Open File", "", "JPEG (*.jpg);;PNG (*.png);;GIF (*.gif)")
    
    if file_name:
        workimage.showImage(file_name)
        workimage.image = Image.open(file_name)

#Підключення функцій до кнопок 
file_list.itemClicked.connect(showChosenImage)
btn_open_folder.clicked.connect(showFilenamesList)
btn_black_white.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.rotate_left)
btn_left.clicked.connect(workimage.rotate_right)
btn_mirror.clicked.connect(workimage.mirror)
btn_sharpness.clicked.connect(workimage.sharpnen)
main_win.setStyleSheet(Styles.style)
save_action.triggered.connect(save_file)
open_action.triggered.connect(open_file)
quit_action.triggered.connect(main_win.close)
main_win.show()
app.exec_()
