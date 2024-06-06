LOOPS

#There are two types of loops 
#1.For loop-A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and perform a block of code for each element in that sequence. 
#The iteration stops once all elements in the sequence have been processed.

#2.While loop-With the while loop we can execute a set of statements as long as a condition is true.


# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
#BREAK STATEMENT: With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#CONTINUE STATEMENT:With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#RANGE STATEMENT: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)
#PASS STATEMENT: for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
