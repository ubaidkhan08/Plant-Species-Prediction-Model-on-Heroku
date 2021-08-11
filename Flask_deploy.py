from flask import Flask
from joblib import dump, load
import numpy as np
import streamlit as st

model = load('Multi_class_log_model.joblib')

def predict_forest(sepal_length, sepal_width, petal_length, petal_width):
    input=np.array([[sepal_length, sepal_width, petal_length, petal_width]]).astype(np.string_)
    prediction=model.predict(input)
    pred = '{}'.format(prediction)
    return(pred)

def main():
    st.title("Plant Species Predictor")
    html_temp = """
    <div style+="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    sepal_length = st.text_input("Sepal Length")
    sepal_width = st.text_input("Sepal Width")
    petal_length = st.text_input("Petal Length")
    petal_width = st.text_input("Petal Width")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_forest(sepal_length, sepal_width, petal_length, petal_width)
        st.success('The species of the plant is {}'.format(output[1:-1]))
        
        

        #if output > 0.5:
            #st.markdown(danger_html,unsafe_allow_html=True)
        #else:
            #st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
