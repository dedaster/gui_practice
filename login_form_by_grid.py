# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 03:51:17 2022

@author: dedaster
"""

from tkinter import * # импортируем библиотеку

parent = Tk()
parent.title("Login form")
name = Label(parent, text = "Name").grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
password = Label(parent, text = "Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)
parent.mainloop()