# A longer but simple Python conditional program

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
    print("Excellent performance!")
elif marks >= 75:
    print("Grade: A")
    print("Very Good! Keep it up.")
elif marks >= 60:
    print("Grade: B")
    print("Good work, but you can improve.")
elif marks >= 45:
    print("Grade: C")
    print("You passed, but study harder.")
elif marks >= 30:
    print("Grade: D")
    print("You barely passed. Try again with more focus.")
else:
    print("Grade: F")
    print("You failed. Don’t give up, study and try again!")
