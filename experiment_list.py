members = ["ayo", "mama", "mummy ayo", "big mummy"]
print(members)
members[2] = "Titilola"
members[3] = "Yinka"
members[1] = "morenike"
print(members[0:4])

members.append("israel")
members.remove("ayo")
print(members[0])


# Write a Python program that:

# Creates a list of 3 favorite foods.
# Asks the user for a new favorite food and adds it to the list.
# Prints the updated list.

print("Below is a hand on an exercise: ")

name = input("What is your name: ")
fav_food = ["Rice", "Beans", "plantain"]
print("Mr ayo Favourite food are : ", fav_food)
user_fav_food = input(f"Enter your favorite food {name}: ")
fav_food.append(user_fav_food)
print("Now my favourite food and yours is: ", fav_food)


print("Below are the fav_food listed out one by one: ")
for foods in fav_food:
    print(foods)
