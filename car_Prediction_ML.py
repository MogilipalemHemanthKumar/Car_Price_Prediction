import streamlit as st
import pickle
import numpy as np
filename = "car_Prediction.sav"
data = pickle.load(open(filename, "rb"))
def prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = data.predict(input_data_reshaped)
    return float(prediction)
def main():
    Car_Name = st.text_input("Car_Name")
    Year = (st.text_input("Year"))
    Present_Price = (st.text_input("Present Price"))
    Kms_Driven = (st.text_input("Kms Driven"))
    Fuel_Type = st.text_input("Fuel Type")
    Seller_Type = st.text_input("Seller Type")
    Transmission = st.text_input("Transmission")
    Owner = st.text_input("Owner")
    final_Prediction = ''
    if st.button("Predict Price"):
        x=int((Fuel_Type).replace('Petrol', '0').replace('Diesel', '1').replace("CNG", '2'))
        y=int((Seller_Type).replace("Dealer",'0').replace("Individual",'1'))
        z=int((Transmission).replace("Manual",'0').replace("Automatic",'1'))
        A=int((Owner).replace("Yes",'1').replace("No",'0'))
        final_Prediction = prediction(
            [ int(Year),float(Present_Price), float(Kms_Driven),x,y,z,A])
    st.success(final_Prediction)

if __name__=="__main__":
    main()
