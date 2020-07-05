"""
filename = "myfile.txt"
filename.partition('.')

filename, seperator, extension = filename.partition('.')

print(filename)
"""


name = "README.txt"
ext_name = name[6:]
print("This is the extension name:", ext_name)
filename = name[:6]
print("This is the filename:", filename)
