from math import sqrt
num=int(input('Enter your number : '))
if num > 1 :
    for i in range(2,int(sqrt(num))+1):
        if (num % 1 == 0):
            print(num , 'is a not prime number')
            break
    else:
        print(num, 'is  a prime  number ')
else:
    print(num , 'is not prime number')