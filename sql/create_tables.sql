CREATE TABLE customers(
 CustomerID varchar(15) primary key,
 FirstName varchar(20),
 LastName varchar(20),
 Country varchar(100)
);

CREATE TABLE products(
  ProductID varchar(15) primary key,
  Name varchar(100),
  Category varchar(100),
  Price decimal
);

CREATE TABLE sales( 
 OrderID varchar(15) primary key,
 CustomerID varchar(15),
 ProductID varchar(15),
 OrderDate date,
 Quantity int,
 UnitPrice decimal(10,2),
 SalesAmount decimal(10,2),
 foreign key (CustomerID) references customers(CustomerID),
 foreign key (ProductID) references products(ProductID)

);