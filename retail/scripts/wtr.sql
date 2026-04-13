if not EXISTS(select 1 from sys.schemas s join sys.tables t on s.schema_id = t.schema_id where s.name='bronze' and t.name='wtr')
BEGIN
    create table bronze.wtr
    (
        table_name varchar(200),
        last_uploaded date,
        last_updated DATETIME2(6) 
    )
end

select * from bronze.wtr


insert into bronze.wtr 
VALUES ('bronze.retail', '1990-01-01',getdate());



