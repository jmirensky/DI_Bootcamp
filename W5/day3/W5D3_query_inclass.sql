--ALIAS y concatenacion
-- SELECT   first_name || ' ' || last_name AS full_name  FROM actors;
-- SELECT   CONCAT(first_name, ' ', last_name) AS full_name FROM actors;
-- SELECT first_name AS name_actor, birthdate AS birth_date FROM actors;


--Funciones de agregación

-- -- Consigue el número de first_name
-- SELECT count(first_name) AS name_actor FROM actors;

-- --Consigue el número de actores
-- SELECT count(*) FROM actors;

-- --Consigue el máximo número de Óscar
-- SELECT MAX(number_oscars) as best_actor FROM actors;

-- --Consigue el número mínimo de Óscar
-- SELECT MIN(number_oscars) as worst_actor FROM actors;

-- SELECT first_name, last_name, number_oscars
-- FROM actors 
-- where
-- number_oscars = (SELECT MIN(number_oscars) FROM actors); --los actores que tienen el minimo
		 
-- --Consigue la suma de los Óscar
-- SELECT SUM(number_oscars) as total_Oscars FROM actors;

--corrijo el nombre de Matt Damon
-- UPDATE actors
-- set first_name = 'Matt'  
-- where actor_id = 1;

-- -- agrego otro Matt
-- INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
-- VALUES('Matt','Ross','03/01/1970', 0);

-- -- cláusula DISTINCT
-- SELECT DISTINCT first_name FROM actors ORDER BY first_name;--no repite Matt

-- SELECT * FROM actors WHERE first_name in ('Matt','Leo','Davis', 'George');
-- SELECT * FROM actors WHERE first_name not in ('Matt','Leo','Davis', 'George');

-- SELECT * FROM actors WHERE birthdate between '1961-01-01' and '1980-01-01';  --rangos


--  excercises:

-- -- Obtén el número medio de Oscars en la tabla
-- SELECT ROUND(AVG(number_oscars), 2) AS average_number_oscars FROM actors;

-- -- Consigue actores distintos según el número de Oscar que tengan = cuántos Oscar tiene cada actor
-- SELECT first_name, last_name, sum(number_oscars) FROM actors
-- GROUP BY first_name, last_name
-- ORDER BY sum(number_oscars) desc;

-- -- Consigue a los actores nacidos después del 01/01/1970
-- SELECT * FROM actors WHERE birthdate >  '01/01/1970'

-- -- los actores cuyos nombres sean , o David Morgan Will
-- SELECT * FROM actors WHERE first_name not in ('David', 'Morgan', 'Will');



--se crea una nueva tabla cars y colores, luego hacemos un inner join con una condición having

-- CREATE TABLE cars (
-- car_id serial PRIMARY KEY,
-- car_color INTEGER,
-- car_name text
-- );
-- INSERT INTO cars (car_color, car_name ) VALUES
-- 					(1, 'Mazda'),
-- 					(5, 'BMW'),
-- 					(8, 'Renault'),
-- 					(5, 'BMW'),
-- 					(8, 'Bugatti');


-- CREATE TABLE colors (
-- color_id INTEGER PRIMARY KEY,
-- namer VARCHAR(50)
-- );
-- INSERT INTO colors (color_id, namer ) VALUES
-- 					(1, 'blue'),
-- 					(5, 'yellow'),
-- 					(8, 'black');

-- SELECT cars.car_name, co.namer, COUNT(car_color) as color 
-- FROM cars 
-- INNER JOIN colors as co
-- ON cars.car_color = co.color_id
-- GROUP BY cars.car_name,co.namer;

-- -- having: solicitemos lo mismo, excepto los coches negros
-- SELECT cars.car_name, co.namer, COUNT(car_color) as color 
-- FROM cars 
-- INNER JOIN colors as co
-- ON cars.car_color = co.color_id
-- GROUP BY cars.car_name,co.namer
-- HAVING co.namer != 'black';

-- --UNION: Combina resultados de dos o más sentencias SELECT en un solo conjunto de resultados. 
-- -- Las dos tablas debes tener el mismo número de columnas
-- SELECT
--     car_name
-- FROM
--     cars
-- UNION
-- SELECT
--     nameR
-- FROM
--     colors
-- ORDER BY 
--  car_name ASC;

