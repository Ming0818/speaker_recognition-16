# -*- coding: utf-8 -*-

import tkinter as tk
import main
#import recording_wave as recw
   
"""
def record(text):
    recw.rec()
    print(text)
"""


def main_window():
    flag = True
    root = tk.Tk()
    root.wm_geometry("300x180+350+200")
    
    while(flag):
        label_add = tk.Label(root, text = "Добавить в базу", bg='lightblue')
        label_add.place(x=0, y=0, width=300, height=80,)
        but_add_open = tk.Button(root, text = "Открыть",)
        but_add_open.place(x=90, y=50, width=120, height=25)
#        but_add_rec = tk.Button(root, text = "Записать")
#        but_add_rec.place(x=165, y=50, width=120, height=25)
        
        label_search = tk.Label(root, text = "Найти в базе", bg='lightblue')
        label_search.place(x=0, y=85, width=300, height=100)
        but_search_open = tk.Button(root, text = "Открыть",)
        but_search_open.place(x=90, y=150, width=120, height=25)
#        but_search_rec = tk.Button(root, text = "Записать")
#        but_search_rec.place(x=165, y=150, width=120, height=25)
                
        
        but_add_open.bind("<Button-1>", lambda event: main.open_file(event, "add"))
#        but_add_rec.bind("<Button-1>",  lambda event:record("add"))
        but_search_open.bind("<Button-1>", lambda event: main.open_file(event, "search"))
#        but_search_rec.bind("<Button-1>", lambda event:record("rec"))
        
        
        
        if root.quit() == None:
            flag = False            
        root.mainloop()
