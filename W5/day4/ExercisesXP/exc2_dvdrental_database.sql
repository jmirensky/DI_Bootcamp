--Exercise 2: dvdrental database

-- 1 Select all the columns from the “customer” table.
SELECT *
FROM customer;

-- 2 Display the names (first_name, last_name) using an alias named “full_name”.
SELECT
	first_name || ' ' || last_name AS full_name
FROM customer;

-- 3 Get all the dates that accounts were created. Select all the create_date from the “customer” table (no duplicates).
SELECT DISTINCT create_date 
FROM customer;

-- 4 Customer details from the customer table,displayed in descending order by their first name.
SELECT * 
FROM customer
ORDER BY first_name DESC;

--5 Get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT 
	film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- 6 Get the address and phone number of all customers living in the Texas district (“address” table).
SELECT 
	address, phone
FROM address
WHERE district = 'Texas';

--7 Retrieve all movie details where the movie id is either 15 or 150.
SELECT * FROM film
WHERE film_id in (15, 150)

-- 8  Check if your favorite movie exists in the database; get the film ID, title, description, length and the rental rate (“film” table)
SELECT 
	film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Titanic';

/* 9 No luck finding your movie? Write a query to get the film ID, title, description, length and the rental rate of all 
	the movies starting with the two first letters of your favorite movie.*/
SELECT 
	film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'ti%';

-- 10 Write a query that will find the 10 cheapest movies.
SELECT
	film_id,
     title,
     rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

-- 11 Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
SELECT
	film_id,
     title,
     rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10 OFFSET 10;

--Bonus: Not using LIMIT. [CHATGPT])
SELECT *
FROM (
    SELECT
        film_id,
        title,
        rental_rate,
        ROW_NUMBER() OVER (ORDER BY rental_rate) AS rn
    FROM film
) t
WHERE rn BETWEEN 11 AND 20;

/* 12 Join the data in the customer table and the payment table.
   You want to get the first name and last name from the customer table, 
   as well as the amount and the date of every payment made by a customer, ordered by their id.*/
SELECT 
	c.first_name,
	c.last_name,
	p.amount, 
	p.payment_date
FROM customer as c
INNER JOIN payment as p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id;


-- 13 You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT
	f.film_id,
	f.title,
	i.inventory_id
FROM FILM AS f
LEFT JOIN inventory as i
ON f.film_id = i.film_id
WHERE i.inventory_id IS  NUlL;

-- 14 Write a query to find which city is in which country.
SELECT 
	ci.city,
	co.country
FROM city as cI
INNER JOIN country as co
ON ci.country_id = co.country_id
ORDER BY co.country, ci.city;



/*  Bonus You want to be able to see how your sellers have been doing? 
	Write a query to get the customer’s id, names (first and last), the amount and the 
	date of payment ordered by the id of the staff member who sold them the dvd.*/
SELECT
    p.staff_id,
	c.customer_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM payment as p
INNER JOIN customer AS c
    ON p.customer_id = c.customer_id
ORDER BY p.staff_id, c.customer_id;