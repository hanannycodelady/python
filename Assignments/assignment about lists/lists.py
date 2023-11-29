# changing item 80 t0 89
total_mark=[60,80,90,98] 
total_mark[1]=89
print(total_mark)

#Adding anew item
total_mark=[60,80,90,98]
total_mark.append(55)
print(total_mark)

# find the size of a list
print( len(total_mark))

#Write a python program to sum up all the items in the list
#summation of the items
total=sum(total_mark)
print(total)

#checklists if true or false
list_one=input("enter items")
list_two=input("enter items")

if list_one and list_two:
    print("true, if there is a common item")
    




