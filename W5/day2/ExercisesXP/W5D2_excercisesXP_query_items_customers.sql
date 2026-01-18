--Exercise 1: Items and customers

CREATE TABLE items(
id serial primary key,
name varchar(50) not null,
price int not null
);

create table customers (
id serial primary key,
first_name varchar(100) not null,
last_name varchar(100) not null
);

insert into items (name, price) values
				('Small Desk', 100),
				('Large desk', 300),
				('Fan', 80);

insert into customers(first_name, last_name) values
				 ('Greg', 'Jones'),
				 ('Sandra', 'Jones'),
				 ('Scott', 'Scott'),
				 ('Trevor', 'Green'),
				 ('Melanie', 'Johnson');

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where last_name = 'Smith';
select * from customers where last_name = 'Jones';
select * from customers where first_name != 'Scott';