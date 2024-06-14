/*Aggregate functions in SQL are used to perform calculations on multiple rows of a table's column and return a single value. 
These functions are often used with the GROUP BY clause. 
Here are the most commonly used aggregate functions:
COUNT(): Returns the number of rows.
SUM(): Returns the total sum of a numeric column.
AVG(): Returns the average value of a numeric column.
MAX(): Returns the maximum value in a column.
MIN(): Returns the minimum value in a column.*/

-- ASSUME EXAMPLE 
CREATE TABLE jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    company_id INT,
    salary DECIMAL(10, 2),
    date_posted DATE
);

INSERT INTO jobs (title, company_id, salary, date_posted) VALUES
('Software Engineer', 1, 60000.00, '2024-06-01'),
('Data Analyst', 2, 55000.00, '2024-06-05'),
('Project Manager', 1, 75000.00, '2024-06-10'),
('Designer', 3, 50000.00, '2024-06-15'),
('System Admin', 2, 65000.00, '2024-06-20');

-- COUNT:
SELECT COUNT(*) AS total_jobs FROM jobs;
-- SUM:
SELECT SUM(salary) AS total_salary FROM jobs;
-- AVG:
SELECT AVG(salary) AS average_salary FROM jobs;
-- MAX:
SELECT MAX(salary) AS highest_salary FROM jobs;
-- MIN:
SELECT MIN(salary) AS lowest_salary FROM jobs;


