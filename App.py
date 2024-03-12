# Core pkg

import streamlit as st

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    st.title("Main App") #
    
    menu =["Home", "EDA", "ML", "About"] #create menu list
    choice =st.sidebar.selectbox("Menu" ,menu)  #create sidebar to house menu
    
    #create a link for each menu
    
    if choice == "Home":
        st.subheader("Home")
    elif choice == "EDA":
        run_eda_app()
    elif choice == "ML":
        run_ml_app()
    else:
       st.subheader("About")   
     
   
       




if __name__ == '__main__':
   main()