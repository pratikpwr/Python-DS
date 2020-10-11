# program to count top ten common words
handle = None

try:
    handle = open('D:\My Projects\Python Projects\pythonDataStructures\lists_8\mbox-short.txt')
except:
    print("Error in opening file")
    quit()

new_tup = []
my_dict = dict()

for line in handle:
    words_in_line = line.split()

    for word in words_in_line:
        my_dict[word] = my_dict.get(word, 0) + 1

# bigger code
lst = list()
for k, v in my_dict.items():
    new_tup = (v, k)
    lst.append(new_tup)

lst = sorted(lst, reverse=True)
print(lst)
# using list comprehension in one line
print(sorted([(v, k) for (k, v) in my_dict.items()], reverse=True))

for val, key in lst[:10]:
    print(key, val)

x, y = 3, 4
print(x, y)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])