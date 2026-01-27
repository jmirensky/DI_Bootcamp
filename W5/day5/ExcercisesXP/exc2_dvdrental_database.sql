 -- Exercise 2: DVD Rental

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
SELECT * FROM language;

SELECT * FROM film
 WHERE film_id IN (1, 2, 3, 10, 20, 30);
 
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

UPDATE film
SET language_id = 6
WHERE film_id IN (10, 20, 30);


-- Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- table > customer > constraints > address_id is a Foreign Key, it comes from address table (there it is PRIMARY KEY)
/*We cannot insert address_id values into the customer table without first verifying that they already exist in the address table.*/


-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE IF EXISTS customer_review;

/*Just in case, you need to check first:
-  if the table exists on the schema
-  if other tables depend from it as "child" tables. In this case, there is no dependency because does not have children, and we can delete it easily.*/


-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) as not_returned
FROM rental
WHERE return_date IS NULL;


-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
--inner join of 3 tables: rental, inventory, film
SELECT 
	f.title,
	f.replacement_cost
FROM rental r
INNER JOIN inventory i 
ON r.inventory_id = i.inventory_id
INNER JOIN film f 
ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;


/*Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
but he can’t remember their names.
Can you help him find which movies he wants to rent?*/

-- The 1st film: The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
--inner join of 3 tables: film, film_actor,actor
SELECT DISTINCT
	f.title,
	f.description
FROM film f
INNER JOIN film_actor fa
ON f.film_id = fa.film_id
INNER JOIN actor a
ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope'
AND a.last_name = 'Monroe'
AND f.description ILIKE '%sumo%';

-- The 2nd film: A short documentary (less than 1 hour long), rated “R”.
-- only with information of film table
SELECT DISTINCT
	f.title,
	f.description
FROM film f
WHERE f.length < 60
AND f.RATING = 'R'
AND f.description ILIKE '%documentary%';

-- The 3rd film: A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
--inner join of 5 tables: rental, customer, payment, inventory, film
--[with ChaGPT]
SELECT DISTINCT   
	f.title,
	f.description
FROM rental r
INNER JOIN customer c
ON r.customer_id = c.customer_id
INNER JOIN  payment p
ON r.rental_id = p.rental_id
INNER JOIN  inventory i
ON r.inventory_id = i.inventory_id
INNER JOIN  film f 
ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew'
  AND c.last_name = 'Mahan'
  AND p.amount > 4
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
--inner join of 5 tables: rental, customer, payment, inventory, film
--[with ChaGPT]
SELECT DISTINCT
	f.title,
	f.description,
	f.replacement_cost
FROM rental r
JOIN customer c
ON r.customer_id = c.customer_id
JOIN inventory i
ON r.inventory_id = i.inventory_id
JOIN film f 
ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew'
  AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;