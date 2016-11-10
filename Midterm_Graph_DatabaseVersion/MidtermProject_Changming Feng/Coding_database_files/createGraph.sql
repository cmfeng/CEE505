.open Graph.db
drop table if exists Cities;
drop table if exists Airports;
drop table if exists Airlines;
drop table if exists Flights;


create table Cities(
	ID		int not null primary key,	
	name		char(20),
	state		char(5)
);

create table Airports(
	name		char(3) not null primary key,
	cityID	int,
	Long		double,
	Lati		double,
	X		double,
	Y		double
);

create table Airlines(
	ID		int not null primary key,	
	name		char(20)
);

create table Flights(
	ID		int not null primary key,	
	Number	char(10),
	OperatorID	int,
	FromAir	char(3),
	ToAir 	char(3), 
	DepartTime	int,
	ArrivalTime	int,
	TravelTime	int
);	
