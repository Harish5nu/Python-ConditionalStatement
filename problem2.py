#Q. write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# Take marks input from user for 3 subjects
s1 = int(input("Enter marks for Subject 1: "))
s2 = int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))

#checks for total percentage
total_percentage=(100*(s1+s2+s3))/300

if(total_percentage>=40 and s1>=33 and s2>=33 and s3>=33):
    print("You passed", total_percentage)

else:
    print("You failed try again", total_percentage)