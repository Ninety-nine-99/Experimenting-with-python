def sg():
    print("The Statistician General of NBS welcome you")

sg()


def director(name):
    print("ICT DIRECTOR name is", name)
director("Mustapha")
director("fafunmi")

for i in range(5):
    print(i)

def add(a, b):
    return a * b

result = add(4,3)
print(result)

#Takes one number as input.
#Returns the square of the number.
#Prints "The square of X is Y" where X is the number and Y is the result.

x = int(input("Enter a desired number: "))

def square(number):
    return number * number

y = square(x)

print(f"The square of {x} is {y}")


