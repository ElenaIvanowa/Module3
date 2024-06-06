def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(7, 'Привет!', False)
print_params()
print_params(8)
print_params(b=25)          # неверный тип переменной, но результат выводится
#print_params(с=[1, 2, 3])    неверный тип переменной, результат не выводится

values_list = [5, 'яблоко', False]
values_dict= {'a':13, 'b':'кошка', 'c':True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
