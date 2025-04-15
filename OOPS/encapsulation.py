class Students:
    def __init__(self,name,year,section):
        self.name=name
        self.year=year
        self.section=section

    def get_detail(self):
        return f"{self.name.upper()} and {self.year.upper()} and {self.section.upper()} !!" 

class Year_1(Students):
    def __init__(self,name,year,section,no_of_students):
        super().__init__(name,year,section)
        self.no_of_students=no_of_students
    def counts(self):
        return f"{self.name}.upper() and {self.year}.upper() and {self.section}.upper() and {self.no_of_students}.upper()"

frist_year_students=Students("Yash Jain","2023","Section : B")
print(frist_year_students.get_detail())