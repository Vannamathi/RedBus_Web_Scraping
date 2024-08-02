import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu

# Establish a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='redbus_info'
)
mycusror = mydb.cursor(buffered=True)

# Function to load data for a given state
def load_data(state):
    df = pd.read_csv(f"df_{state}.csv")
    routes = df["Route_name"].tolist()
    return routes

# List of states
states = ["Kerala", "Andhra Pradesh", "Telugana", "Goa", "Rajastan",
          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"]

# Setting up Streamlit page
slt.set_page_config(layout="wide")

slt.markdown(
    """
    <style>
    .main {
        background-color: #D3A7D3;
    }
    .title {
        color: red;
    }
    .custom-font {
        font-family: 'Times New Roman', Times, serif;
    }
    .heading-one {
        color: #4B0082; /* Teal color */
        font-size: 32px;
        text-align: center;
        font-family: serif; /* font */ 
    }
    .heading-two {
        color: green; 
        font-size: 28px;
        text-align: center;
        font-family: sans-serif; /* Different font */
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
slt.markdown('<h1 class="heading-one">Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit 🚌</h1>', unsafe_allow_html=True)
slt.markdown('<h2 class="heading-two">Explore Bus Routes and Types</h2>', unsafe_allow_html=True)
# States and Routes page setting

S = slt.selectbox("Lists of States", states)
routes = load_data(S.lower())

col1, col2 = slt.columns(2)
with col1:
    select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
with col2:
    select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))

# Select the route
route = slt.selectbox("List of routes", routes)

def type_and_fare(bus_type, fare_range):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="redbus_info")
    mycusror = conn.cursor()
    # Define fare range based on selection
    if fare_range == "50-1000":
        fare_min, fare_max = 50, 1000
    elif fare_range == "1000-2000":
        fare_min, fare_max = 1000, 2000
    else:
        fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

    # Define bus type condition
    if bus_type == "sleeper":
        bus_type_condition = "Bus_type LIKE '%Sleeper%'"
    elif bus_type == "semi-sleeper":
        bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
    else:
        bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

    query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{route}"
            AND {bus_type_condition}
            ORDER BY Price DESC
        '''
    mycusror.execute(query)
    out = mycusror.fetchall()
    conn.close()

    df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
    return df

df_result = type_and_fare(select_type, select_fare)
slt.dataframe(df_result)



#[theme]
#base="light"
#primaryColor="#158eb9"
#secondaryBackgroundColor="#183a7d"
#textColor="#0f0f10"
#font="serif"
