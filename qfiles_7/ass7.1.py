
handle = None
file_name = input("Enter File Name: ")

try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\qfiles_7\words.txt')
except:
    print("Can not open File: ", file_name)
    quit()

for line in handle:
    print(line.rstrip().upper())
