number_one = input ("Enter input 1: ") # this will take input as a string
number_two = input ("Enter input 2: ")

total = number_one + number_two # this will concatenate two strings
print ("Total is: " + total)

number_1 = int (input ("Enter number 1: ")) # This will convert string to integer
number_2 = int (input ("Enter number 2: "))

total = number_1 + number_2 # this will add two strings

print ("Total is: " + str (total)) # We can't concatenate string with integers so we use str()

name, age = "hannan", 21

print ("Your name is " + name + " and your age is " + str (age))

age1 = age2 = age3 = 24

print (age1, age2, age3)


name, age = input ("Enter your name and age: ").split (",") #can be comma or any other string

print (name, age)