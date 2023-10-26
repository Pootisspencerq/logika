from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os





app=QApplication([])
window=QWidget()

btn_left = QPushButton('left')
btn_right =QPushButton('right')
btn_flip = QPushButton('flip')
btn_bw = QPushButton('b and w')
btn_sharp = QPushButton('sharp')
btn_folder = QPushButton('folder')

lst_files = QListWidget()
lb_pic = QLabel("")
layot_editor=QHBoxLayout()

col1 =QVBoxLayout()
col2 =QVBoxLayout()

row =  QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
row.addWidget(btn_bw)

col2.addWidget(lb_pic)
col2.addLayout(row)

layot_editor.addLayout(col1, 1)
layot_editor.addLayout(col2, 4)



def filter(filename):
    result = []
    ext = ['jpg', 'png', 'gif', 'bmp', ' jpeg']
    for file in filename:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result        

def show_files():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files =os.listdir(workdir)
    graphic_files = filter(files)
    
    lst_files.clear()
    lst_files.addItems(graphic_files)
    
class ImageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = 'Modified/'
    def load_image(self, filename):
        self.filename = filename
        full_path = os.path.join(workdir, filename)
        self.original =Image.open(full_path)
     
    def show_Image(self, path):
        lb_pic.hide()
    
        pixmapimage =QPixmap(path)
        
        w, h = lb_pic.width(), lb_pic.height()
        pixmapimage =pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        
        lb_pic.setPixmap(pixmapimage) 
        lb_pic.show() 
        
    def saveandShow(self):
        path = os.path.join(workdir, self.save_dir)  
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
            
        image_path = os.path.join(path, self.filename)   
        self.original.save(image_path)
        self.show_Image(image_path)
         
def showChosenItem():
    filename = lst_files.currentItem().text()
    workimage.load_image(filename)
    full_path = os.path.join(workdir, filename)
    workimage.show_Image(full_path)   
workimage = ImageProcessor()  
    
lst_files.currentRowChanged.connect(showChosenItem)
btn_folder.clicked.connect(show_files) 
        

window.setStyleSheet('''
                        background-color: rgb(0,0,255); 
                        color: yellow;
                        font-size: 20px;
                        border: 2px solid black; 
                        ''')

window.setLayout(layot_editor)
window.show()
app.exec_()

