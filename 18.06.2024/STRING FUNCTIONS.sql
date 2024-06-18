/* In SQL, inbuilt functions (or built-in functions) are predefined functions provided by the SQL database management system to perform various operations on data.
 These functions can be categorized into several types, including string functions, numeric functions, date functions, and aggregate functions. 
Below are some common inbuilt functions along with examples using an assumed "APNA" database. */

-- STRING FUNCTIONS:
-- CONCAT():
-- Concatenates two or more strings.
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

-- LENGTH():
-- Returns the length of a string.
SELECT first_name, LENGTH(first_name) AS name_length
FROM employees;

-- UPPER():
-- Converts a string to uppercase.
SELECT first_name, UPPER(first_name) AS upper_first_name
FROM employees;

-- LOWER()
-- Converts a string to lowercase.
SELECT last_name, LOWER(last_name) AS lower_last_name
FROM employees;



