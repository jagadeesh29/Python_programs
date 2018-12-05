
myDict = [{'name': 'jac', 'age': 25, 'email': 'jacdeesh@gmail.com'},
          {'name': 'bhush', 'age': 25, 'email': 'bhuz@gmail.com'},
          {'name': 'jayan', 'age': 23, 'email': 'jayanth@gmail.com'},
          {'name': 'geherut', 'age': 79, 'email': 'gerUt@gmail.com'}
          ]

def search(myDict):


    search_str = input("enter the search you want to search: ") #1.getting input from user


    search_list =[]#2.creating a list to save the values and show the output
    Flag = 0
    for i in myDict:#3.iterating the list
        for key, value in i.items():#4. Iterating the dictionary values in the list
    #5. If the value matches the input string, appending the "name" into the list
            if (search_str == str(value)):
                search_list.append(i['name'])
                Flag=1
    print(search_list)
    #6. Setting flag to return true or false to the print the if there is no match
    if Flag==1:
        return False
    else:
        return True
#7. if the above function returns true  it should print there is no match
if (search(myDict)):
    print("there is no match")


