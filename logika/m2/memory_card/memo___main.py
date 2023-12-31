from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будемо змішувати відповіді в картці питання
from memo____data import *

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

frm = Question('Яблуко', 'Apple', 'Caterpillar', 'house', 'cat')
frm_card = QuestionView(frm, lb_Question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])

def show_data():
    ''' показує на екрані потрібну інформацію '''
    pass

def check_result():
    ''' перевірка, чи вибрана правильна відповідь 
    якщо відповідь була вибрана, то напис "правильно/не правильно" отримує потрібне значення
    і показує панель відповідів'''
    pass

win_card = QWidget()
win_card.resize(card_width, card_height)
#тут повинні бути параметри вікна

frm_card.show()

win_card.setLayout(layout_card)
win_card.show()
app.exec_()