def factForLoop(n):
    #using for loop 
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact

def factWhileLoop(n):
    fact = 1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    return fact
        
        
number = int(input("Enter the number for return the factorial: "))
print(f'using for loop {factForLoop(number)}')
print(f'using while loop {factWhileLoop(number)}')
