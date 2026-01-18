from etl.extract import extract_data
from etl.transform.transform_products import TransformProducts
from etl.load.load_products import LoadProducts

df = extract_data("data/products.csv")
df_cleaned = TransformProducts(df)
LoadProducts(df_cleaned)

