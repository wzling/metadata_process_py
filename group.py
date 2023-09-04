import csv
d = dict(groupsno = [], groupname = [])
in_path = '/Users/wangtzuling/Documents/python/ex2/group_ori.txt'
out_path = '/Users/wangtzuling/Documents/python/ex2/group.csv'
for line in open(in_path).readlines():
    for s in line:
        if line.find("groupsno") != -1 and s.isdigit():
            num = line.split()[1].replace(',', '')
            if num not in d['groupsno']:
                d['groupsno'].append(num)
        elif line.find("groupname") != -1:
            name = line[line.index(':')+3:-3]
            if name not in d['groupname']:
                d['groupname'].append(name)    
    open(in_path).close()

temp = list(zip(d['groupname'],d['groupsno']))
#print(temp)
with open(out_path, 'w', newline='',encoding='utf-8-sig') as out_csvfile:
    writer = csv.writer(out_csvfile)
    for line in temp:
        writer.writerow(line)
    out_csvfile.close()
        
