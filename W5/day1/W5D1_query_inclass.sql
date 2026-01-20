--En PostgreSQL / pgAdmin no existe el comando SHOW DATABASES como en MySQL.
-- usar esto
-- SELECT datname FROM pg_database;  


-- Se aconseja ir comentando las queries a medida que vamos avanzando...

--compruebo que tengo la Database Hollywood

--sobre la Database Hollywood seleccionada --> click derecho Query Tool se abre el .sql

-- crear tabla actores
-- CREATE TABLE ACTORS (
-- 	ACTOR_ID SERIAL PRIMARY KEY,
-- 	FIRST_NAME VARCHAR(50) NOT NULL,
-- 	LAST_NAME VARCHAR(100) NOT NULL,
-- 	AGE DATE NOT NULL,
-- 	NUMBER_OSCARS SMALLINT NOT NULL
-- );

 --SELECT * FROM actors

-- -- insertar data en los registros de a 1:

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 1);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Gal','Gadot','30/04/1985',0);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Meryl','Streep','22/06/1949',3);

-- --agrego varios en 1 solo comando
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Leo','DiCaprio','11/11/1974',1),
--       ('Denzel', 'Washington', '28/12/1954', 2),
--       ('Bruce', 'Willis', '19/03/1955',0),
-- 	  ('Katharine', 'Hepburn', '12/05/1907',4);

-- select con operadores lógicos, and, or
-- SELECT * FROM actors;
-- SELECT * FROM actors WHERE first_name = 'Matt';
-- SELECT * FROM actors WHERE number_oscars >= 3;
-- SELECT last_name FROM actors WHERE first_name != 'Matt' ;
-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  AND 
-- last_name = 'Damon' ;
-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  AND 
-- last_name = 'Clooney' ;   --no existe
-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  OR 
-- last_name = 'Clooney' ;
-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  OR  
-- number_oscars = 2 ;

--is null - is not null
-- SELECT * FROM actors WHERE  last_name IS NULL;  --no existe
-- SELECT * FROM actors WHERE  last_name IS NOT NULL;

--ILIKE no se afecta x mayúsculas, LIKE sí--
-- SELECT * FROM actors WHERE last_name LIKE '%mon%'; --que contengan mon en su apellido
-- SELECT * FROM actors WHERE last_name LIKE '%y';  --last_names que TERMINAN con "y
-- SELECT * FROM actors WHERE last_name LIKE 'da%'; -- last_names que EMPIEZAN por "da"  no hay
-- SELECT * FROM actors WHERE last_name ILIKE 'da%'; -- last_name que EMPIEZAN por "da", ILIKE insensible a mayus-minus


-- SELECT * FROM actors LIMIT 1;  --recuperar al primer actor
-- SELECT * FROM actors WHERE age > '1960-01-01' LIMIT 1;
-- SELECT * FROM actors WHERE age > '1960-01-01' LIMIT 3 OFFSET 2; --saltar a los dos primeros actores y mostrar a los siguientes tres.

-- SELECT * FROM actors ORDER BY first_name ASC --orden alfabetico ascendente segun first_name

-- -- EJERCICIO
-- -- Los primeros 4 actores
-- SELECT * FROM actors LIMIT 4;

-- -- Los primeros 4 actores ordenados en orden descendente del last_name 
-- SELECT * FROM actors 
-- ORDER BY last_name DESC
-- LIMIT 4;

-- -- Los actores que tienen la letra 'e' en su first_name
-- SELECT * FROM actors WHERE first_name ILIKE '%e%';

-- -- Los actores que obtuvieron al menos 3 Óscar
-- SELECT * FROM actors WHERE number_oscars >=3;

-- --update, con cláusula de retorno
-- UPDATE actors 
-- SET age='1970-01-01' 
-- WHERE first_name='Matt' AND last_name='Damon'
-- RETURNING 
--     actor_id,
--     first_name, 
--     last_name,
--     age;

-- -- EJERCICIO
-- -- Actualizar el nombre de pila de Matt Damon a Maty
-- UPDATE actors 
-- SET first_name='Maty' 
-- WHERE first_name='Matt' AND last_name='Damon';

-- -- Actualiza el número de Oscar de George Clooney a 4 y devuelve el registro actualizado
-- UPDATE actors 
-- SET number_oscars=4 
-- WHERE first_name='George' AND last_name='Clooney'
-- RETURNING 
--     actor_id,
--     first_name, 
--     last_name,
--     age;

-- -- Renombra la columna age por birthdate
-- ALTER TABLE actors RENAME COLUMN age TO birthdate;

-- --delete registro, con cláusula de retorno
-- -- Elimina un actor y devuélvelo
-- DELETE FROM actors WHERE actor_id=3
-- RETURNING actor_id, first_name, last_name, number_oscars;  --Gal Gadot

 -- SELECT * FROM actors
 -- order by actor_id asc;
