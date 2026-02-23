membershipType = int(input("Membership Type: \n 1. Gold \n 2. Silver \n 3. Bronze: \n"))
amount = float(input("Enter amount: "))
discount = 0

if membershipType == 1:
    if amount > 100:
        # discount 20
        discount = 0.2
    else:
        # discount 10
        discount = 0.1

elif membershipType == 2:
    if amount > 100:
        # discount 15
        discount = 0.15
    else:
        # discount 5%
        discount = 0.05

elif membershipType == 3:
    if amount > 100:
        # discount 5%
        discount = 0.05
    else:
        # discount 0%
        discount = 0
else:
    print("Choose from 1.. 3")

discount_amount = amount * discount
finalPrice = amount - discount_amount

print(f"Your discount is: {discount_amount:.2f}" )
print(f"You price: {finalPrice:.2f}")


# print(amount - (amount*discount))


    
