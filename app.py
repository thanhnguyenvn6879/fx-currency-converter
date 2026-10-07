import streamlit as st
from frankfurter import get_currencies, get_latest_rate, get_historical_rate
from currency import format_result
from datetime import datetime

# Title
st.title("FX Converter")

# Select amount of moneymoney
amount = st.number_input("Enter the amount to be converted:", min_value=0.00, value=50.0)
currencies = get_currencies()

# Select type of currency
from_currency = st.selectbox("From Currency:", options=currencies.keys(), index=list(currencies.keys()).index('AUD'))
to_currency = st.selectbox("To Currency:", options=currencies.keys(), index=list(currencies.keys()).index('USD'))

# Button for Get Latest Rate
if st.button("Get Latest Rate"):
    data = get_latest_rate(from_currency, to_currency)
    rate = data['rates'][to_currency]
    current_date = datetime.now().strftime('%Y-%m-%d')
    result = format_result(current_date, from_currency, to_currency, rate, amount)
    st.write(result)

# Box select date
date = st.date_input("Select a date for historical rates:")

# Button for Conversion Rate
if st.button("Conversion Rate"):
    historical_data = get_historical_rate(from_currency, to_currency, str(date))
    rate = historical_data['rates'][to_currency]
    result = format_result(str(date), from_currency, to_currency, rate, amount)
    st.write(result)
