 --Exercise 1: Students table
 
create table students (
id serial primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
birth_date date not null);

insert into students (first_name, last_name, birth_date) values
		('Marc', 'Benichou', '1998-11-02'),
		('Yoan', 'Cohen', '2010-12-03'),
		('Lea', 'Benichou', '1987-07-27'),
		('Amelia',  'Dux', '1996-04-07'),
		('David', 'Grez', '2003-06-14'),
		('Omer', 'Simpson', '1980-10-03');

insert into students (first_name, last_name, birth_date) values
					('Julieta', 'Mirensky', '1984-10-24');

select * from students;

select first_name, last_name from students;

select first_name, last_name from students
where id = 2;

select first_name, last_name from students
where last_name = 'Benichou' AND first_name = 'Marc';

select first_name, last_name from students
where last_name = 'Benichou' OR first_name = 'Marc';

select first_name, last_name from students
where first_name ilike '%a%';  -- first_names contain the letter a.

select first_name, last_name from students
where first_name ilike 'a%';  --first_names start with the letter a.

select first_name, last_name from students
where first_name ilike '%a'; -- first_names end with the letter a.

SELECT first_name, last_name FROM students
where first_name ilike '_%a%'; --second to last letter of their first_names are

select first_name, last_name from students
where id = 2 and id = 3  --id’s are equal to 1 AND 3  => THIS DOES NOT EXIST

select * from students
where birth_date >= '2000-01-01';   -- birth_dates are equal to or come after 1/01/2000.