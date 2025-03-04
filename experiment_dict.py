NYSC = {
    "state coordinator": "Mrs Ucheenna",
    "age": 51,
    "postion": "state coordinator"
}

print(NYSC["postion"])

NYSC["height"] = 5.7

print(NYSC)
for key, value in NYSC.items():
    print(key, value)

print ("Below is a try-out hand on exercise:")
#Create a dictionary with your name, age, and favorite food.
#Ask the user for their name, age, and favorite food, and store it in the dictionary.
#Print both your details and the user’s details.

my_details = {
    "name": "Ayo",
    "age": 25,
    "fav_food": "Rice"
}

print("My details are: ", my_details)
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_fav_food = input("Enter your favorite food: ")

user_details = { "name": user_name,
                 "age": user_age,
                 "fav_food": user_fav_food
                 }

print(f"Mrs/Mr {user_name} details are: {user_details} ")