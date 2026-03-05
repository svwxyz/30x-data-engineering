# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df = spark.sql("""
      select * from sales_dwh.bronze.sales_b
      """)

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.withColumn('CustomerName',upper(trim(col('CustomerName'))))\
        .withColumn('CustomerSegment',upper(trim(col('CustomerSegment'))))\
            .withColumn('Country',upper(trim(col('Country'))))\
                .withColumn('City',upper(trim(col('City'))))\
                    .withColumn('ProductName',upper(trim(col('ProductName'))))\
                        .withColumn('Category',upper(trim(col('Category'))))\
                            .withColumn('SubCategory',upper(trim(col('SubCategory'))))\
                                .withColumn('ShipMode',upper(trim(col('ShipMode'))))\
                                    .withColumn('Region',upper(trim(col('Region'))))

# COMMAND ----------

df = df.dropDuplicates()

# COMMAND ----------

df.write.format('delta')\
    .mode('overwrite')\
        .saveAsTable('sales_dwh.silver.sales_s')