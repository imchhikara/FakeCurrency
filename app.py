import pickle
import streamlit as st
from streamlit_option_menu import option_menu

  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

#Our prediction model
def prediction(variance,skewness,curtosis,entropy):
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


page_icon = ":dollar:"
page_title = "Fake Currency Detection"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

#Hide Streamlit Style
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer{visibility: hidden;}
    header{visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Navigation Menu
selected = option_menu(
    menu_title = None,
    options=["Prediction Centre","History"],
    icons =["bank","archive"],
    orientation="horizontal")

if selected == "Prediction Centre":
    html_temp = """
        <div style ="background-color:black;padding:10px">
        <h1 style ="color:yellow;text-align:center;">Currency - Real or Fake</h1>
        </div>
        """      
    st.markdown(html_temp, unsafe_allow_html = True)


    with st.form("entry_form", clear_on_submit=False):
        # the following lines create text boxes in which the user can enter 
        # the data required to make the prediction
        variance = st.slider("Variance", -20.0, 20.0, 0.0, step=0.0001)
        skewness = st.slider("Skewness", -20.0, 20.0, 0.0, step=0.0001)
        curtosis = st.slider("Curtosis", -20.0, 20.0, 0.0, step=0.0001)
        entropy = st.slider("Entropy", -20.0, 20.0, 0.0, step=0.0001)
        "---"
        submitted = st.form_submit_button("Predict")
        if submitted:
            #db.insert_period(variance,skewness,curtosis,entropy)
            result = prediction(variance,skewness,curtosis,entropy)
            if result == 0:
                st.warning('This is a Fake Currency!', icon="🚨")
                
            elif result == 1:
                st.success('This is a Real Currency!', icon="✅")
                st.balloons()


if selected == "History":
    st.error("Database feature is currently unavailable. Sorry for the inconvience.")
