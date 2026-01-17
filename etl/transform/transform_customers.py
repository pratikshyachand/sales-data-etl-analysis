import pandas as pd

def TransformCustomers(df):
    df = df[['CustomerID', 'FirstName', 'LastName', 'Country']]
    
    # Check for duplicates
    df = df.drop_duplicates(subset=["CustomerID"])

    # Check for missing values
    df = df.dropna(subset=["CustomerID"])
    df["FirstName"] = df["FirstName"].fillna( "Unknown")
    df["LastName"] = df["LastName"].fillna("Unknown")
    df["Country"] = df["Country"].fillna("Unknown")

    # Handle invalid data types
    df["CustomerID"] = df["CustomerID"].astype(str)
    df["FirstName"] = df["FirstName"].astype(str)
    df["LastName"] = df["LastName"].astype(str)
    df["Country"] = df["Country"].astype(str)



    # Standardize text formats
    df["FirstName"] = df["FirstName"].str.strip().str.title()
    df["LastName"] = df["LastName"].str.strip().str.title()
    df["Country"] = df["Country"].str.strip().str.title()

    return df


