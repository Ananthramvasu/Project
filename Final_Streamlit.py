import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Function to create a connection to the MySQL database
def create_db_connection(host, user, password, database_name):
    connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    engine = create_engine(connection_string)
    return engine

# Streamlit app
st.title("Display Data from MySQL")

# Input fields for database connection details
host = st.text_input("Enter MySQL Host", "127.0.0.1")
user = st.text_input("Enter MySQL Username", "root")
password = st.text_input("Enter MySQL Password", type="password", value="*Varsha123$")
database_name = st.text_input("Enter Your DataBase Name")

# Query to execute
query = st.text_input("Enter SQL Query", "SELECT * FROM retail_orders LIMIT 10")

# Execute the query and display results
if st.button("Execute Query"):
    if host and user and password and database_name and query:
        try:
            engine = create_db_connection(host, user, password, database_name)
            df = pd.read_sql_query(query, con=engine)
            st.write("Query executed successfully!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields and provide a valid query.")
