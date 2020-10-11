handle = None
spam_adds = 0.0
lines_adds = 0

# file_name = input("Enter File name:")
file_name = 'D:\My Projects\Python Projects\pythonDataStructures\qfiles_7\mbox-short.txt'
try:
    handle = open(file_name)
except:
    print('File Cannot be opened: ', file_name)
    quit()

for line in handle:

    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    lines_adds = lines_adds + 1
    float_line = float(line[20:26])
    spam_adds = spam_adds + float_line

    print(float_line)
print("spam sum", spam_adds)
print("lines Sum", lines_adds)

average = spam_adds / lines_adds
print("Average spam confidence:", average)
