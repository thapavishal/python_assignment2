str1 = input("string1: ")
str2 = input("string2: ")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if len(str1) == len(str2):
    if sorted_str1 == sorted_str2:
        print("Given stringsa are anagram")

    else:
        print("given strings are not anagrams")
else:
    print("Given strings are not anagram")
