from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json
def writef ():
    with open('ass.json', 'w', encoding='utf8') as file: 
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)
app = QApplication([])

window = QWidget()
field_text = QTextEdit()
lb_notes =QLabel('список')
lst_notes = QListWidget()
btm_notes = QPushButton()

btn_ncreate = QPushButton('створити')
btn_ndelete = QPushButton('видалити')
btn_nsave = QPushButton('зберегти')
lb_tags =QLabel('список')
lst_tags =QListWidget()
field_tag = QLineEdit()
btn_n_add = QPushButton('додати')
btn_nunpin = QPushButton('відкрипити')
btn_nsearch_teg = QPushButton('знайти')
layoute_notes =QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
layoute_notes.addLayout(col1, stretch =2)
layoute_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)
col2.addWidget(lb_notes)
col2.addWidget(lst_notes)


row1 = QHBoxLayout()
row1.addWidget(btn_ncreate)
row1.addWidget(btn_ndelete)

col2.addLayout(row1)
col2.addWidget(btn_nsave)
col2.addWidget(lb_tags)
col2.addWidget(lst_tags)
col2.addWidget(field_tag)
row2 = QHBoxLayout()
row2.addWidget(btn_n_add)
row2.addWidget(btn_nunpin)
row2.addWidget(btn_nsearch_teg)
col2.addLayout(row2)

with open("ass.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

def show_notes():
    key = lst_notes.currentItem().text()
    print(notes[key])
    field_text.setText(notes[key]['text'])   
    lst_tags.clear()
    lst_tags.addItems(notes[key]['tags']) 
    
def add_note():
    note_name, ok = QInputDialog.getText(window, 'add tag' 'tag name')
    if note_name and ok :
        notes[note_name] ={'text':'', 'tags': []}
        lst_notes.addItem(note_name)
    
def save_note():
    if lst_notes.currentItem().text():
        key = lst_notes.currentItem().text()
        notes[key]['text']= field_text.toPlainText()
        writef()    
    
            
    
def deletenote():
    if lst_notes.currentItem().text():
        key = lst_notes.currentItem().text()
        del notes[key]
    field_text.clear()
    lst_tags.clear()
    lst_notes.clear()
    lst_notes.addItems(notes)
    writef()    
    
lst_notes.itemClicked.connect(show_notes)
btn_ncreate.clicked.connect(add_note)   
lst_notes    

window.setLayout(layoute_notes)
window.show()
app.exec()