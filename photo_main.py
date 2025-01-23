import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# from PyQt5 import uic
from main import Ui_MainWindow
from PyQt5.QtGui import QIcon

import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt  # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap  # оптимізована для показу на екрані картинка

from PIL import Image
from PIL.ImageQt import ImageQt  # Для перенесення графіки з Pillow до QT
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
    GaussianBlur, UnsharpMask
)
workdir = ''


def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()








class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, filename):
        ''' під час завантаження запам'ятовуємо шлях та ім'я файлу '''
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def saveImage(self):
        ''' зберігає копію файлу у підпапці '''
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)

        self.image.save(fullname)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.showImage(image_path)

    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        ex.showImage(image_path)


workimage = ImageProcessor()  # поточне робоче зображення для роботи

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configue()

    def configue(self):
        self.ui.listWidget_files.currentRowChanged.connect(self.showChosenImage)
        self.ui.btn_bw.clicked.connect(workimage.do_bw)
        self.ui.btn_left.clicked.connect(workimage.do_left)
        self.ui.btn_right.clicked.connect(workimage.do_right)
        self.ui.btn_sharp.clicked.connect(workimage.do_sharpen)
        self.ui.btn_flip.clicked.connect(workimage.do_flip)

    def showChosenImage(self):
        if self.ui.listWidget_files.currentRow() >= 0:
            filename = self.ui.listWidget_files.currentItem().text()
            workimage.loadImage(filename)
            ex.showImage(os.path.join(workdir, workimage.filename))

    def showImage(self, path):
        self.ui.label_text.hide()
        pixmapimage = QPixmap(path)
        w, h = self.ui.label_text.width(), self.ui.label_text.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.label_text.setPixmap(pixmapimage)
        self.ui.label_text.show()

app = QApplication(sys.argv)
ex = Widget()
ex.show()

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)

    ex.ui.listWidget_files.clear()
    for filename in filenames:
        ex.ui.listWidget_files.addItem(filename)


ex.ui.pushButton_folder.clicked.connect(showFilenamesList)


sys.exit(app.exec_())