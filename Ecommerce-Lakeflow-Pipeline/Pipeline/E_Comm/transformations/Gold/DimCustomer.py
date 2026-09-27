from pyspark import pipelines as dp


dp.create_streaming_table('DimCustomer')

dp.create_auto_cdc_flow(
    target="DimCustomer",
    source="ecomm.silver.customer_s",
    keys=['customer_id'],
    sequence_by='updated_at',
    stored_as_scd_type=2
)
