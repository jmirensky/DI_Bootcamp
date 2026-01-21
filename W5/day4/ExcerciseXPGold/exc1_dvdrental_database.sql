-- Exercise XP Gold

--Exercise 1: DVD Rental

-- Find out how many films there are for each rating.
SELECT rating, COUNT(*) AS total_films
FROM film
GROUP BY rating
ORDER BY rating;

-- Get a list of all the movies that have a rating of G or PG-13.
SELECT title, rating
FROM film
WHERE rating in ('G', 'PG-13')
ORDER BY rating, film ;

/*Filter this list further: look for only movies that are under 2 hours long,
and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.*/
SELECT title
FROM film
WHERE rating in ('G', 'PG-13') AND length < 120 AND rental_rate < 3
ORDER BY film ;


-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
SELECT customer_id, first_name, last_name
FROM customer
LIMIT 5; 

UPDATE customer
SET first_name = 'Julieta',
    last_name = 'Mirensky',
    email = 'julieta@mail.com'
WHERE customer_id = 4
RETURNING first_name, last_name, email;


-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
/*comprobacion -->
SELECT * FROM customer
WHERE customer_id = 4;  ---> address_id = 8  */

UPDATE address
SET address = 'Rishonim 27',
	district = 'South',
	postal_code = '77452',
	phone = '050-1234567'
WHERE 
	address_id = 
(SELECT  address_id FROM  customer WHERE first_name = 'Julieta' AND last_name = 'Mirensky' AND email = 'julieta@mail.com');