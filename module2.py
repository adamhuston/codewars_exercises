import random
# if

# if condition: grade is greater than or equal to 90, print "passed"
grade = random.randint(49, 100)
# otherwise, print "failed"

print(f"{grade} is the first grade")

if grade >= 90:
    print("passed")
else:
    print("failed")

# elif

grade = random.randint(0, 100)
print(f"{grade} is the next grade")

if grade >= 90:
    print("A")
elif grade >= 80:    
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:    
    print("failed")

# for

# for LOOPVARIABLE in SEQUENCE:
#     STATEMENT1

for i in range(10):
    print(i == range(10)[i])


# while

# find the first number that is a multiple of 3 
# that is larger than 50

product = 3 # initialize the product to 3

while product < 50:
    product *= 3
    print(product)

print(f"{product} is the first number that is a multiple of 3 that is larger than 50")


# we are not convinced the above is the best method of solving the problem as stated i
# it skips the first number that is a multiple of 3 that is larger than 50
# the above code tests the product after it has been multiplied by 3, giving us numbers that are 3^n (3 * 3 * 3...n times)
# here is another way to solve the problem, that finds the first number that is a multiple of 3 that is larger than 50
# we will use a while loop and a conditional statement to test the number
# we will initialize a variable to 50
# we will test if the number is a multiple of 3
# if it is not, we will increment the number by 1
test = 50
while test % 3 != 0:
    test += 1

print(f"{test} is the first number that is a multiple of 3 that is larger than 50")

# example 2
# let the user guess a number, repeatedly until they enter an even #
print("I'm thinking of a number!")
#initialize

guess = 1
'''
# while the number is odd (not even) keep asking the user to guess
while guess % 2 != 0:
    guess = int(input("Guess the number: "))
    print(f"you guessed {guess}")
# if we get here, the user entered an even number
print('Good job!')
print(f'{guess} is an even number')

# while loop example 3

# ask the user to enter a number
# max_num = int(input('Please enter an integer'))
current_num = 0

while current_num < max_num:
    print(current_num)
    current_num += 2
'''
# range

# print numbers 1 through 10
for eachNumber in range(1, 11):
    print(eachNumber, end=' ')


# augmented assignment
# +=, -=, *=, /=, %=, **=, //=

# add up all the numbers between 1 and 100

sum = 0
for i in range(1, 101):
    sum += i


# break
# continue
# and
# or
# not

# median
# mean
# mode