handle = None

try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\lists_8\mbox-short.txt')
except:
    print("Error in opening file")
    quit()

count = 0
for line in handle:
    if not line.startswith('From '):
        continue
    count = count + 1
    from_line = line.split()
    print(from_line[1])

print('There were ', count, 'lines in the file with From as the first word')
