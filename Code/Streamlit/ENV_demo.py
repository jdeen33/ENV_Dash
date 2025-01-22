#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:56:15 2025

@author: jdeen@middlebury.edu
"""

 #fd
import pandas as pd
import numpy as np 
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
 
import streamlit as st 
## code from https://python.plainenglish.io/how-to-build-interactive-dashboards-in-python-with-plotly-using-streamlit-047979344d93
#applayout
st.title("ENV Dash Mockup")
st.write("Select a Scope to see emissions for that category")

df= pd.read_csv("/Users/jdeen@middlebury.edu/Documents/ENV_Dashboard/dash_mockup.csv")

scopes= ["Scope 1","Scope 2", "Scope 3", "Offsets Internal", "Offsets External"]
emissions_data=  df[df["Source"].isin(scopes)]
selected_scope= st.selectbox("Select Scope", scopes)

filtered_df= df[df["Source"]==selected_scope]


## bar chart for selected scope 


fig = px.bar(filtered_df, x= "Year" ,y= "value", color="Source", color_discrete_sequence=px.colors.qualitative.Safe)

st.plotly_chart(fig)
    

##treemap plot 
#st.subheader("")

#fig1 = px.treemap(df, path=['Year','Source'], values='value',
                 # color='Source')
#st.plotly_chart(fig1)


st.subheader("All Categories")

fig1 = px.bar(df, x= "Year" ,y= "value", color="Source", color_discrete_sequence=px.colors.qualitative.Antique)

st.plotly_chart(fig1)
    