-- SELECT 
--     car_name,
--     car_id
-- FROM
--     cars
-- UNION
-- SELECT 
--     namer,
--     color_id
-- FROM
--     colors
-- ORDER BY car_name ASC;





--FOREIGN KEY constraint
-- Vamos a crear una tabla de películas (tabla hija respecto a la tabla actores -principal-) y una tabla de productores
--Supongamos por ahora que:
--    Un actor solo puede actuar en una película
--    Una película solo puede contar con un actor

-- CREATE TABLE movies(
-- movie_id SERIAL,  --PK
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,  --FK
-- PRIMARY KEY (movie_id),    --PK
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)  
-- );

-- --trae la fk con una subquery
-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));


-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--      ( 'The Devil Wears Prada', 
--     'The film follows Andrea Sachs, an aspiring journalist who lands a challenging job as an assistant to the demanding editor-in-chief of a high-fashion magazine, leading her to confront her values and ambitions',
--      (SELECT actor_id from actors WHERE first_name='Meryl' AND last_name='Streep')),
--     ( 'Parasite', 
--      'The film follows a poor family who infiltrate the home and life of a wealthy family in Seul.', 
--      (SELECT actor_id from actors WHERE first_name='Song' AND last_name='Kang-ho,'));


-- -- 2 peliculas de Matt Damon + 1 de Meryl Streep
-- --valor coincidente tanto en la tabla actors como en movies
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;


-- --Crear una tabla de productores, con foreing key = id_película ( tabla productores está vinculada a tabla de movies)
-- CREATE TABLE producers(
-- prod_id SERIAL,  --PK
-- prod_name VARCHAR (50) NOT NULL,
-- prod_last VARCHAR (50) NOT NULL,
-- movie_id int,   --FK
-- PRIMARY KEY (prod_id),    --PK
-- FOREIGN KEY (movie_id) REFERENCES movies(movie_id)  --FK
-- );

-- -- Inserta 3 registros, trae la fk CON UN SELECT
-- INSERT INTO producers (prod_name, prod_last, movie_id) values 
--                         ('Jerry', 'Weintraub', (SELECT movie_id from movies WHERE movie_title='Oceans Eleven')); 

-- INSERT INTO producers (prod_name, prod_last, movie_id) values 
--                         ('Lawrence', 'Bender', (SELECT movie_id from movies WHERE movie_title='Good Will Hunting'));

-- INSERT INTO producers (prod_name, prod_last, movie_id) values 
 --                       ('Wendy', 'Finerman', (SELECT movie_id from movies WHERE movie_title='The Devil Wears Prada'));

-- --Inner Join
-- SELECT producers.prod_name, producers.prod_last, movies.movie_title
-- FROM producers
-- INNER JOIN movies
-- ON producers.movie_id = movies.movie_id;


-- -- Left Join
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT OUTER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;


-- -- Right Join  (justo las 2 peliculas son de Matt Damon). Queda igual al inner joing
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- RIGHT OUTER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;

-- -- Full Join o FULL OUTER JOIN
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- FULL OUTER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;


--Ejercicio
--podemos hacer joins aunque las tablas no esten relacionadas

/* Crea una tabla llamada países, con dos campos: country_id y coutry_name. No tiene foreing key.
Es una tabla para probar las uniones de PostgreSQL.

Utiliza INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN y FULL OUTER JOIN para unir los países de la tabla con los actores de la tabla, 
dependiendo de la comparación de su clave primaria
Mira los resultados y analízalos para entender la diferencia entre los tipos de Joins. 
  */


-- CREATE TABLE COUNTRY (
-- country_id serial primary key,
-- country_name varchar(34) not null
-- );

-- INSERT INTO country (country_name) VALUES
--                    ('Mexico'),
--                    ('Portugal'),
--                    ('Japan'),
--                    ('Lituania');

-- select actors.actor_id, actors.first_name, actors.last_name, country.country_id, country.country_name
-- from actors
-- inner join country
-- on actors.actor_id = country.country_id;

-- select actors.actor_id, actors.first_name, actors.last_name, country.country_id, country.country_name
-- from actors
-- full join country
-- on actors.actor_id = country.country_id;

-- select actors.actor_id, actors.first_name, actors.last_name, country.country_id, country.country_name
-- from actors
-- left join country
-- on actors.actor_id = country.country_id;

-- select actors.actor_id, actors.first_name, actors.last_name, country.country_id, country.country_name
-- from actors
-- right join country
-- on actors.actor_id = country.country_id;