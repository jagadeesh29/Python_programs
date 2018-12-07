#7.  Given the area of the circle, write a program to print the radius
def find_radius_from_AOC():
    chk =1
    while chk:
        chk=0
        try:
            area_of_circle = float(input("enter the area of circle: "))
            if(area_of_circle <0):
                print("enter the positive values    ")
                chk=1
        except ValueError:
            print(("enter valid inputs"))
            chk = 1
    radiuss = ((area_of_circle/3.14)**(.5))
    print("the radius is : ",radiuss)
find_radius_from_AOC()

'''
Testcases:


    INPUT                                   OUTPUT
1.   25                              the radius is: 2.821 

2.   aaa                             enter valid inputs

3.   #@                              enter valid inputs 

4.   -6                              enter the positive values

5.    0                              the radius is: 0.0
'''