/* Aggregate Functions
1. COUNT() :
Returns the number of rows that matches a specified criterion. */
SELECT COUNT(*) AS it_department_count
FROM employees
WHERE department = 'IT';
 
 -- SUM():
-- Returns the total sum of a numeric column.
SELECT SUM(salary) AS total_salaries
FROM salaries;

-- AVG():
-- Returns the average value of a numeric column.
SELECT AVG(salary) AS avg_hr_salary
FROM salaries
WHERE department = 'HR';

-- MAX():
-- Returns the maximum value of a column.
SELECT MAX(salary) AS highest_salary
FROM salaries;

-- MIN()
-- Returns the minimum value of a column.
SELECT MIN(salary) AS lowest_salary
FROM salaries;
