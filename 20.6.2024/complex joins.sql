/* Complex Joins
Let's assume we have three tables: employees, departments, and projects.

Tables
employees */
SELECT e.first_name, e.last_name, d.department_name, p.project_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
LEFT JOIN projects p ON ep.project_id = p.project_id
WHERE p.start_date > '2023-01-01' AND p.end_date < '2024-01-01';

/* Subqueries
Example of a Subqueries */
SELECT 
    e.first_name, 
    e.last_name, 
    (SELECT department_name FROM departments d WHERE d.department_id = e.department_id) AS department_name
FROM employees e;

/* Date-Time Functions
Assuming we have the employees table with a hire_date column. */
SELECT 
    employee_id, 
    EXTRACT(YEAR FROM hire_date) AS hire_year,
    EXTRACT(MONTH FROM hire_date) AS hire_month,
    EXTRACT(DAY FROM hire_date) AS hire_day
FROM employees;

SELECT 
    employee_id, 
    TO_CHAR(hire_date, 'YYYY-MM-DD') AS formatted_hire_date
FROM employees;
