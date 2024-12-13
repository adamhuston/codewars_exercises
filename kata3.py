'''
7 kyu - even times last
Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.

Indices in sequence start from 0.

If the sequence is empty, you should return 0.

'''

def even_last(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers[::2]) * numbers[-1]