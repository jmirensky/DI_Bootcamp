--Exercise 1: DVD Rental

-- Get a list of all the languages, from the language table.
SELECT * FROM language;

--Get a list of all films joined with their languages – select the following details: film title, description, and .
SELECT
	f.title, 
	f.description, 
	l.name AS language
FROM film f
INNER JOIN language l
ON f.language_id = l.language_id;

-- Get all languages, even if there are no films in those languages
-- select the following details: film title, description, and language name.
SELECT
	f.title, 
	f.description, 
	l.name AS language
FROM film f
RIGHT JOIN language l
ON f.language_id = l.language_id;

--Create a new table called new_film with the following columns: id, name. Add some new films to the table.
CREATE TABLE new_film (
id serial PRIMARY KEY,
name VARCHAR(100) NOT NULL
);

INSERT INTO new_film (name)
VALUES ('Interstellar'), ('The Godfather'), ('The Matrix'), ('Relatos Salvajes');


/*Create a new table called customer_review, which will contain film reviews that customers will make.
Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
It should have the following columns:
review_id – a primary key, non null, auto-increment.
film_id – references the new_film table. The film that is being reviewed.
language_id – references the language table. What language the review is in.
title – the title of the review.
score – the rating of the review (1-10).
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated.*/
CREATE TABLE customer_review (
  review_id SERIAL PRIMARY KEY,
  film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
  language_id INTEGER REFERENCES language(language_id),
  title VARCHAR(100),
  score INTEGER CHECK (score BETWEEN 1 AND 10),
  review_text TEXT,
  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES 
(1, 1, 'Amazing movie', 9, 'Visually stunning and emotional'),
(2, 1, 'Classic', 10, 'A masterpiece of cinema');

SELECT * FROM new_film;
SELECT * FROM customer_review;

-- Delete a film that has a review from the new_film table. What happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;
The first review was automatically deleted when the movie it referenced was deleted
(due to the ON DELETE CASCADE restriction).