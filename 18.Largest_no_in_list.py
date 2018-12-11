#18. Write a program to find the largest number in the list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14,27,34,23,43,12,23]

def largest_no_of_list(lis):

    maxx =0
    for i in lis:
        if(i > maxx):
            maxx = i
    print(maxx)
largest_no_of_list(list1)