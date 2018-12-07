#6.  Given the radius of the circle, write a program to print the circumference and area of the circle. Write functions to calculate area and circumference
def Circle():


    chk_sel = 1
    while (chk_sel):
        chk_sel =0
        try:
            selection = int(input("select 1 for calculate area of circle\nselect 2 for calculate circumference of circle\nselect 3 for calculate both\nselect here = "))

            if(selection >=1 and selection <=3):
                #print("Enter the valid numbers between 1 and 3")
                radiuss = float(input("Enter the radius: "))
                if(radiuss < 0 ):
                    print("enter positive value for radius")
                    chk_sel = 1

                else:
                    chk_sel =0
            else:
                print("Enter the valid numbers between 1 and 3")
                chk_sel =1
        except ValueError:
            print("enter valid radius")
            chk_sel=1

    aoc = (3.14 * (radiuss ** 2))
    coc = (2 * 3.14 * radiuss)
    def area_of_circle_circumference():
        if( selection ==1):
            print("the area of circle is: ",aoc)
        elif(selection ==2):
            print("The circumference of circle is: ",coc)
        elif(selection == 3):
            print("the area of circle is: ",aoc,"\nThe circumference of circle is: ",coc)
        else:
            print("enter valid inputs")

    area_of_circle_circumference()
Circle()

'''
Testcases:


    INPUT                                           OUTPUT
1.   selection = 3,radius           the area of circle is:  50.24 
                                     The circumference of circle is:  25.12
                                     
2.   radius =  -1                    Enter the valid numbers between 1 and 3

3.   radius =  0                     the area of circle is:  0.0 
                                     The circumference of circle is:  -0.0
                                     
4.   radius = -6                     enter positive value for radius

5.   radius = 5.5                    the area of circle is:  94.985 
                                     The circumference of circle is:  34.54
                                     
6.   4d                              enter valid radius

7.   AAA                             enter valid radius


'''