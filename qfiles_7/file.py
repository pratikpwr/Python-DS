
handle = None
try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\qfiles_7\mbox.txt')
except:
    print("File Can not be Opened.")
    quit()
countLines = 0
countWords = 0
for lines in handle:

    print(lines.rstrip())
    countLines = countLines + 1
    for word in lines:
        countWords = countWords + 1


# length = handle.read()
# print("Total length:", len(length))
print("Total lines Count:", countLines)
print("Total Words Count:", countWords)
