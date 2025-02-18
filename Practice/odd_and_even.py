number =  [12, 7, 34, 23, 45, 66, 89, 90, 41, 55]
even_numbers = []
odd_numbers = []

for x in number:

    if x % 2 == 0:
        even_numbers.append(x)
        # print(f"Even number: {x}")
    else:
        odd_numbers.append(x)
        # print(f"odd number: {x}")

print(f"Четные числа: {even_numbers}")
print(f"Нечетные числа: {odd_numbers}")
    
  