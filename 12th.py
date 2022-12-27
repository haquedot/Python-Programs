# taking two inputs at a time using split
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()
# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print()
# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
