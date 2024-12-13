'''
7 kyu - See You Next Happy Year

A "happy year" is one with no duplicate digits.
Given a random year, return the next "happy year"
'''

def create_digits(input):
    digits = []
    while input > 0:
        target = input % 10
        digits.insert(0, target)
        input //= 10
    return digits

def check_happy(input):
    test = len(input) == len(set(input))
    return test

def next_happy_year(year):
    
    if year < 1000 or year > 9000:
        print("Year should be within 1000 and and 9000")
    
    else:
        new_year = year + 1
        new_year_digits = create_digits(new_year)

        while check_happy(new_year_digits) == False:
            digits = create_digits(year)
            if not check_happy(digits):
                new_year += 1
                new_year_digits = create_digits(new_year)
               

    return new_year        
             
print(next_happy_year(1987))