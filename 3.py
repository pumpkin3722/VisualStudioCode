shoplist = ['apple', 'mango', 'carrot']
items = len(shoplist)
print('I have ', items, ' items to buy')
print('These items are: ')

# Iterate over list items
for item in shoplist:
    print(item, end=' ')
# add item to list
shoplist.append('rice')
print('My list is now ', shoplist)
# Sort the list
shoplist.sort()
print('Sorted list is', shoplist)
print('The first item is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

my_list = ['p','r','o','g','r','a','m']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-3])
# elements 1st to 3rd
print(my_list[:2])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])


nested = ["hello", 2.0, 5, [10, 20]]
nested[3][1]
print(nested[3][1])


shoplist = ['apple', 'mango', 'carrot']
mylist = shoplist
# mylist is another name pointing to same object!
# Remove item from list
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# They are both the same – point to same object
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# now they are different



zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))


ab = {
    'David': 'david.sims@imm.ox.ac.uk',
    'Charlie': 'charlotte.george@imm.ox.ac.uk',
    'Spammer': 'spammer@hotmail.com'
    }
print("David’s email is", ab['David'])
print('There are', len(ab), 'contacts')
# Returning a value
email = ab.get('David', 0)
# Returns 0 if not found
# Deleting a key-value pair
del ab['Spammer']
# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
# Searching the keys
if 'Guido' in ab:
    print("Guido's address is", ab['Guido'])

for name in ab.keys():
    print(name)
for address in ab.values():
    print(address)
for name, address in ab.items():
    print(f'Mail {name} at {address}')