# Take marks input from user for 3 subjects
s1 = int(input("Enter marks for Subject 1: "))
s2 = int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))

# Calculate total and average
total = s1 + s2 + s3
average = total / 3

# Check pass/fail conditions
if s1 >= 33 and s2 >= 33 and s3 >= 33:
    if average >= 40:
        print("Student has passed.")
    else:
        print("Student has failed due to less than 40% overall.")
else:
    print("Student has failed due to less than 33% in one or more subjects.")
