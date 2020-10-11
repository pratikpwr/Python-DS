my_list = [1, 2, 3, 4]
print(my_list)

# lists are mutable
my_list[2] = 6
print(my_list)

my_list.append(6)
print(my_list)

my_list.pop(0)
print(my_list)

my_list.sort()
print(my_list)
print(sum(my_list))
print("number of 6:", my_list.count(6))
