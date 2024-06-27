/* In SQL, procedures, functions, and cursors are essential components used to handle complex database operations. 
Here, we'll provide a detailed explanation and examples based on the hypothetical Apna app, a platform that might handle user registrations, job listings, and applications. 

1. Stored Procedures
A stored procedure is a group of SQL statements that can be executed as a unit. They help in encapsulating logic, reusing code, and improving performance by reducing network traffic.

Example: Procedure to Register a New User
Suppose we want to create a stored procedure to register a new user in the Apna app's users table.*/
CREATE PROCEDURE RegisterUser (
    IN p_username VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    INSERT INTO users (username, email, password, created_at)
    VALUES (p_username, p_email, p_password, NOW());
END;

/* 2. Functions
Functions in SQL are similar to procedures but differ in that they return a single value. Functions can be used in SQL queries just like built-in SQL functions.

Example: Function to Calculate the Number of Applications by a User
Let's create a function to return the count of job applications submitted by a user. */

CREATE FUNCTION GetApplicationCount (p_user_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE app_count INT;
    SELECT COUNT(*) INTO app_count
    FROM applications
    WHERE user_id = p_user_id;
    RETURN app_count;
END;

/* Cursors
Cursors are database objects used to retrieve, manipulate, and navigate through a result set row-by-row. They are useful for processing individual rows returned by a query.

Example: Cursor to List All Job Applications for a Specific Job
Assume we need to process each application for a specific job and perform some operations, such as sending notifications.*/

DELIMITER //

CREATE PROCEDURE ProcessJobApplications (IN p_job_id INT)
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE app_id INT;
    DECLARE user_id INT;
    DECLARE cur CURSOR FOR 
        SELECT application_id, user_id 
        FROM applications 
        WHERE job_id = p_job_id;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO app_id, user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        -- Example operation: Insert into notifications table
        INSERT INTO notifications (user_id, message, created_at)
        VALUES (user_id, CONCAT('Your application ', app_id, ' is being processed.'), NOW());
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;

