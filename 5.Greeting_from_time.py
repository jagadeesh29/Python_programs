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


'''
Testcases:

    INPUT                  OUTPUT
1.    Jac                Good Night - Jac
2.    56                 
3.    @#$%^
4.    -6
5.    5.5

'''