#9.  Given a number, find the next prime number (if 8 is the input, the function should return 11. If 11 is input, it should return 13)


chk = 2
while chk == 2:
    try:
        chk = 1
        n = int(input("select a  number, I'll print the next prime number :"))
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


def nex_prime(n):

    sq = (n**3)
    for i in range(n + 1, sq, 1):
        if (is_prime(i)):
            print("The next prime number of",n, "is",i)
            break
    if(n==0):
        print("The next prime number of 0 is 2")

    elif(n==1):
        print("The next prime number of 1 is 2")

nex_prime(n)



'''
TESTCASES:

        INPUT                       OUTPUT
    1. ASDF                         Enter Valid inputs

    2. -3                           Enter the positive numbers

    3.  @#                          Enter Valid inputs

    4.  0                           The next prime number of 0 is 2
    
    5.  1                           The next prime number of 1 is 2
    
    6.  11                          The next prime number of 11 is 13
    
    7.  12                          The next prime number of 12 is 13

'''