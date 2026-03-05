# Databricks notebook source
# MAGIC %md
# MAGIC #Bronze Layer

# COMMAND ----------

# MAGIC %md
# MAGIC ##Dropping Bronze Table First if exists

# COMMAND ----------

if spark.catalog.tableExists('sales_dwh.bronze.sales_b'):
    spark.sql('DROP table sales_dwh.bronze.sales_b')

# COMMAND ----------

# MAGIC %md
# MAGIC ##Creating Bronze Table Again

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists sales_dwh.bronze.sales_b
# MAGIC as 
# MAGIC select * from sales_dwh.default.sales_src
# MAGIC where OrderDate > (select last_loaded from sales_dwh.bronze.wtr)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_dwh.bronze.sales_b

# COMMAND ----------

# MAGIC %sql
# MAGIC update sales_dwh.bronze.wtr 
# MAGIC set last_loaded = (select max(OrderDate) from sales_dwh.bronze.sales_b),
# MAGIC     last_updated = getdate()