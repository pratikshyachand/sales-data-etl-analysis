-- 1. Total Revenue by Product

SELECT 
p.Name,
sum(s.SalesAmount) as Revenue
FROM
sales s
LEFT JOIN products as p ON s.ProductID = p.ProductID
GROUP BY p.Name
ORDER BY Revenue desc;

-- 2. Total Revenue by Country

SELECT 
c.Country,
sum(s.SalesAmount) as Revenue
FROM
sales as s
LEFT JOIN customers as c ON s.CustomerID = c.CustomerID
GROUP BY c.Country
ORDER BY Revenue desc;

-- 3. Top 10 Customers by Revenue

SELECT
c.CustomerID,
CONCAT(c.FirstName,' ', c.LastName) as CustomerName,
sum(s.SalesAmount) as Revenue
FROM
sales as s
LEFT JOIN customers as c ON s.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY Revenue desc;

-- 4. Product performance by Country

SELECT 
c.Country,
p.Name,
sum(s.SalesAmount) as Revenue
FROM
sales as s
LEFT JOIN products as p ON s.ProductID = p.ProductID
LEFT JOIN customers as c ON s.CustomerID = c.CustomerID
GROUP BY c.Country, p.Name
ORDER BY c.Country asc, Revenue desc;

-- 5. Sales by Product Category

SELECT
DISTINCT p.Category,
sum(s.SalesAmount) as Revenue
FROM sales as s
LEFT JOIN products as p ON s.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Revenue desc;

-- 6. Monthly Revenue

SELECT
FORMAT(OrderDate, 'yyyy-MM') as YearMonth,
sum(SalesAmount) as Revenue
FROM sales
GROUP BY FORMAT(OrderDate, 'yyyy-MM')
ORDER BY YearMonth;

-- 7. Product, Sales, Quantity VS Revenue

SELECT
DISTINCT p.Name,
sum(s.Quantity) as TotalSalesQnty,
sum(s.SalesAmount) as Revenue
FROM
sales as s
LEFT JOIN products as p ON s.ProductID = p.ProductID
GROUP BY p.Name
ORDER BY Revenue desc;

