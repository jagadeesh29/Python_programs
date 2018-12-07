def change_case():
    chk = 1
    while chk==1:
        chk = 0
        user_input = input("enter the string you want to change:")
        if type(user_input) == int:
            print("Please enter string values, then only we can proceed..")
            chk=1
        user_selection = int(input("1.Uppercase\n2.Lowercase\n3.Camelcase"))
        if(user_selection < 1 or user_selection >3):
            print("enter the number between 1 and 3")
            chk=1

    if(user_input == user_input.upper()):
        print("Its is already in UPPERCASE")
    elif(user_input == user_input.lower()):
        print("Its is already in lowercase")
    elif(user_input == user_input.title()):
        print("Its is already in camelcase")


    if(user_selection==1):
        upp = (user_input.upper())
        print(upp)
    elif(user_selection==2):
        loww = ((user_input.lower()))
        print(loww)
    elif(user_selection==3):
        camel = user_input.title()
        print(camel)
change_case()





