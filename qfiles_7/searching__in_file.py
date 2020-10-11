handle = open('D:\My Projects\Python Projects\pythonDataStructures\qfiles_7\mbox.txt')

for line in handle:
    line = line.rstrip()
    if line.startswith("The"):
        print(line)
