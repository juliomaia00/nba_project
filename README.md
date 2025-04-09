# 🏀 Projeto NBA com PySpark + Databricks + S3

Este projeto é um pipeline de ingestão e transformação de dados da NBA, utilizando PySpark no Databricks e armazenamento em buckets S3. Os dados são tratados e armazenados no formato Delta Lake, organizados em camadas (Bronze neste caso), com versionamento no GitHub.

---

## 🚀 Objetivo

O objetivo deste projeto é:

- Demonstrar a ingestão de dados de um bucket S3
- Realizar um pequeno processamento com PySpark (filtro, transformação e cálculo)
- Salvar os dados como Delta Lake
- Criar uma tabela gerenciada no Hive Metastore (Databricks Community Edition)
- Disponibilizar a estrutura como exemplo real de pipeline de dados em nuvem

---

## 🧱 Arquitetura


 Ingestão Local -> S3 (CSV cru) → Databricks (PySpark Processamento) → S3 (Delta Lake) → Tabela Hive (Processesing)