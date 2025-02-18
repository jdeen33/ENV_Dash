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
st.sidebar.title('Greenhouse Gas Emissions Inventory')
st.sidebar.image('https://github.com/jdeen33/ENV_Dash/blob/main/Data/energy2028-logo.png?raw=true', use_container_width=True)

page = st.sidebar.selectbox('Pages', ['Home', "Breakdown by Scope", 'Data & Methods'])  

##functions to make various plots 

def make_treemap(df,path1,values1,color1,cs1):
    fig = px.treemap(df.dropna(), path=path1, values =values1,color=color1, color_discrete_sequence= cs1)
    fig.update_traces(textposition= "middle center",marker= dict(line=dict(width=2)))
    fig.update_traces(hovertemplate="<b>Source: %{label}</b><br>MTCD: %{value}<extra></extra>")
    fig.update_layout(margin=dict(t=0, l=25, r=25, b=0))
    return fig

# layout and content of individual pages 
if page== 'Home': 
    st.title("Welcome to Middlebury's Greenhouse Gas Emissions Dashboard")
    st.write(" Learn more about Energy 2028 [here]('https://www.middlebury.edu/energy2028)")
    st.write('This dashboard shows a summary of Greenhouse Gas Emissions from the years 2006 to 2024, broken down by type, and measured in metric tons, as well as offsets used to calculate the college’s net emissions')
    
    
    #variables = st.sidebar.selectbox("Detailed Breakdown", ["Overall Emissions","Scope 1","Scope 2"])
    
    col1, col2 = st.columns((3,1), gap="large")
    
    df= pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Tidy/all_scopes.csv")
        
    f_df = df[df['Scope_Total_MCTDEs']!= "Total"]
        
    with col1:
        chart_type = st.selectbox('Choose a chart type', ['Bar', 'Line'])
        st.write("Tip: Hover your cursor over the graph to see underlying data points. Double click on a variable in the legend to display it by itself on the chart")
            
        if chart_type == 'Bar':
            fig = px.bar(f_df, x= "Year" ,y= "value", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Safe, title= "Middlebury College Greenhouse Gas Inventory: 2006-2024, sorted by Metric Tons",
            labels= {"value":"Metric Tons of Carbon Dioxide", "Year":"Fiscal Year","Scope_Total_MCTDEs":"Emission Scope"}  )
            
        elif chart_type == 'Line':
            fig = px.line(f_df, x= "Year" ,y= "value", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Bold, title= "Middlebury College Greenhouse Gas Inventory: 2006-2024, sorted by Metric Tons",
            labels= {"value":"Metric Tons of Carbon Dioxide", "Year":"Fiscal Year","Scope_Total_MCTDEs":"Emission Scope"})
            
            ## Display the chart
        st.plotly_chart(fig, use_container_width=True)
        

        
    with col2:
        st.text("Scope 1 : Direct Emissions from both stationary & mobile combustion of fossil fuels purchased and owned by the institution\n\nScope 2: Indirect Emissions from Electricity Purchases - Includes emissions from all stationary combustion of fossil fuels done in direct proportion to an energy source purchased by the institution \n\nScope 3: Indirect Emissions from Outsourced Travel - This section includes all emissions from the mobile combustion of fossil fuels used in vehicles whose services are directly solicited by the institution. It also includes indirect emissions from landfill waste. \n\nOffsets Internal:  \n\nOffsets External:")
     
    st.subheader("Emission Sources Breakdown by Year")
    st.write("Select a fiscal year to see emissions for that time period")
    years = ["2006_2007","2007_2008","2008_2009","2009_2010","2010_2011","2011_2012","2012_2013","2013_2014","2014_2015","2015_2016","2016_2017","2017_2018","2018_2019","2019_2020","2020_2021","2021_2022","2022_2023","2023_2024"]
    selected_year= st.selectbox("Year",years)       
    st.subheader(f"Middlebury College Greenhouse Gas Emissions in the {selected_year} Fiscal Year")
   
    filtered_year= f_df[(f_df['Year']==selected_year)]
    
    fig2 = px.bar(filtered_year, x= "Scope_Total_MCTDEs" ,y= "value", color="Scope_Total_MCTDEs", color_discrete_sequence=px.colors.qualitative.Prism,
    labels= {"value":"Metric Tons of Carbon Dioxide", "Year":"Fiscal Year","Scope_Total_MCTDEs":"Emission Scope"})
    st.plotly_chart(fig2)


elif page == "Breakdown by Scope":
    scope= st.sidebar.selectbox('Scope', ["Scope 1A", "Scope 2"])
    if scope == "Scope 1A":
        st.write("Click on any box in the visual to isolate it")
        e_df = pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Vizuals/scopes1_2_treemapform.csv")
        scope2= e_df[(e_df['Scope_Type']== "Scope 1")&(e_df['Source_MTCDEs']!= 'Scope 1 TOTAL' )]
        fig= make_treemap(scope2,['Year','Source_MTCDEs','value'],'value','Source_MTCDEs',px.colors.qualitative.T10)        
        st.plotly_chart(fig)#,use_container_width=True)
    
    elif scope== 'Scope 2':
        st.write("Click on any box in the visual to isolate it")
        e_df = pd.read_csv("https://raw.githubusercontent.com/jdeen33/ENV_Dash/refs/heads/main/Data/Vizuals/scopes1_2_treemapform.csv")
        scope2= e_df[(e_df['Scope_Type']== "Scope 2")&(e_df['Source_MTCDEs']!= 'Scope 2 TOTAL' )]
        fig= make_treemap(scope2,['Year','Source_MTCDEs','value'],'value','Source_MTCDEs',px.colors.qualitative.D3_r)        
        st.plotly_chart(fig)

        
