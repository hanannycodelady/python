student_marks=[70,80,90,68]
# Data type  of student_name
print(type(student_marks))
# print student_name 
print(student_marks)
# list accessing
#positive indexing
print(student_marks[2])

# negative indexing
# it start with from the left (-1,-2,-3)
print(student_marks[-2])

# list slicing 
print(student_marks[2:3])
#check if item exists
if 80 in student_marks:
    print("yes, 80 exists in the list") 
else:
    print("no ,80 does not exist")
