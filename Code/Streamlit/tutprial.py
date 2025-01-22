# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st 

st.title("Streamlit Tutorial App")

st.write("This is my new app")

button1= st.button("Click me")  ##forms are better for lots of parameters 

if button1:
    st.write("This is some text ")
    
like= st.checkbox("Do you like this app?")

button2= st.button("Submit")

if button2:
    if like:
        st.write("thanks.I like it too")
    else:
        st.write("I'm sorry. You have bad taste")
        
        
        
st.header("Start of the Radio Button Section")

animal = st.radio("What animal is your favorite?", ("Lions","Tigers","Bears"))

button3 = st.button("Submit Animal")

if button3:
    st.write(animal)
    if animal== "Lions":
        st.write("Roar!")