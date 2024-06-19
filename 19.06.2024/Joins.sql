/* SQL joins are used to combine rows from two or more tables based on a related column between them.
 Here's an explanation of different types of joins with examples using a hypothetical "APNA" database, which might include tables 
 like employees, departments, projects, and salaries.*/
 
 -- 1. INNER JOIN:
--  Returns records that have matching values in both tables.
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;

-- 2.LEFT JOIN (or LEFT OUTER JOIN):
--  Returns all records from the left table, and the matched records from the right table. If no match is found, NULL values are returned for columns from the right table.
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

-- 3.RIGHT JOIN (or RIGHT OUTER JOIN)
  /*Returns all records from the right table, and the matched records from the left table.
 If no match is found, NULL values are returned for columns from the left table. */
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.department_id;

-- 4.FULL JOIN (or FULL OUTER JOIN)
/* Returns all records when there is a match in either left or right table. 
If there is no match, the result is NULL on the side where there is no match. */
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
FULL OUTER JOIN departments ON employees.department_id = departments.department_id;

-- 5.CROSS JOIN
/*Returns the Cartesian product of the two tables.
 Each row from the first table is combined with all rows in the second table.*/
 SELECT employees.first_name, employees.last_name, projects.project_name
FROM employees
CROSS JOIN projects;

-- 6. SELF JOIN
/*Joins a table with itself. 
This is useful for hierarchical data.*/
SELECT e1.first_name AS employee, e2.first_name AS manager
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.employee_id;

-- NATURAL JOIN
/* Based on all columns in the two tables that have the same name and selects rows with equal values in the relevant columns. */
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
NATURAL JOIN departments;
