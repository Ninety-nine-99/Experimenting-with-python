def name(name):
    print("My name is Ayo")
    print(f"I am {name} a data scientist")


name("Ayo")

# Convert your program into a function called get_user_details().
# Call the function and print both your details and the user’s details.


def get_user_details(name, age, fav_foods):
    user_details = {~
        "name": name,
        "age": age,
        "fav_food": fav_foods
    }
    print(f"\n{name}'s details are: {user_details}")
    print("\nBelow are the user details listed one by one:")
    for key, value in user_details.items():
        print(f"{key}: {value}")

def personal_details():
    my_details = {
        "name": "Ayo",
        "age": 25,
        "fav_food": ["Rice"]
    }
    print("\nMy details are:", my_details)


# Get user input
user_name = input("Enter your name: ")

while True:
    try:
        user_age = int(input("Enter your age: "))
        break
    except ValueError:
        print("⚠️ Please enter a valid number for your age.")

# Collect multiple favorite foods
user_fav_foods = []
while True:
    user_fav_food = input("Enter your favorite food: ")
    if user_fav_food.isdigit():
        print("⚠️ Please enter a valid food name, not a number.")
    else:
        user_fav_foods.append(user_fav_food)
        break

# Ask if they want to add more favorite foods
while True:
    user_more_fav_food = input("Enter another favorite food? (yes/no): ")
    if user_more_fav_food.lower() == "yes":
        user_new_fav_food = input("Enter your favorite food: ")
        user_fav_foods.append(user_new_fav_food)
    elif user_more_fav_food.lower() == "no":
        break
    else:
        print("⚠️ Please enter 'yes' or 'no'.")

# Call functions
personal_details()
get_user_details(user_name, user_age, user_fav_foods)



#Ask the user if they want to add more favorite foods.
#2️⃣ Store multiple favorite foods in a list instead of a single value.

# below is the code for the above task
#Enter another favorite food? (yes/no): yes
#Enter your favorite food: Pizza
#Enter another favorite food? (yes/no): no







