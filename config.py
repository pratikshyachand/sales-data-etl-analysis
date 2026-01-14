import pyodbc

# returns a connection to the SQL Server database
def getConnection():
    con = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=Chand\\SQLEXPRESS;"
        "DATABASE=AnalyticsDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return con



