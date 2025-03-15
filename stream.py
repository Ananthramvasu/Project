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
with st.expander("Query 1: Top 10 highest revenue-generating products"):
    query1 = st.text_area("SQL Query 1", 
        "SELECT Order_Id, product_Id, (Quantity * List_Price) AS Revenue_Column "
        "FROM retail_orders ORDER BY Revenue_Column DESC LIMIT 10;")
    if st.button("Execute Query 1"):
        execute_query(query1)

# Query 2
with st.expander("Query 2: Top 5 cities with the highest profit margins"):
    query2 = st.text_area("SQL Query 2", 
        "SELECT City FROM retail_orders ORDER BY Profit DESC LIMIT 5;")
    if st.button("Execute Query 2"):
        execute_query(query2)
# Query 3
with st.expander("Query 3: Calculate the total discount given for each category"):
    query3 = st.text_area("SQL Query 3", 
        "select Category,sum(Discount) as Total_Discount from retail_orders group by Category;")
    if st.button("Execute Query 3"):
        execute_query(query3)
        
# Query 4
with st.expander("Query 4: Find the average sale price per product category"):
    query4 = st.text_area("SQL Query 4", 
        "select Category,Sub_Category,avg(Sale_Price) as Average_Sale_Price from retail_orders group by Category,Sub_Category;")
    if st.button("Execute Query 4"):
        execute_query(query4)
# Query 5
with st.expander("Query 5: Find the region with the highest average sale price"):
    query5 = st.text_area("SQL Query 5", 
        "select City,Region,round(avg(Sale_Price),3) as Average_Sale_Price from retail_orders group by City,Region order by Average_Sale_Price desc limit 1;")
    if st.button("Execute Query 5"):
        execute_query(query5)
#Query 6
with st.expander("Query 6:Find the total profit per category"):
    query6 = st.text_area("SQL Query 6","select Category,sum(Profit) as Total_Profit from retail_orders group by Category;")
    if st.button("Execute Query 6"):
        execute_query(query6)
#Query 7
with st.expander("Query 7: Identify the top 3 segments with the highest quantity of orders"):
    query7 = st.text_area("SQL Query 7","select Segment,sum(Quantity) as Total_Quantity from retail_orders group by Segment order by Total_Quantity desc limit 3;")
    if st.button("Execute Query 7"):
        execute_query(query7)
#Query 8
with st.expander("Query 8: Determine the average discount percentage given per region"):
    query8 = st.text_area("SQL Query 8","select Region,round(avg(Discount_Percent),2) as Average_Discount_Price from retail_orders group by Region;")
    if st.button("Execute Query 8"):
        execute_query(query8)
#Query 9
with st.expander("Query 9: Find the product category with the highest total profit"):
    query9 = st.text_area("SQL Query 9",
    "select Category,Sub_Category,round(sum(Profit),2) as Total_Profit from retail_orders group by Category,Sub_Category order by Total_Profit desc limit 1;")
    if st.button("Execute Query 9"):
        execute_query(query9)
#Query 10
with st.expander("Query 10: Calculate the total revenue generated per year"):
    query10 = st.text_area("SQL Query 10",
    "select year(str_to_date(Order_Date,'%d-%b-%y')) as Order_Year from retail_orders;")
    if st.button("Execute Query 10"):
        execute_query(query10)        
       