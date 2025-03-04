def name(name):
    print("My name is Ayo")
    print(f"I am {name} a data scientist")


name("Ayo")

# Convert your program into a function called get_user_details().
# Call the function and print both your details and the user’s details.


def personal_details():
    my_details = {
        "name": "Ayo",
        "age": 25,
        "fav_food": "Rice"
    }

    print("My details are: ", my_details)


def get_user_details(name, age, fav_food):
    user_details = {"name": user_name,
                    "age": user_age,
                    "fav_food": user_fav_food
                    }
    print(f"{user_name} details are: {user_details} ")
    print("Below are the user details listed out one by one: ")
    for key, value in user_details.items():
        print(key, value)


user_name = input("Enter your name: ")

while True:
    try:
        user_age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for your age.")

while True:
    user_fav_food = input("Enter your favorite food: ")
    if user_fav_food.isdigit():
        print("Please enter a valid food name, not a number.")
    else:
        break

personal_details()
get_user_details(user_name, user_age, user_fav_food)


