-- Exercises XP Ninja
-- Bonus Public Database

--Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name, last_name FROM customers
ORDER BY last_name, first_name
LIMIT 2 OFFSET
    		(SELECT COUNT(*) - 2 FROM customers)
;

-- delete all purchases made by Scott.
DELETE FROM purchases
WHERE customer_id =
	(SELECT id FROM customers WHERE first_name = 'Scott' and last_name = 'Scott');
	
-- Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
SELECT * FROM CUSTOMERS;
-- Yes. Scott is still in the customer table because I deleted him from purchases, not from customers.

/*find all purchases. Join purchases with the customers table, so that Scott’s order will appear,
although instead of the customer’s first and last name, you should only see empty/blank. 
(Which kind of join should you use?).*/

-- I delete all purchases made by Scott. So, Scott’s order will appear!
--With a Right Join I can see all the purchases. If some customers did not make any purchase, item_id & quentity_purchase will be NULL
SELECT
    p.item_id,
    p.quantity_purchased,
	c.first_name,
    c.last_name
FROM purchases p 
RIGHT JOIN customers c 
    ON p.customer_id = c.id;


/*find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear.
(Which kind of join should you use?)*/

-- I delete all purchases made by Scott. So, Scott’s order will appear!
-- With an Inner Join I can see all the purchases made ONLY by customers who really exist in my customer table.

SELECT
    p.item_id,
    p.quantity_purchased,
	c.first_name,
    c.last_name
FROM purchases p 
INNER JOIN customers c 
    ON p.customer_id = c.id;