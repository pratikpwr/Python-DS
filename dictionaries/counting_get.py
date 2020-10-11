counts = dict()
names = ['Mac', 'Johny', 'Mia', 'Dani', 'Mia', 'Sophia']

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)
