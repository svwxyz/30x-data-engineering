# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark = SparkSession.builder.appName('dWH').getOrCreate()

# COMMAND ----------

# MAGIC %md
# MAGIC #Reading CSv

# COMMAND ----------

df = spark.read.format('csv')\
            .option('header','true')\
                .option('inferSchema','true')\
                    .load('/Volumes/sales_dwh/default/src/sales_data.csv')

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #Writing Table

# COMMAND ----------

df.write.format('delta')\
    .mode('overwrite')\
        .saveAsTable('sales_dwh.default.sales_src')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.default.sales_src

# COMMAND ----------

# MAGIC %md
# MAGIC #Creating Catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists sales_dwh;
# MAGIC use catalog sales_dwh

# COMMAND ----------

# MAGIC %md
# MAGIC #Creating Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists sales_dwh.bronze;
# MAGIC create schema if not exists sales_dwh.silver;
# MAGIC create schema if not exists sales_dwh.gold;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #Water Table 

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.bronze.wtr(
# MAGIC     table_name varchar(200),
# MAGIC     last_loaded date,
# MAGIC     last_updated timestamp
# MAGIC )

# COMMAND ----------

# %sql
# insert into sales_dwh.bronze.wtr
# values ('sales_b','1990-01-01',getdate())

# COMMAND ----------

# MAGIC %sql
# MAGIC select * 
# MAGIC from sales_dwh.bronze.wtr