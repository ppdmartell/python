dictionary = {"dog":"chien", "horse":"cheval", "cat":"xhat"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word,"->",dictionary[word])
    else:
        print(word, "is not in dictionary")

# "Iterating over a dictionary using keys() method"
print("\n'Iterating' over a dictionary")
for key in dictionary:
    print(key, "->",dictionary[key])

# If you want it sorted, you can use the sorted() method. However, sorted means naturally sorted,
# not representing the order they are in the dictionariy. And the sorting is done on the keys,
# not the values. By the way, starting from Python 3.7, dictionaries preserve the order of
# in which items are added.

# Important, starting from Python 3.7, the keys() method returns the keys in the saeme order
# are stored in the dictionary. As well as the values() and items() methods.

print("\nSorted naturally based on the first letter")
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])


# Returning the elements with items() returns tuples, where each tuple is a key value.
print(dictionary.items())

de = {"test":"1"}
print(de.items())

# Printing each key-value pair using a for loop
for key,value in dictionary.items():
    print(key, "->", value)

# Returning and printing the values only with values() method:
for value in dictionary.values():
    print(value)

# Important: A dictionary is not able to automatically find a key by using a value

# Replacing the value 'chat' with 'minou'
dictionary['cat'] = 'minou'
print(dictionary)

dictionary['swan'] = 'cygne'
print(dictionary)

# You can also insert an item to a dictionary by using the update() method
# Using the same update method, you can modify the value for an already existing key
dictionary.update({'duck':'canard'})
dictionary.update({'cat':'chat'})
print(dictionary)

# You can also iterate over a dictionary using a for loop. However, this will only iterate
# over the keys only.
for item in dictionary:
    print(item)


# To check if a given key is contained within a dictionary you can use the keyword in
if 'dog' in dictionary:
    print('Key dog is in the dictionary.')

# You can copy a dictionary to a new one using the method copy()
newd = dictionary.copy()
print(newd)

# You can empty the dictionary by using the method clear()
dictionary.clear()
print(dictionary)
