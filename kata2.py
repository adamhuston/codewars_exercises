'''
7 kyu - Complete The Pattern #1
Function should return (not print) a string of the following pattern, including new line characters. 

1
22
333
4444
...
...
nnn...


If n<1, return an empty string
'''

def pattern(n):
    step = 1
    string = ""
    while step <= n:
        for i in range(step):
            string = string + str(step)
        string += "\n"
        step += 1
    return string