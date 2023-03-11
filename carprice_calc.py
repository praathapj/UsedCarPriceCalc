import streamlit as st
import pickle
import numpy as np

st.title("Check your car's price")
st.write("Instant online quote")

make_brand = st.text_input("Brand","Type here")
model = st.text_input("variant","Type here in detail")
km = st.text_input("km driven","Type here in lakhs")
fuel = st.text_input("Fuel","Diesel or Petrol or CleanFuel(CNG/LPG)")
seller = st.text_input("Seller type","Individual or Dealer or Trustmark Dealer")
trans = st.text_input("Transmission type","Manual/Automatic")
owner = st.text_input("Owner","First /Second /Third /Fourth & Above/ Test Drive car")
seats = st.text_input("Seats","Type here")
mile = st.text_input("Mileage","Type here")
engin = st.text_input("Engine Capacity","Type here in thousands")
power = st.text_input("Engine Power","Type here in bhp")
age = st.text_input("Age","Type here(Current year - Purchased year)")

pickle_in = open("basic_randForest_carPredModel.pkl","rb")
carPrice = pickle.load(pickle_in)


def predictCarValue(make_brand,model,km,fuel,seller,trans,owner,seats,mile,engin,power,age,carPrice):
    """
    to predict the value of car.
    It takes 12 arguments and covert into 17 features.
    returns value in lakhs
    """
    km = float(km)
    mile = float(mile)
    engin = float(engin)
    power = float(power)
    age = float(age)

    bestResaleBrands = ['Toyota','Maruti','Hyundai','Kia','Honda','Mahindra','Tata']

    if make_brand in bestResaleBrands:
        resale = 1
    else:
        resale = 0

    if fuel == 'Diesel':
        fuel_Diesel = 1
        fuel_Petrol = 0
    elif fuel == 'Petrol':
        fuel_Diesel = 0
        fuel_Petrol = 1
    else:
        fuel_Diesel = 0
        fuel_Petrol = 0

    if seller == 'Individual':
        seller_type_Individual = 1
        seller_type_Trustmark_Dealer = 0
    elif seller == 'Trustmark Dealer':
        seller_type_Individual = 0
        seller_type_Trustmark_Dealer = 1
    else:
        seller_type_Individual = 0
        seller_type_Trustmark_Dealer = 0

    if trans == 'Manual':
        transmission_Manual = 1
    else:
        transmission_Manual = 0

    if owner == 'First':
        ofao = 0
        oso = 0
        otd = 0
        oto = 0
    elif owner == 'Second':
        ofao = 0
        oso = 1
        otd = 0
        oto = 0
    elif owner == 'Third':
        ofao = 0
        oso = 0
        otd = 0
        oto = 1
    elif owner == 'Test Drive car':
        ofao = 0
        oso = 0
        otd = 1
        oto = 0
    else:
        ofao = 1
        oso = 0
        otd = 0
        oto = 0

    if int(seats) >= 9:
        seats_btwn6To8 = 0
        seats_lessOrEq5 = 0
    elif int(seats) <= 5:
        seats_btwn6To8 = 0
        seats_lessOrEq5 = 1
    else:
        seats_btwn6To8 = 1
        seats_lessOrEq5 = 0

    ip = np.array([km,mile,engin,power,age,resale,fuel_Diesel,
                                 fuel_Petrol,seller_type_Individual,seller_type_Trustmark_Dealer,
                                 transmission_Manual,ofao,oso,otd,oto,seats_btwn6To8,seats_lessOrEq5]).reshape(1,-1)
    prediction = carPrice.predict(ip)
    
    return prediction


carValue = int()
if st.button("Calculate"):
    carValue = predictCarValue(make_brand,model,km,fuel,seller,trans,owner,seats,mile,
                               engin,power,age,carPrice)
    carValue = round(carValue[0],2)
st.success("Your car estimated value in lakhs: {}".format(carValue))