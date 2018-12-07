#8.  Given a number, find whether or not it is prime

chk =2
while chk==2:
    try:
        chk =1
        n = int(input("enter the number you want to check whether prime or not:"))
        if(n<0):
            print("Enter the positive numbers")
            chk=2
    except ValueError:
        print("Enter Valid inputs")
        chk=2

def is_prime(n):

    if(n == 0 or n==1):
        print("Not a prime")
    elif n > 1:
        for i in range(2, n):
            if (n % i == 0):
                print("not a prime number")
                break
        else:
            print("prime")
    else:
        print("Enter the Valid inputs")
is_prime(n)

'''
TESTCASES:

        INPUT                       OUTPUT
    1. ASDF                         Enter Valid inputs
    
    2. -3                           Enter the positive numbers
    
    3.  @#                          Enter Valid inputs
    
    4.  0                           Not a prime
    
    5.  1                           Not a prime
    
    6.  2                           prime
    
    7.  23                          prime
    
    8.  55                          Not a Prime
    
    9.  " "                         Enter Valid Inputs

'''