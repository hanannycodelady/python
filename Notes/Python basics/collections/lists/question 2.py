#consider  two lists b=[1,1,2,3,4,5,6,7,8,9,10,11,12,13]
# write a program that turns a list that contains only the elements that are common  between a list without duplicate items

a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,1,2,3,4,5,6,7,8,9,10,11,12,13]
common_list=[]
for x in a:
    if x in b and not common_list:
        common_list.append([x])
print(type(common_list))
common_list=set(a)&set(b)
print(common_list)



print(len(a))
print(len(b))


print(common_list)