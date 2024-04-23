import os
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

# Set your API key and model name


# Initialize VannaDefault with your API key and model name
api_key='65972c34807d425b9ede327daabfc981'
vanna_model_name='stw_ai'
vn = VannaDefault(model=vanna_model_name, api_key=api_key)
# Connect to your MSSQL database using the appropriate ODBC connection string
vn.connect_to_mssql(odbc_conn_str='DRIVER={ODBC Driver 17 for SQL Server};SERVER=Demo\\SQLDEV2022;DATABASE=nop_commerce;UID=sa;PWD=12345')
# vn.connect_to_mssql(odbc_conn_str=odbc_conn_str)

# Create a VannaFlaskApp instance with your VannaDefault object
app = VannaFlaskApp(vn)

# Run the Flask app
if __name__ == "__main__":
    app.run()
