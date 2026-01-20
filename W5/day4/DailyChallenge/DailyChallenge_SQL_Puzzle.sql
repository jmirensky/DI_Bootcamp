CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);

SELECT * FROM SecondTab;


 /* - - - - - - - */

 
-- Q1. What will be the OUTPUT of the following statement?
SELECT 
	COUNT(*) 
FROM FirstTab AS ft
WHERE ft.id NOT IN 	
	( SELECT id FROM SecondTab WHERE id IS NULL )

-- Analysis:
-- 	SELECT 
-- 		COUNT(*)
-- 	FROM FirstTab AS ft
-- 	WHERE
-- 		ft.id NOT IN (NULL) => all comparisons with NULL produce UNKNOWN => ft.id UNKNOWN
		
-- Prediction: no record passes. Count = 0


-- Q2. What will be the OUTPUT of the following statement?
SELECT 
	COUNT(*) 
FROM FirstTab AS ft
WHERE
ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Analysis:
-- 	SELECT 
-- 		COUNT(*)
-- 	FROM FirstTab AS ft
-- 	WHERE
-- 		ft.id NOT IN (5) =  ft.id  (6, 7, NULL) => all comparisons with NULL produce UNKNOWN.

-- Prediction: 2 pass (6 and 7). Count = 2


-- Q3. What will be the OUTPUT of the following statement?
    SELECT
		COUNT(*) 
    FROM FirstTab AS ft 
	WHERE
		ft.id NOT IN ( SELECT id FROM SecondTab )

-- Analysis:  
-- 	SELECT 
-- 		COUNT(*)
-- 	FROM FirstTab AS ft
-- 	WHERE
-- 		ft.id NOT IN (5, NULL)  => ft.id NOT IN  5, ft.id NOT IN  NULL => all comparisons with NULL produce UNKNOWN.

-- Prediction: no record passes. Count = 0


-- Q4. What will be the OUTPUT of the following statement?
    SELECT
		COUNT(*) 
    FROM FirstTab AS ft 
	WHERE 
		ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- Analysis:
-- SELECT
-- 		COUNT(*) 
--     FROM FirstTab AS ft 
-- 	WHERE 
-- 		ft.id NOT IN 5  --> ft.id = 6, ft.id = 7, ft.id =NULL  => all comparisons with NULL produce UNKNOWN.
	
-- Prediction: 2 pass (6 and 7). Count = 2