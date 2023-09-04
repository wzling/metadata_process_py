import time
from alive_progress import alive_bar
from dataclasses import replace
import shutil
import os
from os import scandir, walk
from os.path import join
#城市代碼清單
flist = ['A','B','D','E','F','G','H','I',"J",'k','M','N','O','P','Q','T','U','V']
indir = (input('EX:""C:/Users/name/Downloads/RALID/""\n請輸入RKEYN資料夾位置(需要引號):')).replace('\\','/')
#indir = '/Users/wangtzuling/Downloads/RALID'
elapsed = 0
for f in flist:
    #進度條
    with alive_bar(spinner='dots_waves',unknown='wait',title=f'Processing_{f}') as bar:
        #計算運算時間
        start = time.perf_counter()
        #設定檔案目錄位置 
        dir = indir[1:-1] +f+'1/'
        #print('單一縣市所有RKEYN.txt之資料夾位置=',dir)
        out = open(dir[:-9]+'merged/'+f+'.txt','w',encoding='UTF-8',errors='ignore')
    f= "/Users/wangtzuling/Downloads/txt/V1.txt"
    out =  '/Users/wangtzuling/Downloads/done/V.txt'
    fo= open(f,encoding="utf8", errors='ignore')
    out_o = open(out,"w")
    out_o.write('段小段 地號 登記日期(年月日) 登記原因 面積 使用分區 使用地類別 公告土地現值 公告地價 縣市 鄉鎮市區 地段代碼 地政事務所'+'\n')
    temp = []
    for line in fo.readlines()[1:]:
        t = line.split(",")
        #print('before',t,'len=',len(t))
        c = t[11][0:2]
        t[11] = t[11][:-1]
        t.append(c)
        #print('after',t,'len=',len(t))
        for i in t[0:12]:
            out_o.write(i+',')
        out_o.write(t[12]+'\n')
    num_lines = sum(1 for line in open(out))
    print(num_lines+15)
    fo.close()
    out_o.close()

#-------------------- ToDo ----------------------   
#計算不重複資料筆數 >>與RKEYN比對


        
        
