'''Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.'''

file = input('Enter file name:')
dict_addresses = dict()
dict_list = list()
try:
    file = open(file)
except:
    print('File does not exist')

for line in file:
    words = line.split()
    if not line.startswith('From ') : continue
    else:
        dict_addresses[words[1]] = dict_addresses.get(words[1], 0) + 1
        
for address, frequency in list(dict_addresses.items()):
            dict_list.append((frequency, address))
        
dict_list.sort(reverse = True)
                              
print(dict_list)

print(max((dict_list)))
