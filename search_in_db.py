import sqlite3 as lite
import str_in_list as ls
import math
    

# Сравнение вектора признаков с базой
def compare(feat_vect):
    # Считывание информации с базы, и запись её в массив
    db_feat_vect = []
    db_users = lite.connect("db_users.bd")     
    curs = db_users.cursor()
    curs.execute('SELECT * FROM users')
    data = curs.fetchall()
    for i in range(len(data)):
        db_feat_vect += [ls.str_list(data[i][1])]
    curs.close()   
    
    distanse = []
    for i in range(len(data)):
        distanse += [distance_between_elem_sizebook(db_feat_vect[i], feat_vect)]
    min_dist = distanse.index(min(distanse))        
    print("result", data[min_dist][0])
    f = open("Result/e1_sp10_l16.txt", 'a')
    f.write("\nresult "+data[min_dist][0])
    f.close()
        
    
    #f.close()
    #window_hello_user = tk.Tk()
    #lab = tk.Label(window_hello_user, text="Соответствие \n{0}".format(data[min_dist][0]))
    #lab.pack()
    #window_hello_user.mainloop()

  
def distance_between_elem_sizebook(code_book, feat_vect):
    min_dist = []
    for i in range(len(code_book)):
        arr_dist = []
        for k in range(len(feat_vect)):        
            dist = 0
            for j in range(len(feat_vect[0])):
                #wth
                dist += (code_book[i][j]-feat_vect[k][j])**2
            arr_dist += [math.sqrt(dist)]   
        min_dist += [min(arr_dist)]
    
    result = 0
    for i in range(len(min_dist)):
        result += min_dist[i]
    result = result/len(min_dist)
    return result
 