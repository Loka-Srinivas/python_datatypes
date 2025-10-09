class Student:
    def __init__(self, name,roll_number):
        self.name=name
        self.roll_number=roll_number
        self._marks={}
        
    def add_mark(self, subject, mark):
        if mark >=0 and mark <=100:        #simple validation
            self._marks[subject]=mark    
        else:
            print("Invalid marks for", subject)
            
    def calculate_total(self):
        total=0
        for subject in self._marks:
            total=total+self._marks[subject] 
        return total
    
    def calculate_average(self):
        count=0
        for i in self._marks:
            count=count+1
            
        if count==0:
            return 0
        
        total=self.calculate_total()
        return total/count
    
    def get_report(self):
        pass                      #will be defined in child classes
    
class HighSchoolStudent(Student):
    def get_report(self):
        print("Report Card (High School)")
        print("Name:", self.name)
        print("Roll No:", self.roll_number)

        if not self._marks:
            print("No marks available.")
            return

        for subject in self._marks:
            print(subject + ":", self._marks[subject])

        total = self.calculate_total()
        avg = self.calculate_average()

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"

        print("Total:", total)
        print("Average:", avg)
        print("Grade:", grade)

class CollegeStudent(Student):
    def get_report(self):
        print("Report Card (College)")
        print('Name:', self.name)
        print('Roll No:', self.roll_number)

        if not self._marks:
            print("No marks available.")
            return

        for subject in self._marks:
            print(subject + ":", self._marks[subject])

        total = self.calculate_total()
        avg = self.calculate_average()

        if avg >= 85:
            grade = "Distinction"
        elif avg >= 70:
            grade = "First Class"
        elif avg >= 50:
            grade = "Pass"
        else:
            grade = "Fail"

        print("Total:", total)
        print("Average:", avg)
        print("Grade:", grade)


if __name__ == "__main__":
    # High School Student+
    s1 = HighSchoolStudent("Venkata", 101)
    s1.add_mark("Math", 95)
    s1.add_mark("Science", 88)
    s1.add_mark("English", 76)
    s1.get_report()

    # College student
    s2 = CollegeStudent("Narayana", 202)
    s2.add_mark("Math", 82)
    s2.add_mark('Machine Learning', 91)
    s2.add_mark("AI", 87)
    s2.get_report()


        
    
    
                               