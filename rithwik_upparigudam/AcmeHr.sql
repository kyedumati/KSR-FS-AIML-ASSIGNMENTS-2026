create table EmployeeDetails
(Emp_id int,Name varchar(50),Gender varchar(10),
Dob date,ContactInfo int,
Address varchar(50),EmergencyContact int
,EmployeementDetails varchar(50),
ReportingManager varchar(50),
Deparment varchar(30),Designation varchar(50)
);


insert into EmployeeDetails values
(1,"AnanyaRoa","Female",900001111,"KarthikMenon",
"Engineering","SeniorSoftWareEnginner");



create table EmployeesDirectory(Emp_id int,
Name varchar(50),Department varchar(50),Designation varchar(50));


insert into EmployeesDirectory values(
1,"AnanyaRoa","Engineering","SeniorSoftWareEngineer"),
(2,"Karthik Menon","Engineering","EngineeringManager"),
(3,"Meera Lyer","Fiance","Accountant"),
(4,"Rahul Sharma","HumanResources","Hr Executive"),
(5,"Fatima Khan","Product","Product Disigner"),
(6,"Arjun Reddy","Engineering","QA Engineering");


create table HR_Dashboard (date int ,
HeadCount int,OnLeaveToday int,LateArrivalsToday int,
OpenLeaveRequests int);


insert into HR_Dashboard values(
"2026-10-26",248,12,5,7
)



create table DailyAttendance (
EmployeeName varchar(50),datee date,
check_in varchar(10),check_out varchar(10),
hours decimal(10,2),status varchar(20)
);


insert into DailyAttendance values
("AnanyaRoa","2026-10-26","09:02","18:10",9.1,"ON-TIME"),
("KarthikMenon","2026-10-26","09:41","18:30",8.8,"LATE"),
("ArjunReddy","2026-10-26","8:55","17:20",8.4,"ON-TIME"),
("FatimaKhan","2026-10-26","-","-",0.0,"ON-LEAVE"),
("PriyaNair","2026-10-26","10:05","19:00",8.9,"Late");
