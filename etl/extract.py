import pandas as pd
import os

DATA_DIR = "data" # Folder containing CSVs

def extract_all():
    data = {}

    data['customers'] = pd.read_csv(os.path.join(DATA_DIR, "customers.csv")) # creates path to customers.csv
    data['products'] = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))   # creates path to products.csv
    data['sales'] = pd.read_csv(os.path.join(DATA_DIR, "sales.csv"))         # creates path to sales.csv

    return data



