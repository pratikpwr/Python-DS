handle = None

try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\dictionaries\mbox-short.txt')
except:
    print("Error in opening file")
    quit()

my_dict = dict()
total_words = list()

for line in handle:
    if not line.startswith('From '):
        continue

    words_in_line = line.split()
    email = words_in_line[1]

    my_dict[email] = my_dict.get(email, 0) + 1

max_word = None
max_count = None

for mail, count in my_dict.items():
    if max_count is None or count > max_count:
        max_count = count
        max_word = mail

print(max_word, max_count)
