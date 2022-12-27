import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(variance,skewness,curtosis,entropy):  
   
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Fake Currency Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:black;padding:13px">
    <h1 style ="color:white;text-align:center;">The Magical App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    variance = st.slider("Variance", min_value=-20.0, max_value=20.0)
    skewness = st.slider("Skewness", min_value=-20.0, max_value=20.0)
    curtosis = st.slider("Curtosis", min_value=-20.0, max_value=20.0)
    entropy = st.slider("Entropy", min_value=-20.0, max_value=20.0)
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(variance,skewness,curtosis,entropy)
        if result == 0:
            st.success('This is a Fake Currency')
        elif result == 1:
            st.success('This is a Real Currency')
     
if __name__=='__main__':
    main()