# practising with tuples
# Accessing tuples

marks=(80,79,69,70)
marks[0]
print(type(marks))
print(marks[0])  # accessing the tuple
print(len(marks)) # length of a tuple

marks=(80,)
print(type(marks))

# Check weather 79 exists in the variable marks,
# print 77 is a member
#check weather 88 belongs to variable marks, if not u print variable does not exist

marks=(80,79,69,70)
if 79 in marks:
    print("yes, 79 exists in tuple marks")
else:
    print("no , does not exist in tuple marks")
if 88 in marks:
    print("yes,if 88 does not exist")
else:
    print("no, 88 does not exist")
    
Age=20
Name= "Hananny"
print(f"Am {Name} and i am {Age} years old")

marks=(60,79,69,70)
# changing a tuple into a list
new_marks=list(marks)
print(type(new_marks),new_marks)
# changing from 79 to 80
new_marks[1]=88
print(new_marks)
# changing a list to a tuple using a tuple contractor
print(tuple(new_marks))
# adding 99 to the tuple 
new_marks.append(99) 
print( tuple(new_marks))

# Another way of appending using tuples

updated_marks=tuple(new_marks)
updated_list_marks=list(updated_marks)
updated_list_marks.append(100)
print(tuple(updated_list_marks))



