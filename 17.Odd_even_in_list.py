#17. For a list that has numbers, find sum of odd numbers and sum of even numbers

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_even_inlist(lis):
    odd = 0
    even = 0
    for i in lis:
        if(i%2 != 0 ):
            odd += i
        elif(i%2 ==0):
            even += i
    return(odd,even)

ans = odd_even_inlist(list1)
print(ans)

'''
TESTCASES:
        INPUT                                                       OUTPUT
    1. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                               (25, 30)
    2. [-3,2,5,6,3]                                                  (5, 8)
    3. [-3,2,5,6,3,-15,-10]                                          (-10, -2)
    4. [0,0,0]                                                       (0,0)
    
    5.  [-0,0,'a']                                                   TypeError: not all arguments converted during string formatting
    
    '''
