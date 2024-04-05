import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1sD13fRIl21b1k8-DbriEbG-Or5RrPcXm"
    df = pd.read_csv(url)
    return df

df = load_data()

# Sidebar for user input
st.sidebar.title('Real Estate Preferences')
location = st.sidebar.selectbox('Location', df['Location'].unique())
price_range = st.sidebar.slider('Price Range ($)', float(df['Price'].min()), float(df['Price'].max()), (float(df['Price'].min()), float(df['Price'].max())))
bedrooms = st.sidebar.slider('Bedrooms', int(df['Bedrooms'].min()), int(df['Bedrooms'].max()), int(df['Bedrooms'].min()))
bathrooms = st.sidebar.slider('Bathrooms', int(df['Bathrooms'].min()), int(df['Bathrooms'].max()), int(df['Bathrooms'].min()))

# Filter the dataset based on user preferences
filtered_df = df[
    (df['Location'] == location) &
    (df['Price'] >= price_range[0]) &
    (df['Price'] <= price_range[1]) &
    (df['Bedrooms'] >= bedrooms) &
    (df['Bathrooms'] >= bathrooms)
]

# Display recommended properties
st.title('Real Estate Recommender System')
st.subheader('Recommended Properties')
if filtered_df.empty:
    st.write('No properties match your preferences.')
else:
    st.write(filtered_df)
