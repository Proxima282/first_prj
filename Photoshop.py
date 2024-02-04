from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QMainWindow, QAction
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
from os import *
from PaintWindow import*
import styles 

app = QApplication([])
main_win = QMainWindow()
screen = QWidget()
main_win.setWindowTitle("Графічний редактор")
main_win.resize(700, 500)

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

workdir = ''
def chooseWorkdir():
    global workdir 
    workdir = QFileDialog.getExistingDirectory()

def filter(filenames, extensions):
    result = []
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    chooseWorkdir()
    extensions = ['.jpg', '.png', '.gif', '.bmp']
    result = filter(listdir(workdir), extensions)
    file_list.clear()
    file_list.addItems(result)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    
    def loadImage(self, filename):
        self.filename = filename
        file_path = path.join(workdir, filename)
        self.image = Image.open(file_path)

    def showImage(self, path):
        lb_picture.hide()
        pixmapimage = QPixmap(path) 
        w, h = lb_picture.width(), lb_picture.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.AspectRatioMode.KeepAspectRatio)
        lb_picture.setPixmap(pixmapimage)
        lb_picture.show()
    
    def saveImage(self):
        save_path = path.join(workdir, self.save_dir)
        if not (path.exists(save_path) or path.isdir(save_path)):
            mkdir(save_path)
        file_path = path.join(save_path, self.filename)
        self.image.save(file_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def sharpnen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

workimage = ImageProcessor()

def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage(path.join(workdir, filename))

menubar = main_win.menuBar()
file_menu = menubar.addMenu("File")
new_action = QAction("Open", main_win)
new_action.setShortcut("Ctrl+O")
open_action = QAction("Open", main_win)
open_action.setShortcut("Ctrl+O")
save_action = QAction(QIcon("ImageEditor\save.png"), "Save", main_win)
save_action.setShortcut("Ctrl+S")
quit_action = QAction("Quit", main_win)
quit_action.setShortcut("Ctrl+Q")
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

file_list.itemClicked.connect(showChosenImage)
btn_open_folder.clicked.connect(showFilenamesList)
btn_black_white.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.rotate_left)
btn_left.clicked.connect(workimage.rotate_right)
btn_mirror.clicked.connect(workimage.mirror)
btn_sharpness.clicked.connect(workimage.sharpnen)
main_win.setStyleSheet(styles.style)
save_action.triggered.connect(save_file)
open_action.triggered.connect(open_file)
quit_action.triggered.connect(main_win.close)
main_win.show()
app.exec_()
