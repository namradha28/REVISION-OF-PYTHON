TRY-FINALLY 

#In Python, the finally block is always executed no matter whether there is an exception or not.
#The finally block is optional. And, for each try block, there can be only one finally block.

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")
    
