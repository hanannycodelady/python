# consider a list a=[1,1,2,3,5,8,13,21,34,55,89]
# Write a program that bring all the elements of a list that are less than  5


# CREATING AN EMPTY LIST
a=[1,1,2,3,5,8,13,21,34,55,89]
for b in a:
    if b<5:
        print(b)


# storing the items in a list
new_list=[]
for s in a:
    if s<5:
        new_list.append(s) 
        new_list.sort()
print(new_list)



