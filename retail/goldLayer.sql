-------------------
-----Gold Layer----
-------------------

---Dim Order---
if not EXISTS(
    select 1 
    from sys.schemas s 
    join sys.tables t 
    on s.schema_id = t.schema_id 
    where s.name='gold'
    and t.name='DimOrder'
)
Begin 
    create table gold.DimOrder
    (
        order_sk BIGINT IDENTITY,
        order_id int,
        order_date date)
end

---Insert Rows---

insert into gold.DimOrder
select DISTINCT s.order_id, s.order_date
from silver.retail_s s 
left join gold.DimOrder g 
on g.order_id = s.order_id 
where g.order_id is null;

---Dim Customer---
if not EXISTS(
    select 1 
    from sys.schemas s 
    join sys.tables t 
    on s.schema_id = t.schema_id 
    where s.name='gold' and t.name='DimCustomer')
begin 
    create table gold.DimCustomer
    (
        cust_sk BIGINT IDENTITY,
        customer_id varchar(200),
        customer_Name VARCHAR(200),
        city varchar(200),
        status VARCHAR(200)
    )
end


---Insert----

Merge into gold.DimCustomer g 
using silver.retail_s s
on s.customer_id=g.customer_id and g.status='Active'
when matched and (
                    g.customer_Name <> s.customer_name or 
                    g.city <> s.city )
            then 
                update set 
                    g.status='Expired';

insert into gold.DimCustomer 
(customer_id,customer_Name,city,status)
select DISTINCT s.customer_id, s.customer_name, s.city,'Active'
from silver.retail_s s 
left join gold.DimCustomer g 
on s.customer_id=g.customer_id and g.status='Active'
where g.customer_id is null or ( s.customer_name <> g.customer_Name or 
                                 s.city <> g.city)


---Dim Product--
if not exists(
    select 1 
    from sys.schemas s 
    join sys.tables t 
    on s.schema_id=t.schema_id 
    where s.name='gold' and t.name='DimProduct'
    )
begin 
    create table gold.DimProduct
    (
        product_sk bigint identity,
        product_id varchar(200),
        product_name varchar(200),
        product_category varchar(200)
    )
end 

--Insert--

insert into gold.DimProduct 
select 
    distinct
    s.product_id,
    s.product_name,
    s.category
from silver.retail_s s
left join gold.DimProduct g
on s.product_id=g.product_id 
where g.product_id is null

-- select * from gold.DimProduct;


----Dim Payment---

if not EXISTS
(
    select 1 
    from sys.schemas s 
    join sys.tables t 
    on s.schema_id = t.schema_id 
    where s.name='gold' and t.name='DimPayment'
)
BEGIN
    create table gold.DimPayment
    (
        payment_sk bigint identity,
        paymentMethod varchar(200)
    )
end

---Insert---

insert into gold.DimPayment 
select 
    distinct
    s.payment_method
from silver.retail_s s 
left join gold.DimPayment g 
on s.payment_method = g.paymentMethod
where g.paymentMethod is null;

-- select * from gold.DimPayment

--------------------
-----Fact Tables----
--------------------

if not exists(
    select 1 
    from sys.schemas s 
    join sys.tables t 
    on s.schema_id=t.schema_id
    where s.name='gold' and t.name='FactRetail'
)
begin 
    create table gold.FactRetail
    (
        orderID int,
        quantity int,
        UnitPrice Decimal(10,2),
        total_amount decimal(10,2),
        payment_sk bigint,
        product_sk bigint,
        customer_sk bigint,
        order_sk bigint
    )
end

----insert---

insert into gold.FactRetail
select 
    s.order_id,
    s.quantity,
    s.unit_price,
    s.total_amount,
    dp.payment_sk,
    dpr.product_sk,
    dc.cust_sk,
    do.order_sk
from silver.retail_s s 
left join gold.DimPayment dp on s.payment_method=dp.paymentMethod
left join gold.DimProduct dpr on s.product_id= dpr.product_id
left join gold.DimCustomer dc on s.customer_id=dc.customer_id and dc.status='Active'
left join gold.DimOrder do on s.order_id=do.order_id
WHERE NOT EXISTS (
    SELECT 1 
    FROM gold.FactRetail fr 
    WHERE fr.orderID = s.order_id
);


select * from gold.FactRetail;


-- select * from gold.DimCustomer;
-- select * from gold.DimOrder;
        