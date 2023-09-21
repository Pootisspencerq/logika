from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json
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
lst_tags =QLabel('список')

btn_n_add = QPushButton('додати')
btn_nunpin = QPushButton('відкрипити')
btn_nsearch_teg = QPushButton('знайти')
layoute_notes =QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
layoute_notes.addLayout(col1)
layoute_notes.addLayout(col2)

col1.addWidget(field_text)
col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_ncreate)
row1.addWidget(btn_ndelete)


row2 = QHBoxLayout()
row2.addWidget(btn_n_add)
row2.addWidget(btn_nunpin)
row2.addWidget(btn_nsearch_teg)
with open("ass.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
lst_notes.addItems(notes)
window.setLayout(layoute_notes)
window.show()
app.exec()