# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 04:00:06 2022

@author: dedaster
"""

import tkinter as tk # импортируем библиотеку

def click(): # функция действия после нажатия кнопки
    window.destroy() # закрытие окна
    
window = tk.Tk()
window.title("Провокационная кнопка")
button = tk.Button(text = "Только нажми и я закроюсь", width = 25, height = 5, bg = "red", fg = "black", command = click) # command отсылается к функции, которая выполнится по нажатию кнопки
button.pack()

window.mainloop()