
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report



import pickle
filename = 'auto_scout_pickle'
prediction_model = pickle.load(open(filename, 'rb'))

# st.sidebar.title("IMPORTANT!")
# st.sidebar.info("If you want to control train data and make exploratory data analysis on this data, please press the button 'EDA'")
# st.sidebar.write("")
# st.sidebar.info("If you want to make prediction about your car, please press the button 'PREDICTION'")
# st.sidebar.success("")
# radio = st.sidebar.radio("PRESS ONE", ["","EDA","PREDICTION"])
# st.sidebar.success("")

# if radio == "EDA":
#     df = pd.read_csv("auto_scout_train.csv")
#     pr = df.profile_report()

#     st_profile_report(pr)

# elif radio == "PREDICTION":

model = st.sidebar.selectbox("Model Selection:", ['Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia','Renault Clio', 'Renault Duster', 'Renault Espace'])
gear_type = st.sidebar.selectbox("Gearing Type:", ['Automatic', 'Manual', 'Semi-automatic'],index=0)
age = st.sidebar.selectbox("Age:", [0,1,2,3],key=int)
gear= st.sidebar.select_slider("Gears:", [5,6,7,8,9], key=int)
hp = st.sidebar.number_input("Horse_Power:",min_value=40, max_value=250, step=1)
km = st.sidebar.number_input("KM:",step=1)

audia1_jpg = "https://cdn.motor1.com/images/mgl/pm6zJ/s3/audi-a1-2018.jpg"
audia3_jpg = "https://cdn.motor1.com/images/mgl/WOYxj/s3/audi-a3-sportback-40-tfsi-e-2020.webp"
opel_astra = "https://cdn.motor1.com/images/mgl/bq6yk/s3/opel-astra-2021.webp"
opel_corsa = "https://cdn.motor1.com/images/mgl/zokE6/s3/opel-corsa-e-lead.webp"
opel_insignia = "https://cdn.motor1.com/images/mgl/00y6m/s3/2017-opel-insignia-grand-sport.jpg"
renault_clio = "https://cdn.motor1.com/images/mgl/gZnG4/s3/renault-clio.webp"
renault_duster = "https://cdn.motor1.com/images/mgl/VAmwB/s3/dacia-duster-facelift-2021.jpg"
renault_espace = "https://cdn.motor1.com/images/mgl/ZBXyA/s3/renault-espace-5-restyle-2020.webp"


if model == "Audi A1":
    st.image(audia1_jpg)
elif model == 'Audi A3':
    st.image(audia3_jpg)
elif model == 'Opel Astra':
    st.image(opel_astra)
elif model == 'Opel Corsa':
    st.image(opel_corsa)
elif model == 'Opel Insignia':
    st.image(opel_insignia)
elif model == 'Renault Clio':
    st.image(renault_clio)
elif model == 'Renault Duster':
    st.image(renault_duster)
else:
    st.image(renault_espace)

col1, col2 = st.columns(2)
col1.success(f"Model: {model}")
col1.success(f"Gear type : {gear_type}")
col1.success(f"Age: {age}")
col1.success(f"Gear {gear}")
col1.success(f"Horse power {hp}")
col1.success(f"Kilometer : {km}")

my_dict  = {"make_model" : model, "hp_kW" : hp, "km" :km, "age": age, "Gearing_Type": gear_type, "Gears":gear}
my_df = pd.DataFrame.from_dict([my_dict])
pred = prediction_model.predict(my_df)

predict_style = f"""
    <div style="background-color:#073763;font-size:20px;height: 5em;border-radius:20px;width: 15em;margin: auto">
    <h2 style="color:white;text-align:center;"> {str(int(pred[0]))+" $"} </h2>
    </div>
    """

if col2.button("Calculate Your Car Price"): 
    col2.markdown(predict_style,unsafe_allow_html=True)



m = col2.markdown("""<style>
div.stButton > button:first-child {
    background-color: #ea9999;
    color: white;
    height: 10em;
    width: 15em;
    border-radius:20px;
    border:3px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

# div.stButton > button:hover {
# 	background:linear-gradient(to bottom, #ef7676 5%, #ef7676 100%);
# 	background-color:#ef7676;
# }
# div.stButton > button:active {
# 	position:relative;}
#  <style>""", unsafe_allow_html=True)

