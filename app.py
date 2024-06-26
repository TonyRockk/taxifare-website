import streamlit as st
import datetime
import requests
# import pandas as pd

'''
# Taxi Fare App
'''

st.markdown('## Select your informations to get a price')

#### User Input ####
# Date
d = st.date_input(
    "Select the day of pickup",
    datetime.date(2024, 5, 31))
# st.write('You chose a taxi on:', d)

# Time
t = st.time_input('Select an hour', datetime.time(12, 00))
# st.write('Your time', t)

# Pickup
pickup_longitude = st.number_input('Insert your pickup longitude', value=79.0, step=0.0001)
# st.write('Your Pickup longitude is ', round(pickup_longitude,6))

pickup_latitude = st.number_input('Insert your pickup latitude', value=79.0)
# st.write('Your Pickup latitude is ', pickup_latitude)

# dropoff
dropoff_longitude = st.number_input('Insert your dropoff longitude', value=79.0)
# st.write('Your dropoff longitude is ', dropoff_longitude)

dropoff_latitude = st.number_input('Insert your dropoff latitude', value=79.0)
# st.write('Your dropoff latitude is ', dropoff_latitude)

# Passenger
passenger_count = st.number_input(label='Number of person :', min_value=1, step=1)
# st.write(passenger_count, 'people(s)')


url = 'https://taxifare.lewagon.ai/predict'

X_new = {
    "pickup_datetime": f'{d} {t}',
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
    }

r = requests.get(url, params=X_new)

response = r.json()

# st.json(response)
fare = response["fare"]

'''
## Price of your taxi !
'''

st.text(f"The cost of the fare is : {round(fare,2)}$")
