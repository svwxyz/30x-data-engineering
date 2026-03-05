# Databricks notebook source
# MAGIC %sql
# MAGIC select * from sales_dwh.silver.sales_S

# COMMAND ----------

# MAGIC %md
# MAGIC ##DIM Order

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.DimOrder(
# MAGIC   orderKey bigint generated always as identity,
# MAGIC   OrderID int,
# MAGIC   OrderDate date
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.DimOrder
# MAGIC (OrderID,OrderDate)
# MAGIC select distinct 
# MAGIC   s.OrderID,
# MAGIC   s.OrderDate
# MAGIC from sales_dwh.silver.sales_S s
# MAGIC left join sales_dwh.gold.DimOrder g
# MAGIC on s.OrderID = g.OrderID
# MAGIC where g.OrderID is null 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.gold.dimorder

# COMMAND ----------

# MAGIC %md
# MAGIC ##DIM Customer

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.DimCustomer(
# MAGIC   CustomerKey bigint generated always as identity,
# MAGIC   CustomerID  varchar(200),
# MAGIC   CustormerName varchar(200),
# MAGIC   CustomerSegment varchar(200)
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.dimcustomer
# MAGIC (CustomerID,CustormerName,CustomerSegment)
# MAGIC select distinct
# MAGIC   s.customerid,
# MAGIC   s.customername,
# MAGIC   s.customersegment
# MAGIC from sales_dwh.silver.sales_S s
# MAGIC left join sales_dwh.gold.dimcustomer g
# MAGIC on s.customerid = g.customerid
# MAGIC where g.customerid is null

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.gold.dimcustomer

# COMMAND ----------

# MAGIC %md
# MAGIC #DIM Location

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.DimLocation(
# MAGIC   location_key bigint generated always as identity,
# MAGIC   country varchar(200),
# MAGIC   City varchar(200)
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.dimlocation
# MAGIC (country,City)
# MAGIC select distinct
# MAGIC   s.country,
# MAGIC   s.city
# MAGIC from sales_dwh.silver.sales_s s 
# MAGIC left join sales_dwh.gold.dimlocation g 
# MAGIC on s.country = g.country
# MAGIC and s.city = g.city
# MAGIC where  g.Country is null

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.gold.dimlocation

# COMMAND ----------

# MAGIC %md
# MAGIC #DimProduct

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.dimproduct(
# MAGIC     productkey bigint generated always as identity ,
# MAGIC     productid varchar(200),
# MAGIC     productName varchar(200))

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.dimproduct
# MAGIC (productid,productName)
# MAGIC select distinct
# MAGIC   s.productid,
# MAGIC   s.productname
# MAGIC from sales_dwh.silver.sales_s s
# MAGIC left join sales_dwh.gold.dimproduct g
# MAGIC on s.ProductID = g.productid 
# MAGIC where g.productid is null

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.gold.dimproduct

# COMMAND ----------

# MAGIC %md
# MAGIC #Dim Category 

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.dimcategory(
# MAGIC     categorykey bigint generated always as identity,
# MAGIC     category varchar(200),
# MAGIC     subcategory varchar(200)
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.dimcategory
# MAGIC (category,subcategory)
# MAGIC select 
# MAGIC   s.category ,
# MAGIC   s.subcategory
# MAGIC from sales_dwh.silver.sales_s s 
# MAGIC left join sales_dwh.gold.dimcategory g 
# MAGIC on s.Category = g.category
# MAGIC and s.SubCategory = g.subcategory
# MAGIC where g.category is null

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.gold.dimcategory

# COMMAND ----------

# MAGIC %md
# MAGIC #Dim ShipMode

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.dimshipmode(
# MAGIC      shipmodekey bigint generated always as identity,
# MAGIC      shipmode varchar(200))

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.dimshipmode
# MAGIC (shipmode)
# MAGIC select distinct 
# MAGIC   s.shipmode 
# MAGIC from sales_dwh.silver.sales_s s
# MAGIC left join sales_dwh.gold.dimshipmode g
# MAGIC on s.shipmode = g.shipmode 
# MAGIC where g.shipmode is null 

# COMMAND ----------

# MAGIC %md
# MAGIC #DIM Region

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.dimregion(
# MAGIC       regionKey bigint generated always as identity,
# MAGIC       region varchar(200))

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.dimregion 
# MAGIC (region)
# MAGIC select 
# MAGIC   distinct s.region 
# MAGIC from sales_dwh.silver.sales_s s 
# MAGIC left join sales_dwh.gold.dimregion g
# MAGIC on s.region = g.region
# MAGIC where g.region is null 

# COMMAND ----------

# MAGIC %md
# MAGIC #Fact Table 

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.gold.factSales(
# MAGIC     orderkey bigint,
# MAGIC     customerkey bigint ,
# MAGIC     location_key bigint,
# MAGIC     productkey bigint,
# MAGIC     categorykey bigint,
# MAGIC     shipmodekey bigint,
# MAGIC     regionkey bigint,
# MAGIC     quantity int,
# MAGIC     unityprice decimal(10,2),
# MAGIC     discount decimal(10,2),
# MAGIC     totalsales decimal(10,2),
# MAGIC     profit decimal(10,2)
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into sales_dwh.gold.factSales
# MAGIC select 
# MAGIC   do.orderkey,
# MAGIC   dc.customerkey,
# MAGIC   dl.location_key,
# MAGIC   dp.productkey,
# MAGIC   dca.categorykey,
# MAGIC   ds.shipmodekey,
# MAGIC   dr.regionkey,
# MAGIC   s.quantity,
# MAGIC   s.unitprice,
# MAGIC   s.discount,
# MAGIC   s.totalsales,
# MAGIC   s.profit
# MAGIC from sales_dwh.silver.sales_s s 
# MAGIC left join sales_dwh.gold.dimorder do on s.orderid = do.OrderID
# MAGIC left join sales_dwh.gold.dimcustomer dc on  s.CustomerID = dc.CustomerID
# MAGIC left join sales_dwh.gold.dimlocation dl on s.city = dl.city and s.country = dl.country 
# MAGIC left join sales_dwh.gold.dimproduct dp on s.productid = dp.productid
# MAGIC left join sales_dwh.gold.dimcategory dca on s.category = dca.category and s.subcategory = dca.subcategory
# MAGIC left join sales_dwh.gold.dimshipmode ds on s.shipmode = ds.shipmode
# MAGIC left join sales_dwh.gold.dimregion dr on s.region = dr.region 
# MAGIC left join sales_dwh.gold.factSales f
# MAGIC     ON f.orderkey = do.orderkey
# MAGIC    AND f.productkey = dp.productkey
# MAGIC WHERE f.orderkey IS NULL
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.gold.factSales

# COMMAND ----------

# MAGIC %sql
# MAGIC select 
# MAGIC     * 
# MAGIC from sales_dwh.gold.dimcustomer

# COMMAND ----------

# MAGIC %sql
# MAGIC select 
# MAGIC     do.orderid,
# MAGIC    do.orderdate,
# MAGIC     dc.customerid,
# MAGIC     dc.custormerName,
# MAGIC     dc.customersegment,
# MAGIC    dl.country,
# MAGIC     dl.city,
# MAGIC     dp.productid,
# MAGIC     dp.productname,
# MAGIC     dca.category,
# MAGIC    dca.subcategory,
# MAGIC     f.quantity,
# MAGIC     f.unityprice,
# MAGIC     f.discount,
# MAGIC     f.totalsales,
# MAGIC     f.profit,
# MAGIC     ds.shipmode,
# MAGIC     dr.region
# MAGIC   from sales_dwh.gold.factSales f
# MAGIC   left join sales_dwh.gold.dimcategory dca on f.categorykey = dca.categorykey
# MAGIC   left join sales_dwh.gold.dimshipmode ds on f.shipmodekey = ds.shipmodekey
# MAGIC   left join sales_dwh.gold.dimregion dr on f.regionkey = dr.regionkey
# MAGIC   left join sales_dwh.gold.dimcustomer dc on f.customerkey = dc.customerkey
# MAGIC   left join sales_dwh.gold.dimlocation dl on f.location_key = dl.location_key
# MAGIC   left join sales_dwh.gold.dimorder do on f.orderkey = do.orderkey
# MAGIC   left join sales_dwh.gold.dimproduct dp on f.productkey = dp.productkey
# MAGIC   where do.orderid = 1009