# 🛒 E-Commerce DLT Pipeline

A hands-on **Databricks Lakeflow Declarative Pipeline** project for processing e-commerce data using a **Medallion Architecture**.

## 🏗️ Architecture

`Source → Bronze → Silver → Gold`

## 🛠️ Tech Stack

- Databricks
- PySpark
- Delta Lake
- Lakeflow Declarative Pipelines (DLT)
- Unity Catalog

## ✨ Features

- Bronze / Silver / Gold architecture
- Streaming tables
- Data quality expectations
- Deduplication
- Change Data Capture (CDC)
- SCD Type 2
- Fact & Dimension tables

## 📊 Tables

```text
ecomm.src
├── customers
├── orders
└── products

ecomm.bronze
├── customer_b
├── order_b
└── products_b

ecomm.silver
├── customer_s
├── order_s
└── products_s

ecomm.gold
├── dimcustomer
├── dimproducts
└── factorder