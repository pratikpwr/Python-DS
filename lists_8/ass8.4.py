handle = None

try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\lists_8\myromeo.txt')
except:
    print("Error in opening file")
    quit()

total_words = []

for line in handle:
    words_in_line = line.split()
    # print(words_in_line)
    for word in words_in_line:

        if word not in total_words:

            total_words.append(word)

total_words.sort()
print(total_words)
