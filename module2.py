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
    print("passed")
elif grade >= 80:    
    print("almost there")
else:    
    print("failed")

# for



# while

# range
# break
# and
# or
# not

# median
# mean
# mode