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
create table books
(
ISBN char(10) not null primary key,
title varchar(30)
);

create table book_instance
(
acc_no varchar(20) not null primary key,
is_issued varchar(40),
issued_by varchar(40),
status varchar(80) as (concat_ws(' ',is_issued,issued_by))
);
