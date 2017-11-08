import re

f = open('access.log', 'r')
IP = re.findall('(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', f.read())
f.close()

Set_IP = set()
List_IP = list()

for i in IP:
    Set_IP.add(i)
List_IP = list(Set_IP)
List_IP.sort()

prev = ['0', '0', '0', '0']
for line in List_IP:
    cur = line.split('.')
    if int(prev[0]) == int(cur[0]) and int(prev[1]) == int(cur[1]) and int(prev[2]) == int(cur[2]):
        pass
    else:
        print()
        print(cur[0] + '.' + cur[1] + '.' + cur[2] + '.xxx')
    print(line)
    prev = cur