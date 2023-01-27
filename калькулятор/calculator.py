counter = 1 
q_num = float(input("кол-во чисел: ")) 
result = float(input("число: ")) 
 
while counter < q_num: 
    s_num = result 
    oper = input("действие: ") 
    f_num = float(input("число: ")) 
 
    while (f_num == 0 and oper == '/'): 
        print("на ноль делить нельзя!") 
        f_num = float(input("число: ")) 
 
    if oper == '+': result = s_num + f_num 
    elif oper == '-': result = s_num - f_num 
    elif oper == '*': result = s_num * f_num 
    elif oper == '/': result = s_num / f_num 
 
    counter += 1 
    if (counter < q_num): print("промежуточный результат: ", result) 
 
print("конечный результат: ", result) 
input()