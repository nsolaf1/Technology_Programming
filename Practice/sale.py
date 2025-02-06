membership = input("Тип членство(золото, серебро, обычный):")
amount = float(input("Сумма покупки:"))

if membership == "золото":
    if amount > 100:   
        discount = 0.20
    else:
        discount = 0.10
        
elif membership == "серебро":
    if amount > 100:
        discount = 0.15
    else:
        discount = 0.05

elif membership == "обычный":
    if amount > 100:
        discount = 0.05
    else:
        discount = 0
else:
    discount = 0
    print("Некорректный тип членства.")
    
print(f"Ваша скидка:{amount * discount}")
