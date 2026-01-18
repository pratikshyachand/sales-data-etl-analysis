CREATE TABLE customers(
 CustomerID int primary key,
 FirstName varchar(20),
 LastName varchar(20),
 Country varchar(100)
);

CREATE TABLE products(
  ProductID int primary key,
  Name varchar(100),
  Category varchar(100),
  Price decimal(10,2)
);

CREATE TABLE sales( 
 OrderID int primary key,
 CustomerID int,
 ProductID int,
 OrderDate date,
 Quantity int,
 UnitPrice decimal(10,2),
 SalesAmount decimal(10,2),
 foreign key (CustomerID) references customers(CustomerID),
 foreign key (ProductID) references products(ProductID)
);