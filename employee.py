from person import Person, ut

class Employee(Person):
    # def __init__(self, name, age, field_of_work, salary):
    #     super().__init__(name, age)
    #     self._field_of_work = field_of_work
    #     self._salary = salary
    
    def __init__(self, name, age):
        super().__init__(name, age)
        self._field_of_work = input("Field of work: ")
        salary = input("salary: ")
        ut.isPositiveNumber(salary, "salary")
        self._salary = salary
        
        
    def getFieldOfWork(self):
        return self._field_of_work
    

    def getSalary(self):
        return self._salary
    

    def printEmployee(self):
        print(self.getPersonString() + ", the field is " +
                self.getFieldOfWork() + ", the salary is " + str(self.getSalary()))
    

    def printMySelf(self):
        self.printEmployee()
    

    def getDataAsDictionary(self):
        row_data = super().getDataAsDictionary()
        row_data["status"] = "Employee"
        row_data["field_of_work"] = self.getFieldOfWork()
        row_data["salary"] = self.getSalary()
        return row_data