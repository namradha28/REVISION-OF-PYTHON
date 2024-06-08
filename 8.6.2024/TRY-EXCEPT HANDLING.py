TRY-EXCEPT HANDLING 

#The try...except block is used to handle exceptions in Python. 
#SYNTAX:
try:
    # code that may cause exception
except:
    # code to run when exception occurs

#Here, we have placed the code that might generate an exception inside the try block. Every try block is followed by an except block.

#When an exception occurs, it is caught by the except block. The except block cannot be used without the try block.
#EXAMPLE 
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0.