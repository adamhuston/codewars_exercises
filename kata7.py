'''
6 kyu - who likes it?
#BattleRattle

Description:
Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.'''


def likes(names):
    match(names):
        case []: return "no one likes this"
        case [name]: return f"{name} likes this"
        case [name1, name2]: return f"{name1} and {name2} like this"
        case [name1, name2, name3]: return f"{name1}, {name2} and {name3} like this"
        case [name1, name2, name3, name4]: return f"{name1}, {name2} and 2 others like this"
        case _: return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"