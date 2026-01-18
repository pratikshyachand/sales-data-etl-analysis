import pandas as pd

def TransformProducts(df_raw):

    df  = df_raw[["ProductID", "Name", "Category", "Price"]].copy()

   # the commented out below lines of code is for understanding dataset before cleaning/conversion
    ''' print(df.head(10))
        df.info()
        print(df.isnull().sum())
        print(df.isna().sum())
        print(df.duplicated(subset="ProductID").sum())'''

    # Handle data types
    df["Price"] = df["Price"].astype(float).round(2)

    # Standardize text
    for col in ['Name', 'Category']:
        df[col] = df[col].str.strip().str.title()

    # print(df.head(10))
    # df.info()

    return df