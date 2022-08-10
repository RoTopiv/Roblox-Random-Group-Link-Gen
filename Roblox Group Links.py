from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from ntpath import join
from os import link
import string
from tkinter import S
import webbrowser
import random

number = str(random.randint(1000, 100000))

str1 = 'https://www.roblox.com/groups/' + number

webbrowser.open_new_tab(str1)
