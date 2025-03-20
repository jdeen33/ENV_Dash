#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:56:15 2025

@author: jdeen@middlebury.edu
"""

 #fd
import pandas as pd
import numpy as np 
import plotly
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import altair as alt
 
import streamlit as st 
## code from https://python.plainenglish.io/how-to-build-interactive-dashboards-in-python-with-plotly-using-streamlit-047979344d93
#applayout


## Source https://toxigon.com/building-a-multi-page-interactive-dashboard-with-streamlit-and-plotly

## basic layout
st.set_page_config(layout="wide")
st.markdown("## Welcome to Middlebury's Greenhouse Gas Emissions Dashboard")
#st.image('https://github.com/jdeen33/ENV_Dash/blob/main/Data/energy2028-logo.png?raw=true', use_container_width=False)
st.markdown('This dashboard shows a summary of Greenhouse Gas Emissions from the years 2006 to 2024, broken down by type, and measured in metric tons, as well as offsets used to calculate the college’s net emissions')

   
col1, col2 = st.columns((3,1))
 
##functions to make various plots 

def make_bar_graph(df,xval,yval,color1,cs1,title_):
    fig = px.bar(df, x=xval, y=yval,color=color1, color_discrete_sequence= cs1, title=title_,
    hover_data={"Fiscal_Year":False,"Emissions_Source":True,"MTCDE":True},labels={"MTCDE":"Metric Tons of Carbon Dioxide","Fiscal_Year":"Fiscal Year", "Emissions_Source":"Source of Emissions"})
    fig.update_layout(font_family="Balto",font=dict(size=30), margin=dict(l=30, r=30, t=25, b=0))
    fig.update_layout(title_font_weight=1000)
    fig.update_xaxes(rangeselector_font_size=50)
    return fig

all_scopes = pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/all_scopes.csv")
scope1A= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope1_sums.csv")
scope1B= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope1B_MTCDE.csv")
scope2= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope2_sums.csv")
scope3=pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope3_MTCDEs.csv")
        

with col1:       
    st.write("**Tip**: Hover your cursor over the graph to see underlying data points. Double click on a variable in the legend to display it by itself on the chart")
    fig = make_bar_graph(all_scopes, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Safe, title_= "Middlebury College Greenhouse Gas Inventory: 2006-2024")         
    st.plotly_chart(fig)#, use_container_width=True)


   
    st.write ("Double click on any variable in the legend to isolate it on the graph")
    fig1=make_bar_graph(scope1A, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Bold, title_= "Middlebury College Greenhouse Gas Inventory: Scope1A")                
    st.plotly_chart(fig1,use_container_width=True)
    
  
    st.write("Double click on any box in the legend visual to isolate it on the graph")
    fig1=make_bar_graph(scope1B, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Bold, title_= "Middlebury College Greenhouse Gas Inventory: Scope1B")                
    st.plotly_chart(fig1,use_container_width=True)
        
  
    st.write("Double click on any box in the legend visual to isolate it on the graph")
    fig1=make_bar_graph(scope2, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Set2_r, title_= "Middlebury College Greenhouse Gas Inventory: Scope2")                
    st.plotly_chart(fig1,use_container_width=True)
        
  
    st.write("Double click on any box in the legend visual to isolate it on the graph")
    fig1=make_bar_graph(scope3[scope3["Emissions_Source"]!="Total"], xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.D3_r, title_= "Middlebury College Greenhouse Gas Inventory: Scope3")                
    st.plotly_chart(fig1,use_container_width=True)
with col2:
    st.markdown("**Scope 1** : Direct Emissions from both stationary & mobile combustion of fossil fuels purchased and owned by the institution\n\n**Scope 2**: Indirect Emissions from Electricity Purchases - Includes emissions from all stationary combustion of fossil fuels done in direct proportion to an energy source purchased by the institution \n\n**Scope 3**: Indirect Emissions from Outsourced Travel - This section includes all emissions from the mobile combustion of fossil fuels used in vehicles whose services are directly solicited by the institution. It also includes indirect emissions from landfill waste. \n\n**Offsets Internal**:  \n\n**Offsets External**:")

  #fig.update_traces(textposition= "middle center",marker= dict(line=dict(width=2)))
   #fig.update_traces(hovertemplate="<b>Source: %{label}</b><br>MTCD: %{value}<extra></extra>")
   #fig.update_layout(margin=dict(t=0, l=25, r=25, b=0))       
