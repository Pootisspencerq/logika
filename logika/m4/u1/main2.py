from PIL import Image, ImageFilter
class Imageeditor():
    def __init__(self, filename):
        self.filename = filename
        self.original= None
        self.changed =[]
    def open(self):    
        try:
            self.original = Image.open(self.filename)
            print(self.original.size)
            self.original.show()
        except:
            print("oops Sawry file was not found")
    def do_left(self): 
        left = self.original.transpose(Image.ROTATE_90) 
        self.changed.append(left)
        
        left.save('rotate_ '+ self.filename)
        
    def do_cropp(self):
        box =(100, 100, 225, 225)
        cropped =self.original.crop(box)
        cropped.show() 
        cropped.save('cropped_'+ self.filename)    

img =Imageeditor("napoleon.jpg")   
img.open()         

img.do_left()
