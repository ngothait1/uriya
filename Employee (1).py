from Person import Person

class Employee(Person):
    def __init__(self, name, age, field_of_work, salary):
        super().__init__(name, age)
        self._field_of_work = field_of_work
        self._salary = salary
    

    def getFieldOfWork(self):
        return self._field_of_work
    

    def getSalary(self):
        return self._salary
    

    def printEmployee(self):
        print(self.getPersonString() + " the field is " +
                self.getFieldOfWork() + ", the salary is " + str(self.getSalary()))
    

    def printMySelf(self):
        self.printEmployee()