'''
7 kyu - last digits of a number

return the last d digits of n number
include any leading zeros, such that the output is always d digits long
'''

def solution(n,d):
    return [ int(digit) for digit in f"{n % (10 ** d):0{d}}" ]