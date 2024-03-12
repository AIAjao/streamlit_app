import streamlit as st
#load EDA pkg
import pandas as pd
import plotly.express as px
def run_eda_app():
    st.subheader("Exploratory data analysis")
    df = pd.read_csv("materials/prog_languages_data.csv")
    st.dataframe(df)
    
    
    fig = px.pie(df, values = "Sum", names = "lang", title = "")
    st.plotly_chart(fig)
    
    fig2 = px.bar(df, x="lang",y ="Sum",title = "")
    st.plotly_chart(fig2)