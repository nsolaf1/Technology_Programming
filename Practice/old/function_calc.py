def calc(a, b, oper):
    result = 0

    if oper == '+':
        result = a + b

    elif oper == '-':
        result = a - b
    elif oper == '%':
        result = (a*b)/100
    
    print(f"{a} {oper} {b} = {result}")
    return result


print("Выберите операцию: ")
print("1: Сложение (+)")
print("2: Вычитание (-)")
print("3: Умножение (*)")
print("4: Деление (/)")

oper=input("Введите номер операции: ")
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))

calc(a,b,oper)
