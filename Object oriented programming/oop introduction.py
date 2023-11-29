# create a user class with properties ie name age location
# create anew instance of the user class(anew object)
# Access the users name and age
# create a function for the user for the user class that prints a users location
#print the users location using this function

# create a user class with properties ie name age location
class my:
    def _init_(my , name, age, location):
        my.name = name
        my.age = age
        my.location = location
        
# create anew instance of the user class(anew object)
my = my()

# Access the users name and age
name=input("enter your name:")
age=input("enter your age:")
print(name)
print(age)

# create a function for the user for the user class that prints a users location
def print_location(my):
        print("user's location:",my)


#print the users location using this function
print_location("kampala")

