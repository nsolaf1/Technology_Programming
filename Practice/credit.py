salary = int(input("Enter Salary: "))
credit = int(input("Enter credit score: "))

if salary > 50000:
    if credit > 700:
        print("Кредит одобрен с низкой процентной ставкой.")
    else:
        print("Кредит одобрен, но с высокой процентной ставкой")
elif salary < 50000 and salary > 0:
    if credit > 700:
        print("Approved")
    else:
        print("NOT approved")
else:
    print("error")
