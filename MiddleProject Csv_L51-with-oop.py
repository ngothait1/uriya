# Lesson 51 - Middle Project - Saving data to a csv file
# By OOP
import pandas as pd
from Person import Person
from Student import Student
from Employee import Employee

# final_Project_2_9

def mainFunc():
   count_entry = 0
   sum_age = 0
   while True:
      selection = printMenu()
      if selection == 1:
         age = saveNewEntry(main_dict, main_id_list)
         if age >= 0: 
            count_entry += 1
            sum_age += age
      elif selection == 2:
         serchByID(main_dict)
      elif selection == 3:
         printAgesAverage(sum_age, count_entry)
      elif selection == 4:
         printAllNames(main_dict)
      elif selection == 5:
         printAllIds(main_dict)
      elif selection == 6:
         printAllEntries(main_dict)
      elif selection == 7:
         printEntryByIndex(main_dict, main_id_list)
      elif selection == 8:
         saveDataToCsv(main_dict, count_entry)
      elif selection == 9:
         if choiseFunc("Are you sure? (y/n) "):
            print("Goodbye!")
            break
      input("Press enter to continue")


# function for menu

# 1. Save a new entry
def saveNewEntry(entries_dict, id_list):
   id = input("ID: ") # Error to check: 1. ID content char 2. ID is already exists.
   if not isIntNumber(id, "ID"):
      return -1
   id = int(id)
   if id in entries_dict: # is_already_exists
      print("Error: ID already exists: " + str(entries_dict[id]))
      return -1
   name = input("Name: ")
   age = input("Age: ") # Error to check: Input not integer
   if not isIntNumber(age, "Age"):
      return -1
   age = int(age)
   while True:
      status_choise = input("Are you a s-tudent or an e-mployee? Or n-either? (s/e/n) " )
      if status_choise == "s":
         field_of_study = input("Field of study: ")
         year_of_study = input("Year of study: ")
         score_avg = input("Score avg: ")
         status = "student"
         entries_dict[id] = Student(name, age, field_of_study, year_of_study, score_avg)
         break
      elif status_choise == "e":
         field_of_work = input("Field of work: ")
         salary = input("salary: ")
         entries_dict[id] = Employee(name, age, field_of_work, salary)
         status = "employee"
         break
      elif status_choise == "n":
         entries_dict[id] = Person(name, age)
         status = "person"
         break
   print("ID [" + str(id) + "] saved successfully as a " + status + ".")
   id_list.append(id)
   return age

# 2. Search by ID
def serchByID(entries_dict):
   id = input("enter the ID you want to look for: ")
   # Error to check: Input not integer, ID not exists.
   if not isIntNumber(id, "ID"):
      return -1
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
   for index, id in enumerate(entries_dict):
      print(str(index)+ ". " + str(entries_dict[id].getName()))
 
# 5. Print all IDs
def printAllIds(entries_dict):
   for index, id in enumerate(entries_dict):
      print(str(index)+ ". " + str(id))

# 6. Print all entries
def printAllEntries(entries_dict):
   for index, id in enumerate(entries_dict):
      print(str(index), end=". ")
      entries_dict[id].printMySelf()
              
# 7. Print entry by index
def printEntryByIndex(entries_dict, id_list):
   # Error 1
   if len(id_list) == 0:
      print("There are no entries in the database")
      return -1
   index = input("Please enter the index of the entry you want to print: ")
   # Error: Input not integer.
   if not isIntNumber(index, "Index"):
      return -1
   index = int(index)
   # Error: Index out of range.
   if index > len(id_list) - 1:
      print("Error: Index out of range. The maximum index allowed is " + str(len(id_list) - 1))
      return -1
   id = id_list[index]
   entries_dict[id].printMySelf()

# 8. Save all data
def saveDataToCsv(entries_dict, counter):
   data = []
   if counter <= 0:
      if not choiseFunc("There are no entries. Are you sure you want to export an empty file? (y/n) "):
         return -1
   file_name = input("What is your output file name? ")
   for index, id in enumerate(entries_dict):
      data_row = {"ID": id, "Name": entries_dict[id].getName(), "Age": entries_dict[id].getAge()}
      if str(type(entries_dict[id])) == "<class 'Student.Student'>":
         saveStudent(entries_dict, id, data_row)
      elif str(type(entries_dict[id])) == "<class 'Employee.Employee'>":
         saveEmployee(entries_dict, id, data_row)
      else:
         savePerson(data_row)
      data.append(data_row)
   df = pd.DataFrame(data)
   df.to_csv(file_name, index=False)
   print("The file saved successfully")
   
   
# 9. exit
## By the choiseFunc

# Auxiliary functions
def choiseFunc(ask):
   while True:
      choise = input(ask)
      if choise == "y":
         return True
      elif choise == "n":
         return False
 
def printMenu():
   print("1. Save a new entry")
   print("2. Search by ID")
   print("3. Print ages average")
   print("4. Print all names")
   print("5. Print all IDs")
   print("6. Print all entries")
   print("7. Print entry by index")
   print("8. Save all data")
   print("9. Exit")
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


def saveStudent(entries_dict, id, data_row):
   data_row["status"] = "Student"
   data_row["field_of_study"] = entries_dict[id].getFieldOfStudy()
   data_row["year_of_study"] = entries_dict[id].getYearOfStudy()
   data_row["score_avg"] = entries_dict[id].getScoreAvg()
   data_row["field_of_work"] = "_"
   data_row["salary"] = "_"

def saveEmployee(entries_dict, id, data_row):
   data_row["status"] = "Employee"
   data_row["field_of_study"] = "_"
   data_row["year_of_study"] = "_"
   data_row["score_avg"] = "_"
   data_row["field_of_work"] = entries_dict[id].getFieldOfWork()
   data_row["salary"] = entries_dict[id].getSalary()

def savePerson(data_row):
   data_row["status"] = "Person"
   data_row["field_of_study"] = "_"
   data_row["year_of_study"] = "_"
   data_row["score_avg"] = "_"
   data_row["field_of_work"] = "_"
   data_row["salary"] = "_"

# Error functions
def errOptionNotExist(in_put):
   print("Error: Option [" + str(in_put) + "] does not exist. Please try again")
   return -1

def isIntNumber(in_put, id_age_index): # is_integer_number
      if in_put.isdigit():
         return True
      else:
         print("Error: " + id_age_index + " must be a positive integer. " + in_put + " is not positive integer")
         return False        

# Run code
main_dict = {}
main_id_list = []
mainFunc()