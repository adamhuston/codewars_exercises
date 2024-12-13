'''
7 kyu - Disemvowel trolls

You want to punish trolls by removing vowels from their posts


'''

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return "".join(char for char in string_ if char not in vowels)

print(
    disemvowel("test this string")
)
