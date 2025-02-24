from Person import Person

class Student(Person):
    def __init__(self, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(name, age)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._score_avg = score_avg
    
    def getFieldOfStudy(self):
        return self._field_of_study
    

    def getYearOfStudy(self):
        return self._year_of_study
    

    def getScoreAvg(self):
        return self._score_avg
    

    def printStudent(self):
        print(self.getPersonString() + "the field of study is " + self.getFieldOfStudy() + ", the year of study is " + str(self.getYearOfStudy()) + ", the avg is " + str(self.getScoreAvg())) 

    def printMySelf(self):
        self.printStudent()