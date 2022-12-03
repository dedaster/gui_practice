# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 03:21:41 2022

@author: dedaster
"""

from tkinter import * # импортируем библиотеку

parent = Tk() # создаем окно, которое будет родительским для элементов
parent.title("Мир кнопок") # задаем название окну
redbutton = Button(parent, text = "Red", fg = "red") # создаем кнопку и параментро parent привязываем ее к родительскому окну
redbutton.pack(side = LEFT) # устанавливаем расположение кнопки относительно центра окна
bluebutton = Button(parent, text = "Blue", fg = "blue") # параметр text задает текст, указанный на кнопке
bluebutton.pack(side = RIGHT)
greenbutton = Button(parent, text = "Green", fg = "green") # параметр fg задает цвет текста
greenbutton.pack(side = TOP)
purplebutton = Button(parent, text = "Purple", fg = "purple")
purplebutton.pack(side = BOTTOM)
parent.mainloop() # зацикливаем окно, чтобы не закрывалось само


