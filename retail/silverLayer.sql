------------------
---Silver Layer---
------------------
if not EXISTS
(select 1 from sys.schemas s join sys.tables t on s.schema_id = t.schema_id where s.name='silver' and t.name='retail_s')
begin 
    create table silver.retail_s 
    (
        order_id int,
        order_date date ,
        customer_id varchar(200),
        customer_name varchar(200),
        city varchar(200),
        product_id varchar(200),
        product_name varchar(200),
        category varchar(200),
        quantity int,
        unit_price decimal(10,2),
        total_amount DECIMAL(10,2),
        payment_method varchar(200)
    )
end


insert into silver.retail_s
(order_id, order_date, customer_id, customer_name, city, product_id, product_name, category, quantity, unit_price, total_amount, payment_method)
select 
    DISTINCT
    b.order_id,
    b.order_date,
    lower(trim(b.customer_id)),
    lower(trim(b.customer_name)),
    upper(trim(b.city)),
    upper(trim(b.product_id)),
    upper(trim(b.product_name)),
    upper(trim(b.category)),
    b.quantity,
    b.unit_price,
    b.total_amount,
    upper(trim(b.payment_method))
from bronze.retail b;

select * from silver.retail_s;



























