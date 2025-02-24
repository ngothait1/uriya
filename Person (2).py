class Person:
    def __init__(self, name, age): #id
        
        # self._id = id
        self._name = name
        self._age = age


    # def getId(self):
    #     return self._id
    

    def getName(self):
        return self._name
    
   
    def getAge(self):
        return self._age

    def getPersonString(self):
        return "The person " + self.getName() + " is " + str(self.getAge()) + " years old,"


    def printMySelf(self):
        print(self.getPersonString())

if __name__ == "__main__":
    print("You are runnig Person.py")
    #test_id = 101
    test_name = "uri"
    test_age = 2020
    person_test = Person(test_name, test_age) # test_id, 
    if person_test.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but I got " + str(person_test.getAge())) 
    if person_test.getName() != test_name:
        print("Error: Name should be " + test_name + " but I got " + person_test.getName())

    