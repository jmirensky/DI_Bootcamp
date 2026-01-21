-- Exercise XP Gold
-- Exercise 3: Items and customers

borrar xq no salio bien

DROP TABLE IF EXISTS purchases;

-- Create a table named purchases.
CREATE TABLE purchases (
id SERIAL PRIMARY KEY,
customer_id INT  REFERENCES customers(id),
item_id INT  REFERENCES items(id),
quantity_purchased INT NOT NULL
);

-- Insert purchases for the customers, use subqueries

--Scott Scott → 1 fan
INSERT INTO purchases (customer_id, item_id, quantity_purchased )
VALUES (
	(SELECT  id FROM customers WHERE first_name = 'Scott' and last_name ='Scott'),
	(SELECT id FROM items WHERE name = 'Fan'),
	1
);

--Melanie Johnson → 10 large desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased )
VALUES (
	(SELECT id FROM customers WHERE first_name = 'Melanie' and last_name ='Johnson'),
	(SELECT id FROM items WHERE name = 'Large desk'),
	10
);

--Greg Jones → 2 small desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased )
VALUES (
	(SELECT id FROM customers WHERE first_name = 'Greg' and last_name ='Jones'),
	(SELECT id FROM items WHERE name = 'Small Desk'),
	2
);

-- All purchases. Is this information useful to us? => No, as a business we need to make joins, to understand who bought what.
SELECT * from purchases;

-- All purchases, joining with the customers table.
SELECT
	p.id, 
	c.first_name,
	c.last_name,
	p.item_id,
	i.name,
	p.quantity_purchased
FROM purchases p
INNER JOIN customers c
ON p.customer_id = c.id
INNER JOIN items i
ON p.item_id = i.id;

--Purchases of the customer with the ID equal to 5.
SELECT
   c.id,
   c.first_name,
    c.last_name,
	i.id,
	i.name,
    p.quantity_purchased
FROM purchases p
JOIN customers c 
ON p.customer_id = c.id
INNER JOIN items i
ON p.item_id = i.id
WHERE c.id = 5;

--Purchases for a large desk AND a small desk
SELECT
   c.id,
   c.first_name,
    c.last_name,
	i.id,
	i.name,
    p.quantity_purchased
FROM purchases p
JOIN customers c 
ON p.customer_id = c.id
INNER JOIN items i
ON p.item_id = i.id
WHERE i.name IN('Large desk','Small Desk');


-- Use SQL to show all the customers who have made a purchase.
SELECT
    c.first_name,
    c.last_name,
    i.name AS item_name
FROM purchases p
INNER JOIN customers c
ON p.customer_id = c.id
INNER JOIN items i ON p.item_id = i.id;

--Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
INSERT INTO purchases (customer_id, item_id, quantity_purchased )
VALUES (1, NULL, 3)

/* Yes, it works because foreign keys allow NULL, which means "no value" (not "invalid value").
What is NOT allowed is NOT NULL.*/