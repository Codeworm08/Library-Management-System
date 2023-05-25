CREATE database LIBRARY;
use LIBRARY;
create table members
(
memberid varchar(20) not null primary key,
street varchar(100),
city varchar(30),
state varchar(40),
pin_code char(6),
address varchar(300) as (concat_ws(' ',street,city,state,pin_code)),
first_name varchar(100),
last_name varchar(100),
name varchar(200) as (concat_ws(' ',first_name,last_name))
);
create table staff
(
staffid varchar(20) not null primary key,
first_name varchar(100),
last_name varchar(100),
name varchar(200) as (concat_ws(' ',first_name,last_name)),
street varchar(100),
city varchar(30),
state varchar(40),
pin_code char(6),
address varchar(300) as (concat_ws(' ',street,city,state,pin_code)),
date_of_join date,
date_of_birth date
);
create table author
(
authorid varchar(20) not null primary key,
first_name varchar(100),
last_name varchar(100),
name varchar(200) as (concat_ws(' ',first_name,last_name))
);
