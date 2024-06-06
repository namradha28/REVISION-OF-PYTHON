CONDITIONS

#There are 3 types of conditions 
#1. If statement-he if statement checks a condition and executes the block of code within it if the condition is True.
x = 10
if x > 5:
    print("x is greater than 5")
#2. If-else statement- The if-else statement provides an alternative block of code to execute if the condition is False
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#3.Elif statement: The elif (short for "else if") statement allows you to check multiple conditions. It is used after an if statement and before an else statement.
x = 7
if x < 5:
    print("x is less than 5")
elif x < 10:
    print("x is between 5 and 10")
else:
    print("x is 10 or more")

#4. Nested if:You can nest if, elif, and else statements within each other to create more complex conditions.
x = 15
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is not greater than 20")
else:
    print("x is 10 or less")
