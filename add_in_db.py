# -*- coding: utf-8 -*-
from features import mfcc
import scipy.io.wavfile as wav
import lbg
import sqlite3 as lite
import tkinter as tk
import sys
import traceback
import search_in_db as sdb

# Создание кластеризованного вектора признаков
def generate_speech(addr, text):
    try:
        (rate,sig) = wav.read(addr)
        name = addr.split('/')[-2]
        mfcc_feat = mfcc(sig, samplerate=rate, lowfreq=300, highfreq=4000, numcep=20)
        lbg_feat = lbg.generate_codebook(mfcc_feat, 16)[0]
        if text=="add":
            registry(name, lbg_feat)
        if text=="search":
            sdb.compare(lbg_feat)
    except ValueError:
        print("ValueErroe: Not a WAV file \nExit.")
        return -1
        
# Занесение пользователя в базу данных
def registry(name, feature_vector):
    db_users = lite.connect("db_users.bd")     
    curs = db_users.cursor()
    #root = tk.Tk()
    flag = True
    while flag:
        try:
            t = ("{0}".format(name), '{0}'.format(feature_vector))       
            curs.execute("INSERT INTO users(name, feat_vect) VALUES(?, ?)", (t))
            db_users.commit()
            flag = False
        except:
             print('er', ''.join(traceback.format_exception(*sys.exc_info())))
             #label_err_unique = tk.Label(root, text="Такой пользователь уже существует")
             #label_err_unique.pack()
        #else:
            #label_ok = tk.Label(root, text="Пользователь в базе")
            #label_ok.pack()
    db_users.close()
    #root.mainloop()
