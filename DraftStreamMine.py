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
with st.expander("Query 1: Retrive cost price greater than 250"):
    query1 = st.text_area("SQL Query 1", 
        "select * from retail_orders where Cost_Price > 250 order by Cost_Price asc;")
    if st.button("Execute Query 1"):
        execute_query(query1)

# Query 2
with st.expander("Query 2: Selecting cost price of specific id"):
    query2 = st.text_area("SQL Query 2", 
        "select Cost_Price from retail_orders where Order_Id = 5998;")
    if st.button("Execute Query 2"):
        execute_query(query2)
# Query 3
with st.expander("Query 3: Setting up primary and foreign key"):
    query3 = st.text_area("SQL Query 3", 
        "ALTER TABLE retail_orders ADD PRIMARY KEY (Order_Id);")
    if st.button("Execute Query 3"):
        execute_query(query3)
        
# Query 4
with st.expander("Query 4: Creating another table to called Segment details and copying the values from the main table"):
    query4 = st.text_area("SQL Query 4", 
        "create table Segment_Details ( Order_Id int primary key,Segment varchar(100), Country varchar(100),City varchar(100));insert into Segment_Details (Order_Id,Segment,Country,City)select distinct Order_Id,Segment,Country,City from retail_orders;")
    if st.button("Execute Query 4"):
        execute_query(query4)
# Query 5
with st.expander("Query 5: viewing the new table"):
    query5 = st.text_area("SQL Query 5", 
        'select * from Segment_Details')
    if st.button("Execute Query 5"):
        execute_query(query5)
#Query 6
with st.expander("Query 6: Altering the primary key of Segment_Details"):
    query6 = st.text_area("SQL Query 6","ALTER TABLE Segment_Details DROP PRIMARY KEY; alter table Segment_Details add constraint pk_Order_Id primary key (Order_Id);")
    if st.button("Execute Query 6"):
        execute_query(query6)
#Query 7
with st.expander("Query 7: Joins"):
    query7 = st.text_area("SQL Query 7","select * from retail_orders join Segment_Details on retail_orders.Order_Id = Segment_Details.Order_Id;select * from retail_orders join Segment_Details on retail_orders.Country = Segment_Details.Country;")
    if st.button("Execute Query 7"):
        execute_query(query7)
#Query 8
with st.expander("Query 8: Write a query to categorize based on profits"):
    query8 = st.text_area("""select Profit,
case 
	when Profit > 50 then 'Margings are High'
    when Profit > 20 then 'Good profit'
    else 'Work hard to earn profit'
end as Profit_Category
from retail_orders;""")
    if st.button("Execute Query 8"):
        execute_query(query8)
#Query 9
with st.expander("Query 9: Date-Based Order Classification"):
    query9 = st.text_area("SQL Query 9",
    """select 
case
	when year(str_to_date(Order_Date, '%d-%b-%y')) =  2023 then 'Very Recent Order'
    when year(str_to_date(Order_Date, '%d-%b-%y')) = 2022 then 'Recent Order'
    else 'Older Order'
end as Order_Date_Classification
from retail_orders WHERE Order_Date_Classification IS NOT NULL;""")
    if st.button("Execute Query 9"):
        execute_query(query9)
#Query 10
with st.expander("Query 10: filtering the data"):
    query10 = st.text_area("SQL Query 10",
    "select Region, avg(Cost_Price) as Average_CP from retail_orders where City like 'Henderson' group by Region;")
    if st.button("Execute Query 10"):
        execute_query(query10) 
#Query 11
with st.expander("Query 11: filtering the data"):
    query11 = st.text_area("SQL Query 11",
    "select Region,Postal_Code from retail_orders where Cost_Price > 100;")
    if st.button("Execute Query 11"):
        execute_query(query11) 
#Query 12
with st.expander("Query 12: filtering the data"):
    query12 = st.text_area("SQL Query 12",
    "select Region, round(avg(Cost_Price),2) as Average_CP from retail_orders group by Region;")
    if st.button("Execute Query 12"):
        execute_query(query12)         
       