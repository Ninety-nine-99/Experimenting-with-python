"""
Asks the user to enter a number.
Uses a for loop to print numbers from 1 to that number.
If the number is 5 or more, print "Great choice!" at the end.
"""

x = int(input("Enter a number: "))
for i in range(1,x+1):
    print(i)
if x >=5 :
    print("Great Choice")