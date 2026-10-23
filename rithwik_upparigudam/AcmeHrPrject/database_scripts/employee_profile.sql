-- Employee profile tables DDL script

create table employee(
   emp_id varchar2(20) primary key,
   name varchar(40) not null,
   designation varchar(50) not null,
   email varchar(50) unique
)

create table dept(
  dept_id varchar(20),
)
