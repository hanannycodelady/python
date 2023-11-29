# i) finding the average of two numbers
def calculating_average(x,y):
    return (x+y)/2

#Testing the function with different numbers

number_one=8
number_two=9

average=calculating_average(number_one,number_two)
print(f"The average of {number_one} and {number_two} is {average}")


# ii)

number_one=float(input("enter first number:"))
number_two=float(input("enter second number:"))
number_three=float(input("enter third number:"))

minimum=min(number_one,number_two,number_three)

print(f"the minimum number is:{minimum}")







