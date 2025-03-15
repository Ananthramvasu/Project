import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Function to create a connection to the MySQL database
def create_db_connection(host, user, password, database_name):
    connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    engine = create_engine(connection_string)
    return engine

# Function to execute and display query results
def execute_query(query):
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

# Streamlit app
st.title("Display Data from MySQL")

# Input fields for database connection details
host = st.text_input("Enter MySQL Host", "127.0.0.1")
user = st.text_input("Enter MySQL Username", "root")
password = st.text_input("Enter MySQL Password", type="password", value="*Varsha123$")
database_name = st.text_input("Enter Your Database Name")

# Query 1
with st.expander("Query 1: Retrieve cost price greater than 250"):
    query1 = st.text_area("SQL Query 1", 
        "SELECT * FROM retail_orders WHERE Cost_Price > 250 ORDER BY Cost_Price ASC;")
    if st.button("Execute Query 1"):
        execute_query(query1)

# Query 2
with st.expander("Query 2: Selecting cost price of specific ID"):
    query2 = st.text_area("SQL Query 2", 
        "SELECT Cost_Price FROM retail_orders WHERE Order_Id = 5998;")
    if st.button("Execute Query 2"):
        execute_query(query2)

# Query 3
with st.expander("Query 3: Setting up primary and foreign key"):
    query3 = st.text_area("SQL Query 3", 
        "ALTER TABLE retail_orders ADD PRIMARY KEY (Order_Id);")
    if st.button("Execute Query 3"):
        execute_query(query3)

# Query 4
with st.expander("Query 4: Modifying the datatype of the column"):
    query4 = st.text_area("SQL Query 4", 
        "ALTER TABLE retail_orders MODIFY COLUMN Category VARCHAR(255);")
    if st.button("Execute Query 4"):
        execute_query(query4)

# Query 5: Creating Table and Copying Data (Split into Two Buttons)
with st.expander("Query 5: Creating and Populating Segment_Details Table"):
    query5_create = "CREATE TABLE Segment_Details (Order_Id INT PRIMARY KEY, Segment VARCHAR(100), Country VARCHAR(100), City VARCHAR(100));"
    query5_insert = "INSERT INTO Segment_Details (Order_Id, Segment, Country, City) SELECT DISTINCT Order_Id, Segment, Country, City FROM retail_orders;"
    
    if st.button("Execute Query 5 - Create Table"):
        execute_query(query5_create)
    if st.button("Execute Query 5 - Insert Data"):
        execute_query(query5_insert)

# Query 6: Altering Primary Key
with st.expander("Query 6: Altering Primary Key of Segment_Details"):
    query6_drop = "ALTER TABLE Segment_Details DROP PRIMARY KEY;"
    query6_add = "ALTER TABLE Segment_Details ADD CONSTRAINT pk_Order_Id PRIMARY KEY (Order_Id);"

    if st.button("Execute Query 6 - Drop Primary Key"):
        execute_query(query6_drop)
    if st.button("Execute Query 6 - Add New Primary Key"):
        execute_query(query6_add)

# Query 7: Joins (Split into Two Buttons)
with st.expander("Query 7: Performing Joins"):
    query7_1 = "SELECT * FROM retail_orders JOIN Segment_Details ON retail_orders.Order_Id = Segment_Details.Order_Id;"
    query7_2 = "SELECT * FROM retail_orders JOIN Segment_Details ON retail_orders.Country = Segment_Details.Country;"
    
    if st.button("Execute Query 7 - Join on Order_Id"):
        execute_query(query7_1)
    if st.button("Execute Query 7 - Join on Country"):
        execute_query(query7_2)

# Query 8: Categorizing based on profits
with st.expander("Query 8: Categorize Based on Profits"):
    query8 = """SELECT *, 
    CASE 
        WHEN Profit > 50 THEN 'Margins are High'
        WHEN Profit > 20 THEN 'Good profit'
        ELSE 'Work hard to earn profit'
    END AS Profit_Category 
    FROM retail_orders;"""
    
    if st.button("Execute Query 8"):
        execute_query(query8)

# Query 9: Date-Based Order Classification
with st.expander("Query 9: Date-Based Order Classification"):
    query9 = """SELECT *, 
    CASE 
        WHEN YEAR(STR_TO_DATE(Order_Date, '%d-%b-%y')) = 2023 THEN 'Very Recent Order'
        WHEN YEAR(STR_TO_DATE(Order_Date, '%d-%b-%y')) = 2022 THEN 'Recent Order'
        ELSE 'Older Order'
    END AS Order_Date_Classification 
    FROM retail_orders;"""
    
    if st.button("Execute Query 9"):
        execute_query(query9)

# Query 10: Filtering Data
with st.expander("Query 10: Filtering the Data"):
    query10 = "SELECT Region, AVG(Cost_Price) AS Average_CP FROM retail_orders WHERE City LIKE 'Henderson' GROUP BY Region;"
    
    if st.button("Execute Query 10"):
        execute_query(query10)

# Query 11: Filtering Data
with st.expander("Query 11: Filtering the Data"):
    query11 = "SELECT Region, Postal_Code FROM retail_orders WHERE Cost_Price > 100;"
    
    if st.button("Execute Query 11"):
        execute_query(query11)

# Query 12: Calculating Average Cost Price per Region
with st.expander("Query 12: Calculating Average Cost Price per Region"):
    query12 = "SELECT Region, ROUND(AVG(Cost_Price), 2) AS Average_CP FROM retail_orders GROUP BY Region;"
    
    if st.button("Execute Query 12"):
        execute_query(query12)
