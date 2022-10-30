# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5

num = ''

def fun(num):
    for i in range(0,len(num)):
        if (num[i+1])-num[i] != 1:
            return num[i]+1

with open('input.txt', 'r') as data:
    
    num = data.read()

num = list(map(int, num.split()))

print(fun(num))