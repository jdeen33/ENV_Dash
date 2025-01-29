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

df= pd.read_csv("/Users/jdeen@middlebury.edu/Documents/ENV_Dashboard/ENV_Dash/Data/Tidy/all_scopes.csv")

f_df = df[df['Scope_Total_MCTDEs']!= "Total"]

chart_type = st.selectbox('Choose a chart type', ['Bar', 'Line'])

if chart_type == 'Bar':
    fig = px.bar(f_df, x= "Year" ,y= "value", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Safe)

elif chart_type == 'Line':
    fig = px.line(f_df, x= "Year" ,y= "value", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Bold)

## Display the chart
st.plotly_chart(fig, use_container_width=True)









scopes= ["Scope 1","Scope 2", "Scope 3", "Offsets Internal", "Offsets External"]
emissions_data=  df[df["Scope_Total_MCTDEs"].isin(scopes)]
selected_scope= st.selectbox("Select Scope", scopes)

filtered_df= df[df["Scope_Total_MCTDEs"]==selected_scope]
 
st.subheader(f"Emissions from {selected_scope}")

## bar chart for selected scope 

fig1 = px.bar(filtered_df, x= "Year" ,y= "value", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Safe)

st.plotly_chart(fig1)
    

## emissions by year 


years = ["2006_2007","2007_2008","2008_2009","2009_2010","2010_2011","2011_2012","2012_2013","2013_2014","2014_2015","2015_2016","2016_2017","2017_2018","2018_2019","2019_2020","2020_2021","2021_2022","2022_2023","2023_2024"]
selected_year= st.selectbox("Year",years)

st.subheader(f"GHGI Emissions in {selected_year}")
    
filtered_year= df[(df['Year']==selected_year)&( df['Scope_Total_MCTDEs']!= 'Total')]

fig2 = px.bar(filtered_year, x= "value" ,y= "Year", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Prism)

st.plotly_chart(fig2)


st.subheader("Emission Sources Breakdown by Year")

e_df = pd.read_csv("/Users/jdeen@middlebury.edu/Documents/ENV_Dashboard/ENV_Dash/Data/Vizuals/scopes1_2_treemapform.csv")

scope1 = e_df[e_df['Scope_Type']== "Scope 1"]
scope2= e_df[(e_df['Scope_Type']== "Scope 2")&(e_df['Source_MTCDEs']!= 'Scope 2 TOTAL' )]

fig2 = px.treemap(scope2.dropna(), path= ['Scope_Type','Year','Source_MTCDEs'],values= 'value', color='Source_MTCDEs',color_discrete_sequence=px.colors.qualitative.Bold)
st.plotly_chart(fig2)

    