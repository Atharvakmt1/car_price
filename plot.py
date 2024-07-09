import numpy as np
import pandas as pd
import streamlit as st

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)

    # ADD NEW CODE HERE.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())