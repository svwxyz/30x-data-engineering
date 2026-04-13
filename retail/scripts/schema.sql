-----------
--Scehma---
-----------


-----------
--Bronze---
-----------
if not EXISTS
(select 1 from sys.schemas where name='bronze')
BEGIN
    EXEC('create schema bronze;')
end


-----------
--Silver---
-----------

if not EXISTS
(select 1 from sys.schemas where name='silver')
begin 
    EXEC('Create schema silver');
END


-----------
--Gold---
-----------

if not EXISTS
(select 1 from sys.schemas where name='gold')
begin 
    EXEC('Create schema gold');
END

