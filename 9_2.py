'''Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).'''

file = input('Enter file name:')
dict_words = dict()
try:
    file = open(file)
except:
    print('File does not exist')
    exit()

for line in file:
    words = line.split()
    if not line.startswith('From ') : continue
    else:
        dict_words[words[2]] = dict_words.get(words[2],0) + 1
print(dict_words)
