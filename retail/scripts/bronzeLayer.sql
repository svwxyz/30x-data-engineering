if EXISTS
(select 1 from sys.schemas s join sys.tables t on s.schema_id = t.schema_id where s.name='bronze' and t.name='retail')
begin 
    drop table bronze.retail
end


select * 
into bronze.retail
from dbo.sales_data
WHERE order_date >= (select last_uploaded from bronze.wtr where table_name='bronze.retail');

update bronze.wtr
set last_uploaded=(select max(order_date) from bronze.retail),
    last_updated=GETDATE()
where table_name='bronze.retail';


select * 
from bronze.retail;


