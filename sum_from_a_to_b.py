'''сумма чисел от числа_1 до числа_2'''
from_num = int(input())
to_num = int(input())
summ = 0
i = from_num
while i <= to_num:
    summ += i
    i += 1
print(summ)