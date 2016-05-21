# -*- coding: utf-8 -*-

import xlwt

f = open("e1_sp10_l16.txt", 'r')
inf = []
res = []
beg = 225
wb = xlwt.Workbook()
ws = wb.add_sheet('list1', cell_overwrite_ok=True)
   
while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        inf += [line.split('\n')[0]]   
        
for i in range(1, len(inf), 2):
    res += [inf[i].split(' ')[1]]
#res = res[90:]
k = 1
for i in range(0, len(res), 9):
    coef = 0
    ws.write(k, 0, 'p{0}'.format(beg+k-1))
    for j in range(9):
        ws.write(k, j+1, res[i+j])
        if res[i+j] == 'p{0}'.format(beg+k-1):
            coef += 1
    ws.write(k, 10, coef/9)
    k+=1
   
wb.save("file2.xls")
f.close()