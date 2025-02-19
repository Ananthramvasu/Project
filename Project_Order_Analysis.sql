use guvi_project;
select * from retail_orders;

-- 1.Find top 10 highest revenue generating products
select Order_Id,product_Id,(Quantity * List_Price ) as Revenue_Column from retail_orders order by Revenue_Column desc limit 10; 

-- 2.Find the top 5 cities with the highest profit margins
select City from retail_orders order by Profit desc limit 5;

-- 3.Calculate the total discount given for each category
select Category,sum(Discount) as Total_Discount from retail_orders group by Category;

-- 4. Find the average sale price per product category
select Category,Sub_Category,avg(Sale_Price) as Average_Sale_Price from retail_orders group by Category,Sub_Category;

-- 5. Find the region with the highest average sale price
select City,Region,round(avg(Sale_Price),3) as Average_Sale_Price from retail_orders group by City,Region order by Average_Sale_Price desc limit 1;

-- 6. Find the total profit per category
select Category,sum(Profit) as Total_Profit from retail_orders group by Category;

-- 7. Identify the top 3 segments with the highest quantity of orders
select Segment,sum(Quantity) as Total_Quantity from retail_orders group by Segment order by Total_Quantity desc limit 3;

-- 8.  Determine the average discount percentage given per region
select Region,round(avg(Discount_Percent),2) as Average_Discount_Price from retail_orders group by Region;

-- 9. Find the product category with the highest total profit
select Category,Sub_Category,round(sum(Profit),2) as Total_Profit from retail_orders group by Category,Sub_Category order by Total_Profit desc limit 1;

-- Calculate the total revenue generated per year
-- SELECT YEAR(Order_Date) AS Year, SUM(Quantity * List_Price) AS Total_Revenue
-- FROM retail_orders
-- GROUP BY Year
-- ORDER BY Year; 
-- 10. Calculate the total revenue generated per year 
select year(str_to_date(Order_Date,'%d-%b-%y')) as Order_Year, sum((Quantity * List_Price )) as Total_Revenue from retail_orders group by Order_Year order by Order_Year;
select  year(str_to_date(Order_Date,'%d-%b-%y')) as Order_Year from retail_orders;

-- 10 queries to be created on own
-- 1. retrive cost price greater than 250
select * from retail_orders where Cost_Price > 250 order by Cost_Price asc;

-- 2. selecting cost price of specific id
select Cost_Price from retail_orders where Order_Id = 5998;

-- 3.  Setting up primary and foreign key
ALTER TABLE retail_orders ADD PRIMARY KEY (Order_Id);

-- 4. Modifying the datatype of the column.
ALTER TABLE retail_orders MODIFY COLUMN Category VARCHAR(255);

-- 5. creating another table to called Segment details and copying the values from the main table
create table Segment_Details (
    Order_Id int primary key,
    Segment varchar(100),
    Country varchar(100),
    City varchar(100)
);

insert into Segment_Details (Order_Id,Segment,Country,City)
select distinct Order_Id,Segment,Country,City from retail_orders;
select * from Segment_Details;

-- 6. altering the primary key of Segment_Details
ALTER TABLE Segment_Details DROP PRIMARY KEY;
alter table Segment_Details add constraint pk_Order_Id primary key (Order_Id);

select * from retail_orders;
select * from Segment_Details;

-- 7. joins 
select * from retail_orders join Segment_Details on retail_orders.Order_Id = Segment_Details.Order_Id;
select * from retail_orders join Segment_Details on retail_orders.Country = Segment_Details.Country;

-- 8. Write a query to categorize based on profits
select *,
case 
	when Profit > 50 then 'Margings are High'
    when Profit > 20 then 'Good profit'
    else 'Work hard to earn profit'
end as Profit_Category
from retail_orders;


-- 9. Date-Based Order Classification
select *,
case
	when year(str_to_date(Order_Date, '%d-%b-%y')) =  2023 then 'Very Recent Order'
    when year(str_to_date(Order_Date, '%d-%b-%y')) = 2022 then 'Recent Order'
    else 'Older Order'
end as Order_Date_Classification
from retail_orders;

-- 10. filtering the data
select Region,Postal_Code from retail_orders where Cost_Price > 100;
select Region, avg(Cost_Price) as Average_CP from retail_orders where City like 'Henderson' group by Region;
select Region, round(avg(Cost_Price),2) as Average_CP from retail_orders group by Region;