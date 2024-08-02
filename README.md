# RedBus_Web_Scraping
INTRODUCTION
	The "Redbus Data Scraping and Filtering with Streamlit Application" project aims to improve the transportation industry by making it easier to collect, analyze, and display bus travel data. Using Selenium for web scraping, this project automatically gathers detailed information from Redbus, such as bus routes, schedules, prices, and seat availability. By simplifying data collection and offering useful tools for making decisions based on data, this project can help make transportation operations more efficient and better planned.

PROBLEM STATEMENT
	The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

DOMAIN
	TRANSPORTATION

TECHNOLOGY
•	Python 3.12.4
•	MySQL 8.0
•	Selenium
•	Streamlit

INSTALLED PACKAGE
•	Selenium – pip install selenium, from selenium import webdriver
•	Pandas – pip install pandas
•	Streamlit – pip install streamlit
•	MySQL Connector– pip install mysql-connector-python
•	Streamlit-Option-Menu – pip install streamlit-option-menu

CODE FLOW 
	This project contains four files.
1.	Redbus.ipynb
2.	BusDetails.ipynb
3.	Sql.ipynb
4.	RedBus_APP.py
   
Redbus.ipynb  
 1. Importing Libraries:
    		Imports Selenium, time, and pandas libraries for web automation and data manipulation.
      2. Initializing the Browser:
   		Starts a new Chrome browser session with `webdriver.Chrome()`.
3. Loading the Webpage:
   		Navigates to the Redbus  online booking page.
4. Waiting for Page to Load:
   		Pauses the script for 3 seconds.
5. Maximizing the Browser Window:
   		Maximizes the browser window.
6. Setting Up Explicit Wait:
  		Creates an explicit wait with a 20-second timeout.
7. Defining the `State_link_route` Function:
    		Retrieves bus route links and names, handling pagination.
8. Extracting Data:
    		Calls the function to extract and store bus route links and names.
9. Handling Pagination:
    		Navigates through pages to gather all data.
10. Returning Data:
   		Returns lists of bus route links and names.
    
BusDetails.ipynb
1. Importing Libraries:
   	The script imports necessary libraries from Selenium for web automation, along with time for delays and pandas for data manipulation.
2. Reading the CSV File:
  	 Reads a CSV file containing bus route data using pandas and displays the content.
3. Initializing the Browser:
   	Starts a new Chrome browser session with `webdriver.Chrome()`.
4. Initializing Lists for Bus Details:
   	Creates empty lists to store bus details like names, types, start and end times, ratings, durations, prices, available seats, route names, and links.
5. Looping Through Each Link:
  	Iterates through each row in the dataframe to get the route link and route name.
6. Loading Each Link in Browser:
  	Opens each route link in the browser and pauses for 2 seconds to allow the page to load.
7. Clicking Elements to Reveal Bus Details:
 	 Finds elements containing the route link and clicks them to reveal bus details, adding a delay of 2 seconds after each click.
8. Clicking Button to View Buses:
 	Attempts to click a button to view buses. If the button is not found, the script continues to the next iteration.
9. Scrolling Through the Page:
 	Uses ActionChains to scroll down the page until no new content is loaded, pausing for 5 seconds between scrolls.
10. Extracting Bus Details:
   	Finds elements containing bus details (names, types, times, ratings, durations, prices, and seats) using XPath and extracts their text.
11. Appending Data to Lists:
   	 Appends extracted bus details to respective lists created earlier.
12. Printing Completion Message:
    	Prints "Successfully Completed" upon completion of the script.
    
Sql.ipynb
1. Importing Libraries:
   Imports pandas for data manipulation, mysql.connector for database connection, and numpy for numerical operations.
2. Reading CSV Files:
   Reads multiple CSV files containing bus data into individual pandas DataFrames.
3. Concatenating DataFrames:
   Concatenates the individual DataFrames into a single DataFrame named `Final_df`.
4. Converting Ratings to Numeric:
   Converts the "Ratings" column to string, removes the word "New", strips whitespace, extracts the first character, and converts it to a numeric type. Non-numeric values are set to NaN and then filled with 0.
5. Converting Prices to Numeric:
   Removes the "INR" string from the "Price" column, converts it to floating-point numbers, and fills NaN values with 0.
6. Handling NaN Values:
   Replaces any remaining NaN values in the DataFrame with None.
7. Filtering by Price:
   Filters the DataFrame to include only rows where the "Price" is less than or equal to 7000.
8. Saving to CSV:
   Saves the cleaned DataFrame to a CSV file at the specified path.
9. Installing MySQL Connector:
     Installs the MySQL connector for Python using pip.
10. Connecting to MySQL Database:
    Establishes a connection to the MySQL database with specified credentials.
11. Creating Database:
    Creates a new database named "REDBUS_INFO" if it does not already exist.
12. Creating Table:
    Creates a table named "bus_details" in the "REDBUS_INFO" database with specified columns.
13. Inserting Data into Table:
    Prepares an SQL insert query and inserts data from the DataFrame into the "bus_details" table.
14. Committing Changes:
    Commits the transaction to save changes to the database.
15. Printing Success Messages:
    Prints messages indicating successful creation of the table and insertion of values.

RedBus_APP.py
1. Importing Libraries:
   	Imports pandas for data manipulation, mysql.connector for database operations, Streamlit for creating the web application, and `option_menu` for navigation.
2. Database Connection:
   	Establishes a connection to a MySQL database named `redbus_info` and creates a cursor for executing SQL queries.
3. Loading Data Function:
   	Defines a function `load_data` that reads a CSV file for a given state and returns a list of bus routes.
4. List of States:
   	Creates a list of states for which bus route data is available.
5. Streamlit Page Setup:
   	Configures the Streamlit page layout to be wide and applies custom CSS styles for page background, headings, and fonts.
6. Custom Headings:
    Adds two custom-styled headings to the Streamlit app using HTML and CSS:
    A primary heading with teal color and serif font.
    A secondary heading with green color and sans-serif font.
7. State and Route Selection:
   	Creates a dropdown menu for selecting states and a list of routes based on the selected state.
   	Provides radio buttons for selecting bus type and fare range.
8. Fetching Data Based on Selection:
   	Defines a function `type_and_fare` that queries the `bus_details` table in the MySQL database based on selected bus type, fare range, and route.
   	Constructs an SQL query, executes it, and fetches results into a DataFrame.
9. Displaying Data:
   	Displays the filtered bus details DataFrame in the Streamlit app.
