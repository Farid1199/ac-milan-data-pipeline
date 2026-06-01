# 🔴⚫ AC Milan Performance ETL Pipeline (2023/24 Season)

## 📌 Project Overview
This project is an automated **ETL (Extract, Transform, Load)** pipeline designed to process and analyze AC Milan's performance data for the 2023/24 Serie A season. 

The goal was to take raw match and player data, engineer new performance metrics (like Goal Contributions and Match Goal Differences), and load them into a structured SQL database for professional-grade analytics.

---

## 🏗️ ETL Architecture
The pipeline follows a modular architecture to ensure clean code and scalability:

```mermaid
graph LR
    A[Raw CSV Data] --> B[Extract]
    B --> C[Transform]
    C --> D[Load]
    D --> E[(SQLite DB)]
    D --> F[Clean CSV Exports]
    E --> G[SQL Analytics]