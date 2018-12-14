#16. A list has numbers. Write a program to move odd number to start of the list and even number to the end of the list.
#    list = [1,2,3,4,5,6,7,8,9,10] should be transformed to [1,3,5,7,9,2,4,6,8,10]

def list_oddfirst_evensecond():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = []
    list3 =[]

    for i in list1:
        if(i%2 !=0):
            list2.append(i)
        elif(i%2 ==0):
            list3.append(i)
    return (list2+list3)

ans = list_oddfirst_evensecond()
print(ans)


'''
Testcases:

Input                                                   output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]               [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
[1, 2, 3,321, 4, 5, 6, 7, 8, 9,10,10]         [1, 3, 321, 5, 7, 9, 2, 4, 6, 8, 10, 10]
[a,b,c]                                       TypeError: not all arguments converted during string formatting       
[@]                                           TypeError: not all arguments converted during string formatting
[-1,0,0,-4, 2, 3, 4, 5, 6, 7, 8, 9, 10]       [-1, 3, 5, 7, 9, 0, 0, -4, 2, 4, 6, 8, 10]
[-1.5,0.5,0,-4, 2, 3, 4, 5, 6, 7, 8, 9, 10]   [-1.5, 0.5, 3, 5, 7, 9, 0, -4, 2, 4, 6, 8, 10]
'''
