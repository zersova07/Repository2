def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def sum_numbers_month(days):
    z = []
    for i in range(1, days + 1):
        z.append(int(str(i)[0]))
        if(i > 9):
            z.append(int(str(i)[1]))
    return sum(z)

def sum_numbers_months(february):
    return sum_numbers_month(31) * 7 + sum_numbers_month(30) * 4 + sum_numbers_month(february)


check = check_leap_year(int(input("Введите год: ")))

if check == False: print("Сумма: ", sum_numbers_months(28))
else: print("Сумма: ", sum_numbers_months(29))