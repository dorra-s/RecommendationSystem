import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import streamlit as st
from PIL import Image

# Load Netflix data and preprocess
netflix_data = pd.read_csv(r'/home/dorra/Desktop/movie py/netflix_titles.csv')  
netflix_data.drop_duplicates(inplace=True)
netflix_data['director'].fillna("Unknown", inplace=True)
netflix_data['cast'].fillna("Unknown", inplace=True)
netflix_data['country'].fillna("Unknown", inplace=True)
netflix_data.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

features_to_consider = ['type', 'director', 'cast']
netflix_data[features_to_consider] = netflix_data[features_to_consider].fillna('')
netflix_data['combined_features'] = netflix_data[features_to_consider].apply(lambda row: ' '.join(row), axis=1)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(netflix_data['combined_features'])

# Building the Streamlit App
background_image_path = '/home/dorra/Desktop/movie py/netflixBACK.png'
background_image = Image.open(background_image_path)

netflix_icon_path = '/home/dorra/Desktop/movie py/netflixICON.png'  
netflix_icon = Image.open(netflix_icon_path)

st.set_page_config(page_title="Netflix", page_icon=netflix_icon, layout='wide')

st.image(background_image, use_column_width=True)

st.markdown(
    """
    <h1 style='text-align: center; font-family: "EB Garamond", serif;color :red ;font-size: 56px;'>Movie/Tv Show Recommendation</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='font-family: "Cormorant Garamond", serif;'>Select Your Preferences :</h1>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns((0.1,0.1))
with col1:
    liked_movies = st.multiselect("Select your favorite movies", netflix_data['title'])

with col2:
    favorite_type = st.multiselect("Select your favorite type", netflix_data['type'].unique())

if len(liked_movies) >= 3 and len(favorite_type) >= 1:
    selected_directors = netflix_data[netflix_data['title'].isin(liked_movies)]['director'].unique()
    selected_actors = netflix_data[netflix_data['title'].isin(liked_movies)]['cast'].unique()

    user_preferences_text = ' '.join(liked_movies + favorite_type + selected_directors.tolist() + selected_actors.tolist())
    user_profile_feature_vector = tfidf_vectorizer.transform([user_preferences_text])

    similarities = cosine_similarity(user_profile_feature_vector, tfidf_matrix)

    N = 10
    top_indices = np.argsort(similarities[0])[::-1][:N]
    recommended_movies = netflix_data.iloc[top_indices]

    
    st.subheader("Top 10 Movie Recommendations:")
    for movie in recommended_movies['title']:
         st.write(movie, unsafe_allow_html=True, key=movie)
else:
    st.info("Select at least 3 movies and at least one type to get recommendations.")
