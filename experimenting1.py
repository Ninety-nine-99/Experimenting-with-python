"""
Asks the user for their temperature in Celsius.
If the temperature is above 30°C, print "It's hot!"
If the temperature is between 20°C and 30°C, print "The weather is nice!"
If the temperature is below 20°C, print "It's cold!

"""

celsius = int(input("Enter your temperature in Celsius: "))
if celsius > 30:
    print("It is hot")
elif  20 <= celsius <= 30:
    print("The weather is nice!")
else:
    print("It is cold")


