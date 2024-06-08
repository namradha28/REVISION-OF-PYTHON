TRY-ELSE CLAUSE

#In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.
#For these cases, you can use the optional else keyword with the try statement.
# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
    