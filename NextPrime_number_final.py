# n = int(input("enter the number:"))
# y = int(input("which element you want after current prime no"))
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return False
                break;
        return True
    else:
        return False


# n=3, y= 0, sq =9
def nex_prime():

    n = int(input('Enter the prime or non prime number you want to start from: '))
    y = int(input("enter the element which you want to find: "))

    sq = n ** 2
    for i in range(n + 1, sq, 1):
        if (is_prime(i)):
            y -= 1
            if (y == 0):
                return i
                break


nex_prime()
