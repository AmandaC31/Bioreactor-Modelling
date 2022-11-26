import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
#import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Deep Learning for Bioreactor Modelling and Control-Optimization')
st.markdown("""
This app performs allows Bioreactor start up to determine their feedstock characteristics and 
 optimize their process through forecasting and control.
""")
#Displaying full data

st.sidebar.header('User Input file')
st.sidebar.markdown('''           
[Example 1 CSV input file](https://raw.githubusercontent.com/AmandaC31/Bioreactor-Modelling/main/Example1.csv)

[Example 2 CSV input file](https://raw.githubusercontent.com/AmandaC31/Bioreactor-Modelling/main/Example2.csv)

[Example 3 CSV input file](https://raw.githubusercontent.com/AmandaC31/Bioreactor-Modelling/main/Example3.csv)

''')


#uploading csv file
uploaded_file = st.sidebar.file_uploader("Upload your CSV file with recorded data to display them and obtain your feedstock characteristics", type=["csv"])
if uploaded_file is not None:
   input_df = pd.read_csv(uploaded_file)


# 1. display recorded data from csv file table and graph
st.header('Your bioreactor recorded data ')
if uploaded_file is not None:
    if st.checkbox('Show dataset'):
        st.subheader('Recorded for a 24 hour period')
        st.write(input_df[:96])
    st.subheader('Dissolved oxygen')
    st.line_chart(x="Time (hour)", y="DO (mol/L)", data=input_df)
    st.subheader('Nitrate concentration')
    st.line_chart(x="Time (hour)", y="NO3 (mol/L)", data=input_df)
    st.subheader('Ammonia concentration')
    st.line_chart(x="Time (hour)", y="NH4+ (mol/L)", data=input_df)
    if st.checkbox('Show pH'):
        st.subheader('pH')
        st.line_chart(x="Time (hour)", y="pH", data=input_df)
    else :
        st.subheader('Hydrogen ion concentration')
        st.line_chart(x="Time (hour)", y="H+ (mol/L)", data=input_df)
else:
    st.write('Awaiting CSV file to be uploaded.')

# 2. Prediction of feedstocks parameters
st.header('Prediction of feedstock parameters')
if uploaded_file is not None:
    st.markdown("""
    Based on your recorded data, your feedstock characteristics are the following: 
    """)
else:
    st.write('Awaiting CSV file to be uploaded.')







# Reads in saved prediction model
#load_clf = pickle.load(open('XXX.plk', 'rb'))

# Apply model to make predictions
#prediction = load_clf.predict(input_df)


#st.write([prediction])


# 3. Forecasting data
with st.sidebar:
        st.write("Select bioreactor process characteristics for forecasting:")
def user_input_features():
        Biotype = st.sidebar.selectbox('Bioreactor type',('plug flow','batch'))
        DO = st.sidebar.slider('Dissolved oxygen (mol/L) ', 0.0000, 5.0000, 3.0000, 0.1000 )
        SN3O = st.sidebar.slider('Nitrate Concentration (mol/L)', 0.0000,0.0100,0.0050,0.0001 )
        SNH4 = st.sidebar.slider('Ammonia Concentration (mol/L)', 0.0000,0.0100,0.001,0.0001 )
        pH = st.sidebar.slider('pH', 0.0000,14.0000,7.0000, 0.1)
        data = {'Bioreactor type': Biotype,
                'Dissolved oxygen (mol/L)': DO,
                'Nitrate Concentration (mol/L)': SN3O,
                'Ammonia Concentration (mol/L)': SNH4,
                'pH': pH,
                }
        features = pd.DataFrame(data, index=[0])
        return features
st.header('Forecasting')
input_df_1 = user_input_features()
st.write(input_df_1)

st.markdown("""
The forecasting option is still in progress and will soon be available!
""")




#df.hist()
#st.pyplot()


#st.area_chart(input_df["Days"])

