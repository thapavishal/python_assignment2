list1 = ['ana', 'bhoo', 'creeti', 'dewan', 'eve']
print(list1)
list1.append('zoo')
list1.insert(0, 'nepal')
print("Updated list: ", list1)
print(list1.sort())

"""
list1 = []

list1.append('luke')
list1.append('hobbs')
list1.append('shankar')
list1.append('robot')
list1.append('apple')
list1.append('queen')
list1.append('oliver')
print(list1)
sorted_list = sorted(list1)
print(sorted_list)

for name in sorted_list:
    first = sorted_list[0]
    last = sorted_list[-1]
print(first)
print(last)
"""

"""
list1 = [{'name': "john", 'id': 1}, {'name': "cena", 'id': 5},
         {'name': "shankar", 'id': 3}]

print(list1)

print(sorted(list1, key=lambda i: i['id']))
"""
