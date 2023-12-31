from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os
with Image.open("napoleon.jpg") as original:
    
    print( original.size)
    print (original.format)
    print (original.mode)
    
    
    bw_original = original.convert("L")
    bw_original.show()
    bw_original.save("grey.jpg")
    
    blur_original =original.filter(ImageFilter.BLUR)
    blur_original.show()
    blur_original.save("blur.jpg")
    
    pic_up = original.transpose(Image.ROTATE_180)
    pic_up.show()
    pic_up.save("rotate.jpg")
    
    
    original.show()
    
    QApplication
    
    
    
    
    
    
    
    
    
    
    
    
    