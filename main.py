# -*- coding: utf-8 -*-

import add_in_db
import interface


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
#    """
    for i in range(238, 265, 1):
        print(i)        
        #addr_01 = "/home/user/Project_Python/Speaker_Recognition/VCTK-Corpus/wav48/p{0}/p{0}_012.wav".format(i)
        #addr_02 = "/home/user/Project_Python/Speaker_Recognition/VCTK-Corpus/wav48/p{0}/p{0}_013.wav".format(i)
        addr = "/home/user/Project_Python/Speaker_Recognition/VCTK-Corpus/wav48/p{0}/p{0}_011.wav".format(i)
        
        data = add_in_db.generate_speech(addr, "add", addr_01=0, addr_02=0) 

    """
    for i in range(225, 235, 1):
  
        for j in range(1, 10):
            f = open("Result/e1_sp10_l16.txt", 'a')
            print(">>p{0}_00{1}.wav".format(i, j))
            f.write("\n>>p{0}_00{1}.wav".format(i, j))
            addr = "/home/user/Project_Python/Speaker_Recognition/VCTK-Corpus/wav48/p{0}/p{0}_00{1}.wav".format(i, j)
            add_in_db.generate_speech(addr, "search")
            f.close()
        if i == 235:
            break
    
    """
# 225-265 (40 )
# 225-235 (10)
    