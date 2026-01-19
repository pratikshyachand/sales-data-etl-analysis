## 📊 Sales Data ETL, Analysis and Visualization

An end-to-end data analytics project demonstrating a complete workflow from raw CSV files --> ETL --> SQL database --> Analysis --> Visualization

The objective of this project is to practice **data engineering fundamentals**  and **data analysis using SQL + Python**.

## 📌 Project Overview

1. Extracted from CSV files
2. Built an **ETL pipeline** using Python
3. Loaded cleaned data into a **SQL Server database**
4. Analyzed data using **SQL and pandas**
5. Visualized insights using **matplotlib and seaborn**

## 🛠️ Tech Stack

### Languages and Libraries
- Python
- pandas
- matplotlib
- seaborn
- pyodbc
- sqlalchemy

### Tools
- VS Code
- Git and Github

## ⚙️ Requirements
- Python 3.12+
- Microsoft SQL Server (SQLEXPRESS)
- ODBC Driver 17+
- SQL Server Management Studio (SSMS)

## 📂 Dataset
 
Source: Kaggle (Retail Sales Dataset)

## 🟰 ETL Pipeline

**1. Extract**
- Load CSV files from **Kaggle Dataset using pandas**

**2. Transform**
- Remove duplicate records
- Handle missing values
- Convert columns into appropriate data type
- Clean text fields (strip(), title())

**3. Load**
- Load cleaned data into **SQL server**
- Data connection handled using **pyodbc**
- Tables created with proper relationships

## 🔍 Data Analysis
- SQL queries executed using **SQLAlchemy**
- Analysis performed inside **Jupyter Notebook and Python Scripts**</br>
- Key analysis included:
  - Revenue by Product
  - Revenue by Country
  - Top Customers by Revenue
  - Product Performance in Countries
  - Revenue by Category
  - Monthly Revenue
  - Quantity vs Revenue by Product

## 📈 Data Visualization
  Visualization are created using matplotlib and seaborn based on SQL query results.

## ▶️ How to Run the Project
  
  The following instructions are written for **Windows 11**:

  **1. Clone the Repository**
  ```bash 
    git clone https://github.com/pratikshyachand/sales-data-etl-analysis.git

    cd sales-data-etl-analysis
  ```

  **2. Create  and Activate Virtual Environment**
```bash
  python -m venv myvenv

  myvenv\Scripts\activate
```
  **3. Install Dependencies**
  ```bash
     pip install -r requirements.txt
```
  **4. Setup SQL Server**

  - Ensure SQL Server is installed and running
  - Install ODBC Driver 17+
  
  **5. Create Database Tables**
  - Open SQL Server Management Studio (SSMS)
  - Connect to your SQL Server instance
  - Create and select your database
  - Run the SQL script in sql\create_tables.sql to create tables 

  **6. Configure Database Connection**
  - Update config.py with your server and database details.

 **7. Run ETL Pipeline**
 ```bash
    python -m etl.run_etl
 ```
  
  **8. Run Analysis and Visualization**
  - Open analysis/analysis_visualization.ipynb in VS Code
  - Select the correct Python Kernel
  - Run cells sequentially to generate analysis and visualization
 ---
🤝 **Contributing**

This project is for learning purposes.
Feel free to fork, improve or suggest enhancements.
