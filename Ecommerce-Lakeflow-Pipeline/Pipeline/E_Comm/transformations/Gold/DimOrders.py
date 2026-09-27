from pyspark import pipelines as dp

@dp.table(name='ecomm.gold.FactOrder')
def DimOrders():
  return spark.readStream.table('ecomm.silver.order_s')