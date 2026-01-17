from etl.extract import extract_data
from etl.transform.transform_customers import TransformCustomers
from etl.load.load_customers import LoadCustomers

df = extract_data("data/customers.csv")
df_cleaned = TransformCustomers(df)
LoadCustomers(df_cleaned)