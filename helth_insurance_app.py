import streamlit as st
import joblib   

def main():
    html_temp = '''
    <div style="background-color:gray;padding:15px">
    <h2 style="color:white";text-align:center>Helth Insuarance Cost Prediction</h2>
    <div>
    
    '''
    
    
    st.markdown(html_temp, unsafe_allow_html=True)
    model = joblib.load('helth_insu')
    
    p1 = st.slider('Enter Your Age',18, 100)
    s1 = st.selectbox('Sex',('Male', 'Female'))
    if s1 == 'Female':
        p2 = 0
    else:
        p2 = 1
        
    p3 = st.number_input('Enter Your BMI Value')
    p4 = st.selectbox('Number of Children', list(range(0, 4)))
    s2 = st.selectbox('Smoker',('yes', 'no'))
    if s1 == 'no':
        p5 = 0
    else:
        p5 = 1
    p6 = st.slider('Enter The Region',1,4)
    
    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6]])   
        st.balloons()
        st.success(f'Your Insurance Cost is ${pred[0]:,.2f}') 
    
    
if __name__ == '__main__':  
    main()
    