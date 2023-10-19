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

workdir = QFileDialog.getExistingDirectory()
print(workdir)

files =os.listdir(workdir)
print(files)

def filter(filename):
    result = []
    ext = ['jpg', 'png', 'gif', 'bmp', ' jpeg']
    for file in filename:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result        
        
print(filter(files))


window.setLayout(layot_editor)
window.show()
app.exec_()

