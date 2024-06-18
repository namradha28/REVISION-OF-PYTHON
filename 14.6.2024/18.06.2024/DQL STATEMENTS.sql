/* DQL, or Data Query Language, is a subset of SQL (Structured Query Language) that focuses on retrieving data from a database. 
DQL primarily involves the use of the SELECT statement, which allows you to query and fetch data from one or more tables in a database.
 Here's a breakdown of its components and how it works:*/
 
 -- 1.SELECT Statement:
-- The SELECT statement is used to specify the columns of data you want to retrieve.
SELECT FirstName, LastName, Salary
FROM Employees;

 -- FILTERING DATA:
 SELECT FirstName, LastName, Salary
FROM Employees
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'Sales');

-- USING AGGREGATE FUNCTIONS:
SELECT DepartmentID, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DepartmentID;

-- JOINING TABLES:
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID;

-- ORDERING DATA:
SELECT FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;

-- GROUPING DATA 
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
 
 -- USING JOINS:
 SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.id;

-- COMBINING CLAUSES:
SELECT first_name, last_name, department
FROM employees
WHERE salary > 50000
ORDER BY salary DESC;

 
 



