# 1.	כתוב פונקציה שמקבלת רשימה של מספרים, ומכפילה את כל האיברים ברשימה ב-2
# 2.	כתוב קוד שמקבל מהמשתמש 50 מספרים ושומר אותם ברשימה
# 3.	כתוב קוד שמדפיס את כל המספרים מ0 עד 1000
# 4.	 כתוב פונקציה שמקבלת רשימה, ומדפיס את כל האיברים בה, כאשר ליד כל איבר מופיע גם האינדקס שלו.

# 1.
def dblNumlst(integer_list):
    for index, number in enumerate(integer_list):
        integer_list[index] *= 2

# 2.
lst_usr = []
for index in range(50):
    num = input("Enter number for index " + str(index) + ": ")
    if num == "stop":
        break
    lst_usr.append(num) 


# 3.
for i in range(1001):
    print(i)

# 4.
def printList(list_user):
    for index, iterator in enumerate(list_user):
        print("Index " + str(index) + ": " + iterator)



# my_list = [1, 2, 3, 4]
# print(my_list)
# dblNumlst(my_list)
# print(my_list)

#print(getListFrmUsr())

# list_2 = ["ab", "cd", "ef", "gh"]
# printList(list_2)
