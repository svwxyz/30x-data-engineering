from pyspark import pipelines as dp

dp.create_streaming_table('ecomlkh.silver.customer_s')

dp.create_auto_cdc_flow(

    target="ecomlkh.silver.customer_s",
    source="ecomlkh.bronze.customer_b",
    keys=['customer_id'],
    sequence_by='uploaded_at',
    stored_as_scd_type=2
)
