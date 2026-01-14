CREATE TABLE customers(
 customerID varchar(15) primary key,
 gender varchar(7),
 age int 
)

CREATE TABLE products(
 product_category varchar(20) primary key,
)

CREATE TABLE sales(
 transactionID int primary key not null,
 salesDate date,
 price_per_unit decimal,
 customerID varchar(15) foreign key,
 product_category varchar(20) foreign key,
 quantity int,
 total_amount decimal

)