from pyspark import pipelines as dp


dp.create_streaming_table('DimProducts')

dp.create_auto_cdc_flow(
    target="DimProducts",
    source="ecomm.silver.products_s",
    keys=['product_id'],
    sequence_by='updated_at',
    stored_as_scd_type=2
)
