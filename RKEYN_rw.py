# encoding:utf-8
import os
import numpy as np
#indir = (input('EX:"C:/Users/name/Downloads/unzip/"\n請輸入unzip資料夾位置(如有錯誤，需加上引號):')).replace('\\','/')
indir = '/Users/wangtzuling/Downloads/unzip'
#----------所有RKEYN資料夾路徑--------------
rkeynfile = []
for root, dirs, files in os.walk(indir,topdown = False):
    for name in dirs:    
        if os.path.join(root,name).find('RKEYN') != -1:
            rkeynfile.append(os.path.join(root,name))
#print(rkeynfile)
#---------------讀取XXXXXX_RKEYN.TXT內容-------------------
def r_txt(file):
    tl = []
    ofile = open(file,'r',errors='ignore')
    for line in ofile.readlines()[1:]:
        if line[0:2] == '48' and line.find('代碼') == -1:
            tl.append(line)
    ofile.close()
    return tl
#print(len(r_txt('/Users/wangtzuling/Downloads/unzip/T_屏東縣/TB/RKEYN/TB0202_RKEYN.TXT')))
#print(r_txt('C:/Users/lyric/Downloads/unzip/A_臺北市/AA/RKEYN/AA0149_RKEYN.TXT'))
#-----------------c2_code---------------------------------
c2_l=[]
for i in range(len(rkeynfile)):
    c2_code = rkeynfile[i][rkeynfile[i].find('RKEYN')-3:rkeynfile[i].find('RKEYN')-1]
    c2_l.append(c2_code)
    c2_list = list(set(c2_l))       
#print(c2_list)

#-----------------一個c2內的所有txt的路徑=rkeynfile內的路徑+txt檔名-------------------------
def c2txtdir(c2filedir):
    txtdir_l = []
    for root, dirs, files in os.walk(c2filedir,topdown = False):
        for fname in files:    
            txtdir_l.append(os.path.join(root,fname)) #c2內所有的txt路徑放進txtdir_l
    return txtdir_l
#print(len(c2txtdir(rkeynfile[0])))
#------------處理暫存資料、存成c1.txt---------------------
def list2txt(out):
    outlist = []
    c1 = out[0][0]
    c2 = out[0]
    del out[0]
    for i in range(len(out)):
        t = out[i].split(',')
        del t[0]
        t[0] = c2+t[0]
        t[2] = t[2][:-1]
        t.append(c1)
        t.append(c2)
        outlist.append(t)
    outf = open(indir[:-6]+'merged/'+c1+'/'+c2+'.txt','w',encoding='UTF-8',errors='ignore')
    outf.write('地段代碼,段小段名别,鄉鎮市區,縣市,地政事務所代碼'+'\n') #header
    for data in outlist:
        for w in data[:4]:
            outf.write(w+',')
        outf.write(data[4]+'\n')
    outf.close()
###################################################################################
#--------------把c2內所有txt暫存成矩陣---------------------
for i in range(len(rkeynfile)):
    out = 0
    t = []
    for txtdir in c2txtdir(rkeynfile[i]):
        #print(txtdir,'共有',len(r_txt(txtdir)),'筆資料','\n',r_txt(txtdir),'\n')
        if t ==[]:
            t.append(rkeynfile[i][rkeynfile[i].find('RKEYN')-3:rkeynfile[i].find('RKEYN')-1])
        t.append(r_txt(txtdir))
    #print(len(t))
    #print(t[0])
    a = np.array(t,dtype=object)
    #print(len(a[1]))
    #print(len(a))
    #-----------------c2 check if data in all txt match------------------------------
    for j in range(len(a[1])):
        for i in range(len(a)):
            if i != 0 and i+1<=len(a)-1:
                if a[i][j] != a[i+1][j]:
                    print('OH NO!','\n','第',i-1,'個的第',j,'行: ',a[i-1][j],'\n','第',i,'個的第',j,'行: ',a[i][j])
                if i+1>len(a):
                    break
            out = a[1]
    out.insert(0,a[0])
    list2txt(out)
#print(len(out))
#print(out)
    #print(out[0],len(out),'\n-------------------')
    print(t[0],'真正資料數目=',len(t[1]))
    print(t[0],'內有的txt檔數目=',len(t)-1,'\n')

#-----------------------把c2.txt結合成c1.txt----------------------------
#temp = []
#for c2 in c2_list:
#    outf = open(indir[:-6]+'merged/'+c2+'.txt','r',errors='ignore')

###################################################################################
#-------------------- ToDo ----------------------   
#mkdir c1 >> list2txt()
#merge (c2.txt)*n >> (c1.txt)*1
#找出異常值:地段代瑪out[0] alpha數量 != 2 >>計算筆數 & 擷取出來另外存放