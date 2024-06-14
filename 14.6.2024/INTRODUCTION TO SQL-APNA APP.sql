/*SQL (Structured Query Language) is the standard language used to manage and manipulate relational databases.
 Below are the basic SQL commands with syntax and examples tailored to a hypothetical job portal app, Apna.*/
 -- CREATING TABLES 
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

CREATE TABLE applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    job_id INT,
    candidate_name VARCHAR(100) NOT NULL,
    application_date DATE,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

-- INSERTING VALUES INTO THE TABLE:
-- Insert data into the companies table
INSERT INTO companies (name, location) 
VALUES ('Apna Inc.', 'Bangalore'), ('Tech Solutions', 'Mumbai');

-- Insert data into the jobs table
INSERT INTO jobs (title, company_id, salary, date_posted)
VALUES ('Software Engineer', 1, 60000.00, '2024-06-01'),
       ('Data Analyst', 2, 55000.00, '2024-06-05');

-- Insert data into the applications table
INSERT INTO applications (job_id, candidate_name, application_date)
VALUES (1, 'Alice Smith', '2024-06-02'),
       (2, 'Bob Johnson', '2024-06-06');
       
-- QUERYING DATA INTO THE DATABASES:
-- Select all companies
SELECT * FROM companies;

-- Select all jobs with their respective company names
SELECT j.job_id, j.title, j.salary, c.name AS company_name
FROM jobs j
JOIN companies c ON j.company_id = c.company_id;

-- Select all applications for a specific job
SELECT a.candidate_name, a.application_date, j.title
FROM applications a
JOIN jobs j ON a.job_id = j.job_id
WHERE j.title = 'Software Engineer';

-- UPDATING DATA INTO THE TABLE:
-- Update the salary of a specific job
UPDATE jobs
SET salary = 65000.00
WHERE title = 'Software Engineer';

-- Update the location of a specific company
UPDATE companies
SET location = 'Hyderabad'
WHERE name = 'Tech Solutions';

-- DELETING RECORDS IN A TABLE:
-- Delete a specific application
DELETE FROM applications
WHERE candidate_name = 'Bob Johnson';

-- Delete a specific job
DELETE FROM jobs
WHERE title = 'Data Analyst';

-- DROPPING TABLE:(DELETES THE ENTIRE DATABASE)
DROP TABLE applications;

-- ALTERING TABLES IN A DATABASE:
-- Add a new column to the companies table
ALTER TABLE companies ADD email VARCHAR(100);

-- Drop a column from the jobs table
ALTER TABLE jobs DROP COLUMN date_posted;

-- Modify the data type of a column in the applications table
ALTER TABLE applications MODIFY candidate_name VARCHAR(150);

