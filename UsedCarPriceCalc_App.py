import streamlit as st
import pickle
import numpy as np
import pandas as pd
import datetime

# Read CSV file
carsData = pd.read_csv("train/cleaned_carsData.csv")

# Predict car value
def predictCarValue(carBrand,carModel,carDrive,carKM,carFuel,prevOwner,carAge,engPow,engCap,ml_model):
    """
    To predict the value of car.
    returns value in lakhs
    """

    # Type cast variables into required dtype
    engCap = float(engCap)
    engPow = float(engPow)
    carAge = int(carAge)

    # Input query
    ip = [carBrand,carModel,carDrive,carKM,carFuel,prevOwner,carAge,engPow,engCap]

    # Predict price for input query
    prediction = ml_model.predict(ip)
    
    # Retuen predicted price
    return prediction

# Load the trained model to predict
pickle_in = open("UsedCarPricePred_Model.pkl","rb")
carPrice_model = pickle.load(pickle_in)

# Build web App layout and Queries

# app title
st.title("Check your car's price")
st.write("Instant online quote")

# Get data 

# Get brand
make_brand = st.selectbox(label="Brand",options=carsData['make'].unique())
# Get model
model = st.selectbox("variant",carsData[carsData['make']==make_brand]["model"].unique())
# Get transmission
trans = st.selectbox("Transmission type",carsData['transmission'].unique())
# Get km driven
km = st.selectbox("km driven",carsData['km_driven'].unique())
# Get fuel 
fuel = st.selectbox("Fuel",carsData['fuel'].unique())
# Get previous owners
owner = st.selectbox("Owner",carsData['owner'].unique())
# Get car age
curr_year = datetime.date.today().year
year = st.selectbox("Purchased Year",range(curr_year-20,curr_year+1))
age = int(curr_year) - int(year)
# Get engine power
power = st.text_input("Engine Power (bhp eg: 74 or 87.81)")
# Get engine capacity
engin = st.text_input("Engine Capacity(In thousand eg: 0.789 or 1.2 or 1.8 )")

# Get car condition
cond = st.radio("Car Condition",("Good","Very Good","Excellent"),
                horizontal =True)

# Predict value
carValue = int()
if st.button("Calculate"):
    carValue = predictCarValue(make_brand,model,trans,km,fuel,owner,age,power,engin,carPrice_model)
    #carValue = round(carValue,2)
    # Max and min value
    maxVal = carValue + carValue/10 # Plus 10%
    minVal = carValue - carValue/10 # Minus 10%
    diff = (maxVal-minVal)/3

    # Value based on condition
    if cond == "Good":
        minCondVal = minVal
        maxCondVal = minVal + diff
    elif cond == "Very Good":
        minCondVal = minVal + (2*diff)
        maxCondVal = maxVal - diff
    elif cond == "Excellent":
        minCondVal = maxVal - diff
        maxCondVal = maxVal

    st.write("Price based on car condition")
    st.success("₹{} Lakhs - ₹{} Lakhs".format(round(minCondVal,2),
                                                         round(maxCondVal,2)))
    st.write("Get your car inspected for exact price")