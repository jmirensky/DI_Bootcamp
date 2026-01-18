select * from actor;
select count(*) from actor; --7

insert into actor (first_name, last_name, age, number_oscars) values
('Julia', 'Roberts', '1967-10-28', 1);
--no puedo dejar informacion incompleta, constrain not null en las 4
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
