from etl.extract import extract_data
from etl.transform.transform_sales import TransformSales
from etl.load.load_sales import LoadSales

df = extract_data("data/sales.csv")
df_cleaned = TransformSales(df)
LoadSales(df_cleaned)