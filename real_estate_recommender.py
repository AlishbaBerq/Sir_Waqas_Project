# Install required libraries
!pip install streamlit

# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load real estate data (example)
data = {
    'Property': ['House A', 'House B', 'House C', 'House D'],
    'Description': ['Beautiful house in downtown.', 'Cozy apartment with a garden.', 'Spacious villa with pool.', 'Modern loft in the city center.']
}

df = pd.DataFrame(data)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])

# Calculate similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend properties
def recommend_property(property_name, cosine_sim=cosine_sim):
    idx = df[df['Property'] == property_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get the top 3 similar properties
    
    property_indices = [i[0] for i in sim_scores]
    return df['Property'].iloc[property_indices]

# Streamlit UI
st.title('Real Estate Recommendation System')

property_name = st.selectbox('Select a property:', df['Property'])

if st.button('Find Similar Properties'):
    recommendations = recommend_property(property_name)
    st.write(recommendations)
