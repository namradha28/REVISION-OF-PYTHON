/* TCL commands are used to manage transactions in the database. 
A transaction is a sequence of one or more SQL operations that are executed as a single unit of work. 
The main TCL commands are COMMIT, ROLLBACK, and SAVEPOINT. */

/* COMMIT
The COMMIT command is used to save all changes made during the current transaction.
Once a transaction is committed, the changes are permanent and visible to other users. */
BEGIN TRANSACTION;
UPDATE employees SET salary = salary * 1.10 WHERE department = 'Sales';
COMMIT;

/* ROLLBACK

The ROLLBACK command is used to undo changes made during the current transaction. 
It can revert the database to the state it was in before the transaction began. */
BEGIN TRANSACTION;
UPDATE employees SET salary = salary * 1.10 WHERE department = 'Sales';
ROLLBACK;

/* SAVEPOINT

The SAVEPOINT command sets a point within a transaction to which you can later roll back. 
This allows partial rollbacks within a transaction. */
BEGIN TRANSACTION;
UPDATE employees SET salary = salary * 1.10 WHERE department = 'Sales';
SAVEPOINT before_bonus_update;
UPDATE employees SET bonus = bonus * 1.15 WHERE department = 'Sales';
ROLLBACK TO SAVEPOINT before_bonus_update;
COMMIT;

/* Triggers
A trigger is a stored procedure in a database that automatically invokes whenever a specified event occurs. Triggers are used to maintain the integrity of the information on the database.
Creating a Trigger:
Triggers can be created to run before or after an INSERT, UPDATE, or DELETE operation on a table. */

CREATE TRIGGER employee_salary_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < OLD.salary THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Salary cannot be decreased!';
    END IF;
END;

--  Trigger Example
CREATE TRIGGER log_employee_changes
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (employee_id, old_salary, new_salary, change_date)
    VALUES (OLD.employee_id, OLD.salary, NEW.salary, NOW());
END;

/* Views
A view is a virtual table based on the result set of an SQL query. It can contain all rows of a table or select rows from a table. Views are used to simplify complex queries, enhance security, and provide a layer of abstraction.

Creating a View

The CREATE VIEW command is used to create a view.*/

CREATE VIEW employee_view AS
SELECT employee_id, first_name, last_name, department, salary
FROM employees
WHERE department = 'Sales';

/* Using a View
Once created, a view can be queried like a regular table */
SELECT * FROM employee_view;

/*Updating a View
Some views are updatable, which means you can use them to insert, update, and delete rows in the underlying table.*/
UPDATE employee_view
SET salary = salary * 1.10
WHERE employee_id = 101;

/* Dropping a View
To delete a view, use the DROP VIEW command.*/
DROP VIEW employee_view;


