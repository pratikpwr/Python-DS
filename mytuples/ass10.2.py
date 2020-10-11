handle = None

try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\mytuples\mbox-short.txt')
except:
    print("Error in opening File.")
    quit()

my_dict = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    hour = line.split()[5].split(':')[0]
    my_dict[hour] = my_dict.get(hour, 0) + 1

lst = list()

for k, v in my_dict.items():
    new_tup = (k, v)
    lst.append(new_tup)

new_list = sorted(lst)
for key, val in new_list:
    print(key, val)
