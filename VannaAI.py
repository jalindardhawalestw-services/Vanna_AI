import os
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

# Set your API key and model name
api_key = '65972c34807d425b9ede327daabfc981'
vanna_model_name = 'stwai'

# Initialize VannaDefault with your API key and model name
vn = VannaDefault(model=vanna_model_name, api_key=api_key)

# Connect to your MSSQL database using the appropriate ODBC connection string
odbc_conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=STWDOTNETSERVER\\DEV19;DATABASE=ADAM;UID=stw;PWD=StW@2021*!$'
vn.connect_to_mssql(odbc_conn_str=odbc_conn_str)

# Create a VannaFlaskApp instance with your VannaDefault object
app = VannaFlaskApp(vn)

# Run the Flask app
if __name__ == "__main__":
    app.run()
