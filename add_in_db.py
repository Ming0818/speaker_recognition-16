# -*- coding: utf-8 -*-
from features import mfcc
import scipy.io.wavfile as wav
import lbg
import sqlite3 as lite
import str_in_list as ls
import sys
import traceback
import search_in_db as sdb


def lgb(addr):
    try:
        (rate,sig) = wav.read(addr)
        koef = 16
        name = addr.split('/')[-2]
        mfcc_feat = mfcc(sig, samplerate=rate, lowfreq=300, highfreq=4000, numcep=20)
        return name,lbg.generate_codebook(mfcc_feat, koef)[0]
    except ValueError:
        print("ValueErroe: Not a WAV file \nExit.")
        return -1
    
# Создание кластеризованного вектора признаков
def generate_speech(addr, text, addr_01=0, addr_02=0,):
    if text=="add": 
        """
        db_users = lite.connect("db_users.bd")     
        curs = db_users.cursor()
        name = addr.split('/')[-2]
        curs.execute("SELECT * FROM users WHERE name='{0}'".format(name))
        data = curs.fetchall()
        lbg_feat = []
        for i in range(len(data)):
            lbg_feat += ls.str_list(data[i][1])
        curs.close() 
        """
        (name, lbg_feat) = lgb(addr)
        """
        lbg_feat_01 = lgb(addr_01)[1]
        lbg_feat_02 = lgb(addr_02)[1]
        for i in range(len(lbg_feat)):
            for j in range(len(lbg_feat[0])):
                lbg_feat[i][j] = (lbg_feat[i][j] + lbg_feat_01[i][j]+lbg_feat_02[i][j])/3
      #  db_users.close()
                """
        registry(name, lbg_feat)
    if text=="search":
        lbg_feat = lgb(addr)[1]
        sdb.compare(lbg_feat)
    
        
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

def update(name, feature_vector):
    db_users = lite.connect("db_users.bd")     
    curs = db_users.cursor()
    try:    
        curs.execute("UPDATE users SET feat_vect='{0}' WHERE name='{1}'".format(feature_vector, name))
        db_users.commit()
    except:
        print('er', ''.join(traceback.format_exception(*sys.exc_info())))
    db_users.close()

"""
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
        lbg_feat = lbg.generate_codebook(mfcc_feat, 32)[0]
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
"""