#10. Given a number, find the prime number that comes first when we count backwards. (if 11 is input, it should return 7. If 9 is inputs, it should return 7)

chk = 2
while chk == 2:
    try:
        chk = 1
        n = int(input("select a  number, I'll print the previous prime number :"))
        if (n < 0):
            print("Enter the positive numbers")
            chk = 2
    except ValueError:
        print("Enter Valid inputs")
        chk = 2

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return False
                break;
        return True
    else:
        return False


def previous_prime(n):

    if(n==0 or n==1 or n==2):
        print(" No prime numbers are there before",n)
    for i in range(n -1, 0, -1):
        if (is_prime(i)):
            print("The previous prime number of",n, "is",i)
            break


previous_prime(n)

'''
TESTCASES:

        INPUT                       OUTPUT
    1. ASDF                         Enter Valid inputs

    2. -3                           Enter the positive numbers

    3.  @#                          Enter Valid inputs

    4.  0                           No prime numbers are there before 0
    
    5.  1                           No prime numbers are there before 0
    
    6.  2                           No prime numbers are there before 0
    
    7.  12                          The previous prime number of 12 is 11
    
    8.  9                           The previous prime number of 9 is 7
    
    '''

