#  write a python function to find the ;maximum of three numbers
# a=70 , b= 80, c=65
def maximum_value(a,b,c):
    if a>b and a>c :
        print(f"{a} is greater than{b} and {c}")
    elif b>a and b>c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")
maximum_value (70,80,65)



# write a python programme to sum all numbers in the list
# = [8,2,3,0,7]
def sum_of_numbers(a,b,c,d,e):
    output= a+b+c+d+e
    print(f"The sum {a} and {b} and {c} and {d} and {e} is {output}")
sum_of_numbers(8,2,3,0,7)


# write a python programme to reverse a string[1,2,3,4,a,b,c,d]
def reversed_string(input_string):
    reversed_str = input_string[::-1]
    return reversed_str
input_str = "1,2,3,4,a,b,c,d"
reversed_str = reversed_string(input_str)
print (reversed_str)


# write a python function to multiply all the number in a list[8,2,3,-1,7 ]
def multiply_lists(numbers):
    result=1
    for num in numbers:
        result*=num
    return result
numbers=[8,2,3,-1,7]
print(multiply_lists(numbers))


# write a python programme to print the even numbers in a given list[1,2,3,4,5,6,7,8,9]

numbers=[1,2,3,4,5,6,7,8,9]
for items in numbers:
    if items% 2 ==0:
        print(items)









































































































































































































































