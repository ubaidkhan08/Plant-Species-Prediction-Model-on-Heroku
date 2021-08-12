import streamlit as st
from joblib import dump, load
import numpy as np

log_model = load('Multi_class_log_model.joblib')

def classify(sepal_length, sepal_width, petal_length, petal_width):
    input=np.array([[sepal_length, sepal_width, petal_length, petal_width]]).astype(np.string_)
    prediction=model.predict(input)
    pred = '{}'.format(prediction)
    return(pred)


    
def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
    """
    
    sl=st.slider('Select Sepal Length', 0.0, 10.0)
    sw=st.slider('Select Sepal Width', 0.0, 10.0)
    pl=st.slider('Select Petal Length', 0.0, 10.0)
    pw=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=[[sepal_length, sepal_width, petal_length, petal_width]]
   

    if st.button('Classify'):
        output=classify(sepal_length, sepal_width, petal_length, petal_width)
        st.success('The species of the plant is {}'.format(output[1:-1]))
       
     
if __name__=='__main__':
    main()
