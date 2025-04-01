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
st.image('https://github.com/jdeen33/ENV_Dash/blob/main/Data/energy2028-logo.png?raw=true', use_container_width=False)
st.markdown('**About this project**: Since 2006, Middlebury College has been tracking its carbon emissions, and the sources of those emissions as part of our efforts to use less energy, and to cease all greenhouse gas emissions. You can download all of the data if you want to do your own analysis. And we’ve created a codebook that explains how the data is structured and the assumptions we made when doing calculations and conversions.' )
st.markdown("We categorize our emissions using the greenhouse gas protocols. These divide emissions into three scopes:  **Scope 1**, **Scope 2**,  and **Scope 3**")
#st.markdown("**Scope 1** :  Emissions from burning fossil fuels on campus\n\n**Scope 2**: Emissions from electricity used on campus.\n\n**Scope 3**: Indirect Emissions from Outsourced Travel - This section includes all emissions from the mobile combustion of fossil fuels used in vehicles whose services are directly solicited by the institution. It also includes indirect emissions from landfill waste. \n\nWe also track two types of offsets:\n\n**Offsets Internal**:Carbon offsets from college-owned carbon sinks. \n\n**Offsets External**:Carbon offsets purchased from external sources. \n\n     \n\n         ")

 
##make_bar_graph function notes (used for all visualizations in dashboard)
## df = pandas dataframe created from csv file- using pd.read_csv()
##xval= x axis values(column in dataframe(df))
##yval= y axis values(in this function is denoted by df column name)
##color1= qualitative variable that you want to be distinguished by color (denoted by df column name)NOT the actual colors in the graph
##cs1= from plotly qualitative color swatches https://plotly.com/python/discrete-color/
  ## cs1 must be input as px.colors.qualitative.x (replace x with the name of the swatch you want to use)
## reference links to plotly documentation provided for all fig.update_layout() methods used
def make_bar_graph(df,xval,yval,color1,cs1,title_, s_title):
    fig = px.bar(df, x=xval, y=yval,color=color1, color_discrete_sequence= cs1, title=title_,
    hover_data={"Fiscal_Year":False,"Emissions_Source":True,"MTCDE":True},labels={"MTCDE":"Metric Tons of Carbon Dioxide","Fiscal_Year":"Fiscal Year", "Emissions_Source":"Source of Emissions"}) #renaming labels from column names to be more legible. The True/False hover data dictionary controls which labels show up when hovering over parts of the graph with mouse #https://plotly.com/python/hover-text-and-formatting/#disabling-or-customizing-hover-of-columns-in-plotly-express    #hover text labeling https://plotly.com/python/figure-labels/#automatic-labelling-with-plotly-express
    fig.update_layout(font_family="Balto",font=dict(size=45), margin=dict(l=30, r=30, t=30, b=0)) #font style, size, and margins of graph #https://plotly.com/python/figure-labels/#global-and-local-font-specification
    fig.update_layout(title_font_weight=1000, title_subtitle_text=s_title) #title_font_weight > makes text bolder the higher the number #https://plotly.com/python/figure-labels/#manual-labelling-with-graph-objects #https://plotly.com/python/reference/layout/#layout-font
    fig.update_layout(title_subtitle_font_size= 13) #can change integer to change size of subtitle font #https://plotly.com/python/reference/layout/#layout-title-subtitle
    fig.update_layout(title_font_size= 17) ##can change integer to change size of title font #https://plotly.com/python/reference/layout/#layout-title
    fig.update_xaxes(rangeselector_font_size=50,autotickangles=[30]) #https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-autotickangles  #https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-rangeselector-font
    return fig

all_scopes = pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/all_scopes.csv")
scope1A= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope1_sums.csv")
scope1B= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope1B_MTCDE.csv")
scope2= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope2_sums.csv")
scope3=pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope3_MTCDEs.csv")
scope1= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/scope1_sums.csv")       
     

fig = make_bar_graph(all_scopes, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Safe, title_= "Middlebury College Greenhouse Gas Inventory: 2006-2024",s_title= "We also track two types of offsets. Internal Offsets: Carbon offsets from college-owned carbon sinks. External Offsets: Carbon offsets purchased from external sources." )
        
st.plotly_chart(fig, use_container_width=True) #creating stacked bar for all scopes


fig1=make_bar_graph(scope1, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Bold, title_= "Middlebury College Greenhouse Gas Inventory: Scope 1", s_title= "Emissions from burning fossil fuels on campus.")               
st.plotly_chart(fig1,use_container_width=True) #stacked nar for scope 1 emissions 
    
  
   
fig2=make_bar_graph(scope2, xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.Set2_r, title_= "Middlebury College Greenhouse Gas Inventory: Scope 2", s_title= "Emissions from electricity used on campus.")                
st.plotly_chart(fig2,use_container_width=True) #stacked bar for scope 2 emissions 
        
  
fig3=make_bar_graph(scope3[scope3["Emissions_Source"]!="Total"], xval= "Fiscal_Year" ,yval= "MTCDE", color1="Emissions_Source", cs1=px.colors.qualitative.D3_r, title_= "Middlebury College Greenhouse Gas Inventory: Scope 3",s_title= "Emissions from college-related travel and landfill waste." )               
st.plotly_chart(fig3,use_container_width=True) #stacked bar for scope 3 emissions 
    


  