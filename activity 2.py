def primeSeive(n):
    prime = [True for i in range (n+1)]
    current=2
    while (current* current  <= n):
        if (prime[current]==True):
            for i in range(current **2,n+1,current):
                prime[i]=False
        current +=1
    prime[0]=False
    prime[1]=False
    for p in range(n+1):
        if prime[p]:
            print(p)

n =int(input('Enter number to find all prime number less than the number : '))
print('following number are smaller')
print('than or equal to') 
primeSeive(n)
