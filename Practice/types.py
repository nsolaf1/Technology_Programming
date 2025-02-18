# fruits = ("apple", "banana", "cherry", "PIe", "asdasd", "a123123")
# (green, *yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"mango", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)


# thisset = {"apple", "asd", "cherry"}
# thisset.discard("banana")
# print(thisset)


# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964,
#  "year": 2020,
#  "year": 2022
# }
# print(thisdict)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change