import hashlib
import csv 
in_path = r'/Users/wangtzuling/scripts/python_script/ex2/p.csv'
out_path = r'/Users/wangtzuling/scripts/python_script/ex2/out_password.csv'
temp1 = []
with open(in_path,'r',encoding='utf_8_sig') as opened_csvfile:
    rows = csv.reader(opened_csvfile)
    for row in rows:
        temp1.append(row)
    opened_csvfile.close()
def t_sha256(in_list):
    temp2 = []
    for c in in_list:
        sha256 = hashlib.sha256((c.encode('utf-8')))
        s = sha256.hexdigest().upper()
        if s == 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855':
            s = ''
        temp2.append(s)
    return temp2
for n in range(len(temp1[0])):
    temp1[0][n] = temp1[0][n].replace('密碼', '_Password_current')
with open(out_path, 'w', newline='') as out_csvfile:
    writer = csv.writer(out_csvfile)
    writer.writerow(temp1[0])   #header
    for r in range(1,len(temp1)):
        print('row:',r)
        print(t_sha256(temp1[r]),'\n'+'----------------')
        writer.writerow(t_sha256(temp1[r]))
    out_csvfile.close()
 