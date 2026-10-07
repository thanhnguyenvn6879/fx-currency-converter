# FX Currency Converter

A simple currency exchange web application built with Python and Streamlit.

The application retrieves exchange rate data from the Frankfurter API and allows users to convert between different currencies using both the latest and historical exchange rates.

## Features

- Convert between multiple international currencies
- Retrieve the latest available exchange rate
- Check historical exchange rates by selecting a date
- Calculate the converted currency amount
- Display the inverse exchange rate
- Interactive web interface built with Streamlit

## Application Preview

### Latest Exchange Rate

![Latest Exchange Rate](images/test-rate.png)

### Historical Exchange Rate

![Historical Exchange Rate](images/historical-rate.png)

## Technologies Used

- Python
- Streamlit
- Requests
- Frankfurter API

## Project Structure

```text
fx-currency-converter/
│
├── images/
│   ├── latest-rate.png
│   └── historical-rate.png
│
├── app.py
├── api.py
├── currency.py
├── frankfurter.py
├── requirements.txt
├── .gitignore
└── README.md

## How it work
The application follows a simple workflow:
1. The user enters an amount to convert.
2. The user selects the source currency.
3. The user selects the target currency.
4. The application requests exchange rate data from the Frankfurter API.
5. The converted amount and inverse exchange rate are calculated.
6. The result is displayed through the Streamlit interface.
Users can also select a date to retrieve a historical exchange rate.
Code Overview
app.py
Contains the Streamlit user interface and handles user interactions such as:
- Entering an amount
- Selecting currencies
- Requesting the latest exchange rate
- Selecting a historical date
- Displaying conversion results
api.py
Handles HTTP requests to the Frankfurter API.
frankfurter.py
Contains functions for retrieving:
- Available currencies
- Latest exchange rates
- Historical exchange rates
currency.py
Calculates the converted amount and inverse exchange rate and formats the final result.
Installation
Clone the repository:
git clone https://github.com/thanhnguyenvn6879/fx-currency-converter.git

Move into the project directory:
cd fx-currency-converter

Install the required packages:
python -m pip install -r requirements.txt

Run the Application
Start the Streamlit application:
python -m streamlit run app.py

The application will normally open in your browser at:
http://localhost:8501

Data Source
Exchange rate data is retrieved from the Frankfurter API.
Frankfurter provides current and historical foreign exchange rate data.
https://www.frankfurter.app/
Example
For example, a user can enter:
Amount: 100
From: AUD
To: CAD

The application retrieves the latest AUD/CAD exchange rate and displays:
- The exchange rate
- The converted amount
- The inverse exchange rate
Purpose
This project demonstrates the use of Python for:
- Consuming data from a REST API
- Organising code into reusable modules
- Processing and formatting API responses
- Building an interactive web application with Streamlit
