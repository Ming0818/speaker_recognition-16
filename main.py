# -*- coding: utf-8 -*-

import tkinter.filedialog as fd
import interface
import add_in_db


def open_file(text, file):
    flag = True
    while(flag):
        try:
            #file = fd.askopenfilename()
            print(text)
        except:
            print("Невозможно открыть выбрать файл")
        else:
            flag = False
            #Если add, то высчитываем вектор признаков, класстеризуе и добавляем его в базу
            #Если search, то вычисляем вектор признаков и сравниваем их со всем, что есть в базе и находим минимум           
            add_in_db.generate_speech(file, text)
                
 
if __name__ == "__main__":
#    interface.main_window()
    """       
    for i in range(225, 241, 1):
        print(i)
        addr = "/home/user/Project_Python/Speaker_Recognition/VCTK-Corpus/wav48/p{0}/p{0}_001.wav".format(i)
        add_in_db.generate_speech(addr, "add") 
    """
    for i in range(225, 241, 1):
        for j in range(1, 10):
            
            f = open("text.txt", 'a')
            print(">>p{0}_00{1}.wav".format(i, j))
            f.write("\n>>p{0}_00{1}.wav".format(i, j))
            addr = "/home/user/Project_Python/Speaker_Recognition/VCTK-Corpus/wav48/p{0}/p{0}_00{1}.wav".format(i, j)
            add_in_db.generate_speech(addr, "search")
            f.close()
        if i == 241:
            break
    
# 225-288 (64 )
    