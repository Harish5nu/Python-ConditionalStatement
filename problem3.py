#Q. A  spam comment if defined as a text containing following keywords:
# "Make a lot of money", " buy now", "subscribe this", " click this ". write a program to detect these spams.

s1="Make a lot of money" 
s2="buy now"
s3="subscribe this"
s4="click this"
message=input("Enter your comment: ")

if ((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
    print("This is spam")
else:
    print("This is not spam")