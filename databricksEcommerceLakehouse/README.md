# Ecommerce Lakehouse Pipeline

**Author:** Sumit Vishwakarma  
**Date:** October 2026

A medallion-architecture lakehouse built using Databricks Lakeflow Spark Declarative Pipelines (SDP), PySpark, Delta Lake, and Unity Catalog to process the Olist e-commerce dataset.

## Architecture

The pipeline follows the **Bronze → Silver → Gold** pattern.

### Source — `ecomlkh.src`

Raw Olist staging tables:
- `olist_customers`
- `olist_orders`
- `olist_order_items`
- `olist_order_payments`
- `olist_products`

### Bronze — `ecomlkh.bronze`

Streaming tables ingest source data with minimal transformations.

- `customer_b` — Customer data with ingestion timestamp.
- `orders_b` — Order records.
- `orderitems_b` — Order-item records.
- `orderPayments_b` — Payment records.
- `products_b` — Product records.

### Silver — `ecomlkh.silver`

Cleaned and deduplicated datasets.

- `customer_s` — Customer history using SCD Type 2 and Auto CDC.
- `order_s` — Cleaned orders.
- `orderitems_s` — Cleaned order items.
- `payment_type` — Normalized payment types.
- `products_s` — Normalized product categories.

Data quality expectations validate required identifiers.

### Gold — `ecomlkh.gold`

Analytics-ready dimensional model built using materialized views.

- `dim_customers` — Customer dimension with SCD Type 2 history, hashed surrogate keys, and a current-record flag.
- `dim_products` — Product dimension with a hashed surrogate key.
- `fact_orders` — Order-level data with aggregated payment values and payment types.
- `fact_order_items` — Item-level sales and freight measures, enriched with product and historical customer dimensions.

## Repository Structure

```text
databricksEcommerceLakehouse/
├── Pipeline/
│   └── transformations/
│       ├── Bronze/
│       ├── Silver/
│       └── Gold/
└── test/
    └── Check
```

## Validation

The validation notebook checks:
- Bronze and Silver row counts.
- Customer SCD Type 2 history.
- Fact-table row counts.
- Duplicate order-item keys.
- Gold data consistency.

## Tech Stack

- Databricks Lakeflow Spark Declarative Pipelines
- PySpark
- Delta Lake
- Unity Catalog
- Python
- SQL
- Olist E-Commerce Dataset

## Author

**Sumit Vishwakarma**  
*Data Engineer | Python, SQL, PySpark | Azure, Databricks & Microsoft Fabric*

**Project Date:** October 2026
