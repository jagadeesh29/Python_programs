
'''

#1. print the
#2.  Print the strings - "Hello, World", "Python is a wonderful language", "I am beginner in Python"
print("Hello, World", "Python is a wonderful language", "I am beginner in Python")

#3.  Assign the strings in the previous exercise to a variable and use the variable to print the string
string1 = ("Hello, World", "Python is a wonderful language", "I am beginner in Python")
print(string1)

#4.  Get the name of the user as input and greet the user saying "Hi <firstname>"
def name():
    name = input("enter your name : ")
    print('Hi',name)
name()
'''
#5.  Get the name of the user as inputs and greet the user saying "Good Morning, <firstname>" or "Good Afternoon, <firstname>" depending upon the time of the day
def greeting_from_time():

    username = input("enter your name: ")
    import datetime
    now = datetime.datetime.now()
    time = str(now.time())
    morning = 'Good Morning'
    afternoon = 'Good Afternoon'
    evening = 'Good Evening'
    night = 'Good Night'
    if(int(time[:2]) < 12):
        print (morning,'-',username)
    elif((int(time[:2]) >=12) and (int(time[:2]) <= 17)):
        print( afternoon,'-', username)
    elif(int(time[:2]) >17 and int(time[:2]) <=20):
        print(evening,'-', username)
    else:
        print(night,'-',username)

greeting_from_time()

#testcases

'''
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

#7.  Given the area of the circle, write a program to print the radius
def find_radius_from_AOC():
    chk =1
    while chk:
        chk=0
        try:
            area_of_circle = float(input("enter the area of circle: "))
            if(area_of_circle <0):
                print("enter the positive values: ")
                chk=1
        except ValueError:
            print(("enter valid inputs"))
            chk = 1
    radiuss = ((area_of_circle/3.14)**(.5))
    print("the radius is : ",radiuss)
find_radius_from_AOC()


#8.  Given a number, find whether or not it is prime
def prime_no(prime_val):
    #prime_val = int(input("enter the number you want to check prime or not: "))
    if(prime_val >1):
            if(prime_val % 2 ==0):
                print("not a prime")
            else:
                print("prime number")
    else:
        print("enter the positive or number greater than 1")
prime_no(55)
'''