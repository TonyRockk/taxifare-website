import streamlit as st
import datetime
import requests
# import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

#### User Input ####
# Date
d = st.date_input(
    "Select the day of pickup",
    datetime.date(2024, 5, 31))
st.write('You chose a taxi on:', d)

# Time
t = st.time_input('Select an hour', datetime.time(12, 00))
st.write('Your time', t)

# Pickup
pickup_longitude = st.number_input('Insert your pickup longitude', value=79.0, step=0.0001)
st.write('Your Pickup longitude is ', round(pickup_longitude,6))

pickup_latitude = st.number_input('Insert your pickup latitude', value=79.0)
st.write('Your Pickup latitude is ', pickup_latitude)

# dropoff
dropoff_longitude = st.number_input('Insert your dropoff longitude', value=79.0)
st.write('Your dropoff longitude is ', dropoff_longitude)

dropoff_latitude = st.number_input('Insert your dropoff latitude', value=79.0)
st.write('Your dropoff latitude is ', dropoff_latitude)

# Passenger
passenger_count = st.number_input(label='Number of person :', min_value=1, step=1)
st.write(passenger_count, 'people(s)')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

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

st.json(response)
fare = response["fare"]

st.text(f"The cost of the fare is : {round(fare,2)}$")
