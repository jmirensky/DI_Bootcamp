-- Exercise XP Gold
-- Exercise 2: students table

/*Update
1 - ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
2 - Change the last_name of David from ‘Grez’ to ‘Guez’.*/
UPDATE students
SET birth_date = '1998-11-02'
WHERE last_name = 'Benichou'
  AND first_name IN ('Lea', 'Marc');

UPDATE students
SET last_name = 'Guez'
WHERE last_name = 'Grez'; 

-- 3 - Delete: Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students
WHERE first_name = 'Lea'
  AND last_name = 'Benichou';


-- 4 Count: Count how many students are in the table.
SELECT COUNT(*) FROM students;


-- 5 Count how many students were born after 1/01/2000.
SELECT COUNT(*) AS total_students FROM students
WHERE birth_date > '2000-01-01' ;


-- 6 - Insert / Alter
/*Add a column to the student table called math_grade.
Add 80 to the student which id is 1.
Add 90 to the students which have ids of 2 or 4.
Add 40 to the student which id is 6.*/

ALTER TABLE students
ADD COLUMN math_grade INT;

UPDATE students
SET math_grade = 80
WHERE id = 1;

UPDATE students
SET math_grade = 90
WHERE id IN (2,4);

UPDATE students
SET math_grade = 40
WHERE id = 6;


-- Count how many students have a grade bigger than 83
SELECT COUNT(*) AS total_students FROM students
WHERE math_grade > 83 ;


-- Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT first_name, last_name, birth_date, 70
FROM students
WHERE first_name = 'Omer'
  AND last_name = 'Simpson'
LIMIT 1;
-- Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.
SELECT id,
first_name,
last_name,
birth_date,
math_grade
FROM students
WHERE first_name = 'Omer'; -- hay2


/* Bonus: Count how many grades each student has.
	* Tip: You should display the first_name, last_name and the number of grades of each student. 
	If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2. [HAY 2 NULL]
	* Tip : Use an alias called total_grade to fetch the grades.
	* Hint: Use GROUP BY.*/
SELECT first_name,
       last_name,
       COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

-- SUM: Find the sum of all the students grades.
SELECT SUM(math_grade) AS sum_of_grades
FROM students;