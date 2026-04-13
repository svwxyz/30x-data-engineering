-- CREATE TABLE dbo.sales_data (
--     order_id INT ,
--     order_date DATE,
--     customer_id VARCHAR(10),
--     customer_name VARCHAR(100),
--     city VARCHAR(50),
--     product_id VARCHAR(10),
--     product_name VARCHAR(100),
--     category VARCHAR(50),
--     quantity INT,
--     unit_price DECIMAL(10,2),
--     total_amount DECIMAL(10,2),
--     payment_method VARCHAR(20)
-- );

-- Batch1
INSERT INTO sales_data VALUES
(1001,'2025-01-05','C001','Amit Sharma','Delhi','P101','Smartphone','Electronics',1,15000,15000,'UPI'),
(1002,'2025-01-06','C002','Neha Verma','Mumbai','P102','Laptop','Electronics',1,55000,55000,'Credit Card'),
(1003,'2025-01-07','C003','Rahul Singh','Bangalore','P103','Headphones','Accessories',2,2000,4000,'Debit Card'),
(1004,'2025-01-08','C004','Priya Mehta','Chennai','P104','Shoes','Fashion',1,3000,3000,'Cash'),
(1005,'2025-01-09','C005','Arjun Kapoor','Kolkata','P105','Watch','Fashion',1,7000,7000,'UPI'),
(1006,'2025-01-10','C001','Amit Sharma','Delhi','P106','Tablet','Electronics',1,20000,20000,'Credit Card'),
(1007,'2025-01-11','C006','Sneha Reddy','Hyderabad','P107','Backpack','Accessories',3,1500,4500,'Debit Card'),
(1008,'2025-01-12','C007','Vikas Gupta','Pune','P108','Office Chair','Furniture',1,8000,8000,'UPI'),
(1009,'2025-01-13','C008','Karan Malhotra','Delhi','P109','Monitor','Electronics',2,12000,24000,'Credit Card'),
(1010,'2025-01-14','C009','Anjali Desai','Ahmedabad','P110','Keyboard','Accessories',2,1000,2000,'Cash'),
(1011,'2025-01-15','C010','Rohit Jain','Jaipur','P111','Mouse','Accessories',3,500,1500,'UPI'),
(1012,'2025-01-16','C002','Neha Verma','Mumbai','P112','Refrigerator','Appliances',1,30000,30000,'Debit Card'),
(1013,'2025-01-17','C011','Meera Iyer','Bangalore','P113','Air Conditioner','Appliances',1,40000,40000,'Credit Card'),
(1014,'2025-01-18','C012','Aditya Roy','Delhi','P114','T-shirt','Fashion',4,800,3200,'Cash'),
(1015,'2025-01-19','C013','Kavita Nair','Chennai','P115','Sofa','Furniture',1,25000,25000,'UPI'),
(1016,'2025-01-20','C014','Manish Yadav','Lucknow','P116','Microwave','Appliances',1,10000,10000,'Debit Card'),
(1017,'2025-01-21','C015','Pooja Bansal','Delhi','P117','Jeans','Fashion',2,2000,4000,'Credit Card'),
(1018,'2025-01-22','C016','Sachin Patil','Pune','P118','Books','Education',5,500,2500,'UPI'),
(1019,'2025-01-23','C017','Deepak Kumar','Patna','P119','Printer','Electronics',1,9000,9000,'Cash'),
(1020,'2025-01-24','C018','Nisha Arora','Chandigarh','P120','Water Purifier','Appliances',1,12000,12000,'Debit Card');

-- Batch2
INSERT INTO sales_data VALUES
(1021,'2025-01-25','C019','Ravi Kumar','Delhi','P121','Smartwatch','Electronics',1,12000,12000,'UPI');

-- Batch3 
INSERT INTO sales_data VALUES
(1022,'2025-01-27','C020','Suresh Patel','Nepal','P122','Washing Machine','Appliances',1,18000,18000,'Credit Card');

-- Batch4 
INSERT INTO sales_data VALUES
(1021,'2025-01-29','C019','Ravi Kumar','Patna','P121','Smartwatch','Electronics',1,12000,12000,'UPI');

select DISTINCT * 
from dbo.sales_data
where customer_name in ('Sachin Patil','Rohit Jain')