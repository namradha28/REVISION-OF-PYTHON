/*SQL joins are used to combine rows from two or more tables based on a related column between them. 
There are several types of joins available in SQL:

INNER JOIN: Returns records that have matching values in both tables.
LEFT JOIN (LEFT OUTER JOIN): Returns all records from the left table and the matched records from the right table. The result is NULL from the right side if there is no match.
RIGHT JOIN (RIGHT OUTER JOIN): Returns all records from the right table and the matched records from the left table. The result is NULL from the left side when there is no match.
FULL JOIN (FULL OUTER JOIN): Returns all records when there is a match in either left or right table. It combines the result of both LEFT JOIN and RIGHT JOIN.
CROSS JOIN: Returns the Cartesian product of the two tables, i.e., all possible combinations of rows.*/

-- ASSUME EXAMPLE 
CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

CREATE TABLE jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    company_id INT,
    salary DECIMAL(10, 2),
    date_posted DATE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- Sample data for companies
INSERT INTO companies (name, location) VALUES
('Apna Inc.', 'Bangalore'),
('Tech Solutions', 'Mumbai'),
('Innovate Labs', 'Delhi');

-- Sample data for jobs
INSERT INTO jobs (title, company_id, salary, date_posted) VALUES
('Software Engineer', 1, 60000.00, '2024-06-01'),
('Data Analyst', 2, 55000.00, '2024-06-05'),
('Project Manager', 1, 75000.00, '2024-06-10'),
('Designer', 3, 50000.00, '2024-06-15');

-- INNER JOIN:
SELECT jobs.title, companies.name AS company_name
FROM jobs
INNER JOIN companies ON jobs.company_id = companies.company_id;

-- LEFT JOIN:
SELECT companies.name AS company_name, jobs.title
FROM companies
LEFT JOIN jobs ON companies.company_id = jobs.company_id;

-- RIGHT JOIN:
SELECT jobs.title, companies.name AS company_name
FROM jobs
RIGHT JOIN companies ON jobs.company_id = companies.company_id;

-- FULL JOIN:
SELECT companies.name AS company_name, jobs.title
FROM companies
FULL JOIN jobs ON companies.company_id = jobs.company_id;

-- CROSS JOIN:
SELECT companies.name AS company_name, jobs.title
FROM companies
CROSS JOIN jobs;
