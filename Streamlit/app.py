import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to streamlit")
st.write("Hello! we will learn basics of streamlit.")
df = pd.DataFrame({
    'Name: ': ['Amit','Harsh','Rishi','Ashish'],
    'Age: ': [22,23,23,21]
})
st.write("Here is the data frame.")
st.write(df)
##Create a line chart
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)
st.title("Streamlit input")
name = st.text_input("Enter your Name: ")
if name:
    st.write("Hello ",name)
##Creating a slider
age = st.slider("Select your age: ",0,100,25)
if age:
    st.write("Your age is: ",age)
##Creating a select Box
options = ['Java','C','C++','Python','JavaScript']
choice = st.selectbox("Select your favorite language: ",options)
if choice:
    st.write("Your favorite language is: ",choice)
date = st.date_input("Select your birthday: ")
if date:
    st.write("Your birthday : ",date)