first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
operator = input("(+,-,*,/,%) : ")


first = int(first)
second = int(second)

if operator == "+":
    print(first, "+", second, "=", first + second)
elif operator == "-":
    print(first, "-", second, "=", first - second)
elif operator == "*":
    print(first, "*", second, "=", first * second)
elif operator == "/":
    print(first, "/", second, "=", first / second)
elif operator == "%":
    print(first, "%", second, "=", first % second)
#elif operator == "**":
   # print()
else:
    print("Invalid Input!!!")