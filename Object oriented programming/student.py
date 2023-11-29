# A class starts with capital letters and in singular
#A class has properties or attributes
class Student:
    # student_number
    # name
    # email
    # contact
    # cohort
    # age
    def _init_(self, student_number, name, email, contact, cohort, age):
        self.student_number= student_number
        self.name=  name
        self.email= email
        self.contact= contact
        self.cohort= cohort
        self.age=age

    def __str__(self) :
        return f'{self.student_number},{self.name}'
    def name_email_cohort(self):
        return f'{self.name},{self.email},{self.cohort}'
        


# OBJECT/INSTANCE
# for you to create an instance or object each should have the same attribute from the class
student1=Student('2023/DCSE/00107/ss','wanjiku hananny','hanannyw@gmail.com','0740598271','cohort 3','20')
print(student1)


# create a function that prints the student name and their cohort,email
# Access this function using instance or object of the class