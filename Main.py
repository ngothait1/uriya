# Lesson 66 - Final Project - Saving data to a csv file by oop
# On base Lesson 51 - Middle Project by oop

import pandas as pd
from person import Person
from student import Student
from employee import Employee
from menus import mainMenu
from utils import Utils as ut
import os



def mainFunc():
   try:
      global count_entry, sum_age
      while True:
         selection = printMenu()
         if selection < 0:
            pass
         elif selection == 1:
            age = saveNewEntry(main_dict, main_id_list)
            if age >= 0: 
                  count_entry += 1
                  sum_age += age
         else:
            func_list = ["none",
                        lambda: serchByID(main_dict),
                        lambda: printAgesAverage(sum_age, count_entry),
                        lambda: printAllNames(main_dict),
                        lambda: printAllIds(main_dict),
                        lambda: printAllEntries(main_dict),
                        lambda: printEntryByIndex(main_dict, main_id_list),
                        lambda: saveDataToCsv(main_dict),
                        lambda: exitProgram(main_dict)       
                        ]
            func_list[selection - 1]()
         input("Press enter to continue")
   
   except KeyboardInterrupt:
      try:
         warningKeyboard()
         exitProgram(main_dict)
         mainFunc()
      except KeyboardInterrupt:
            warningKeyboard("again")
   except FileNotFoundError as e:
      print("\n===== There may be an error in the file name. =====")
      print("Error: " + str(e))
      mainFunc()
   except Exception as e:
      print("\n===== An error occurred =====")
      print("Error: " + str(e) + "\n") # type(e).__name__
      mainFunc()

def warningKeyboard(again=""):
   print("\nWarning! Process was interrupted by the user " + again + " == KeyboardInterrupt ==")
   if again == "again":
      saveDataToCsv(main_dict, True)
      print("Goodbye!")
      exit()


# function for menu

# 1. Save a new entry
def saveNewEntry(entries_dict, id_list):
    id = input("ID: ") # Error to check: 1. ID content char 2. ID is already exists.
    ut.isIntNumber(id, "ID")
    id = int(id)
    if id in entries_dict: # is_already_exists
        print("Error: ID already exists for -->")
        entries_dict[id].printMySelf()
        return -1
    name = input("Name: ")
    age = input("Age: ") # Error to check: Input not integer
    ut.isIntNumber(age, "Age")
    age = int(age)
    while True:
        print()
        person_types = [Student, Employee, Person]
        print("===== Select a status from the list =====")
        for index, status in enumerate(person_types):
            print(str(index) + ". ", end="")
            print(status.__name__)
        choise = input("Enter status (by index): " )
        ut.isIntNumber(choise, "index")
        choise = int(choise)
        if choise in range(0,3):
            entries_dict[id] = person_types[choise](name, age)
            break
        else:
               print("Error: Your input out of range")
    status = entries_dict[id].__class__.__name__
    print("ID [" + str(id) + "] saved successfully as a " + status + ".")
    id_list.append(id)
    return age
      

# 2. Search by ID
def serchByID(entries_dict):
   if len(entries_dict) == 0:
      print("There are no entries in the database")
      return -1
   id = input("enter the ID you want to look for: ")
   # Error to check: Input not integer, ID not exists.
   ut.isIntNumber(id, "ID")
   id = int(id)
   if id not in entries_dict:
      print("Error: ID " + str(id) + " is not saved")
      return -1
   entries_dict[id].printMySelf()
   
     
# 3. Print ages average
def printAgesAverage(sum_age, count_entry):
   if count_entry > 0:
      print(sum_age / count_entry)
   else:
      print(0)

# 4. Print all names
def printAllNames(entries_dict):
   if isEmptyDatabase(entries_dict):
      return -1
   for index, id in enumerate(entries_dict):
      print(str(index)+ ". " + str(entries_dict[id].getName()))
 
# 5. Print all IDs
def printAllIds(entries_dict):
   if isEmptyDatabase(entries_dict):
      return -1
   for index, id in enumerate(entries_dict):
      print(str(index)+ ". " + str(id))

# 6. Print all entries
def printAllEntries(entries_dict):
   if isEmptyDatabase(entries_dict):
      return -1
   for index, id in enumerate(entries_dict):
      print(str(index), end=". ")
      entries_dict[id].printMySelf()
              
# 7. Print entry by index
def printEntryByIndex(entries_dict, id_list):
   # Error 1
   if isEmptyDatabase(id_list):
      return -1
   index = input("Please enter the index of the entry you want to print: ")
   # Error: Input not integer.
   ut.isIntNumber(index, "Index")
   index = int(index)
   # Error: Index out of range.
   if index > len(id_list) - 1:
      print("Error: Index out of range. The maximum index allowed is " + str(len(id_list) - 1))
      return -1
   id = id_list[index]
   entries_dict[id].printMySelf()

# 8. Save all data
def saveDataToCsv(entries_dict, auto_save=False):
   global num_entries_is_save
   if auto_save and not isEmptyDatabase(entries_dict):
      file_name = "auto_save_data.csv"
   elif auto_save:
      return -1
   if isEmptyDatabase(entries_dict) and not auto_save:
      if not choiseFunc("Are you sure you want to export an empty file? (y/n) "):
         return -1
   data = []
   if not auto_save:
      file_name = input("What is your output file name? ")
   ut.isCsvSuffix(file_name, ".csv")      
   for id in entries_dict:
      data_row = entries_dict[id].getDataAsDictionary()
      data_row["ID"] = id
      data.append(data_row)
   df = pd.DataFrame(data)
   df.to_csv(file_name, index=False)
   num_entries_is_save = len(entries_dict)
   if auto_save:
      print("The process has been stopped. Backup file saved:\n" + file_name + " in path: " + str(os.getcwd()))
   print("The file saved successfully")
   
   
# 9. exit
def exitProgram(entries_dict):
   global num_entries_is_save
   if num_entries_is_save < len(entries_dict):
      not_save = len(entries_dict) - num_entries_is_save
      print("!! There are " + str(not_save) + " unsaved entries !!")
   if choiseFunc("Are you sure you want to exit the program? (y/n) "):
      print("Goodbye!")
      exit()


# Auxiliary functions
def choiseFunc(ask):
   while True:
      choise = input(ask)
      if choise == "y":
         return True
      elif choise == "n":
         return False
 
def printMenu():
   for option in mainMenu:
    print(option.value, end=". ")
    print(option.name.replace("_", " ").title())
   choise = input("Please enter your choise: ")
   if not choise.isdigit(): # is_integer_number
     return errOptionNotExist(choise)
   choise = int(choise)
   if choise > 0 and choise < 10: # in_range
     return choise
   else:
     return errOptionNotExist(choise)


def printEntry(entries_dict, id):
   print("ID: " + str(id))
   print("Name: " + str(entries_dict[id].getName()))
   print("Age: " + str(entries_dict[id].getAge()))


def isEmptyDatabase(database):
   if len(database) == 0:
      print("There are no entries in the database")
      return True
   else:
      return False


# Error function
def errOptionNotExist(in_put):
   print("Error: Option [" + str(in_put) + "] does not exist. Please try again")
   return -1


# Run code
main_dict = {}
main_id_list = []
count_entry = 0
sum_age = 0
num_entries_is_save = 0
mainFunc()