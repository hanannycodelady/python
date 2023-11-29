# write a python programme that counts the total number of even and odd numbers in the tuple(1,2,3,4,5,6,7,8)

import dataclasses


numbers=(1,2,3,4,5,6,7,8)
count_even=0
count_odd=0
for x in numbers:
    if x%2==0:
        count_even+=1
    else:
        count_odd+=1
#print("even numbers",count_even)
#print("odd numbers",count_odd)


#using functions 

def count_even_and_odd(numbers):
    count_even=0
    count_odd=0
for x in numbers:
    if x%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"even number are {count_even} and odd numbers are {count_odd}")
count_even_and_odd(numbers)


# create a programme that return the sum of the multiplies of seven and the multiples and the multiples of five
def sum_of_numbers(numbers):
    sum_of_seven=0
    sum_of_five=0
for y in numbers:
    if y%7==0:
        sum_of_seven+= y
    if y%5==0:
        sum_of_seven+= y
        
print(f"{sum_of_seven}")
    









