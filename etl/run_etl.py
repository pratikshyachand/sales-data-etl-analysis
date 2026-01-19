from etl.extract import extract_all
from etl.transform.transform_customers import TransformCustomers
from etl.load.load_customers import LoadCustomers
from etl.transform.transform_products import TransformProducts
from etl.load.load_products import LoadProducts
from etl.transform.transform_sales import TransformSales
from etl.load.load_sales import LoadSales

def main():

    # Extract
    raw_data = extract_all()
    print("Data extracted successfully") 

    # Transform
    customers_df = TransformCustomers(raw_data['customers'])
    products_df = TransformProducts(raw_data['products'])
    sales_df = TransformSales(raw_data['sales'])
    print("Data transformed successfully")

    # Load
    LoadCustomers(customers_df)
    LoadProducts(products_df)
    LoadSales(sales_df)
    print("Data loaded successfully")

if __name__ == "__main__":
  main()