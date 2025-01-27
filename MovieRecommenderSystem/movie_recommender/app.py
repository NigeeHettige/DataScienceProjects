import os
import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv

# Load API key from environment file
load_dotenv()
api_key = os.getenv("API_KEY")

# Function to fetch the movie poster from the TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            print(f"No poster_path found for movie ID {movie_id}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title("Movie Recommender System")

# Dropdown for movie selection
option = st.selectbox(
    "Select a movie you like:",
    movies['title'].values,
)

# Recommendation button
if st.button("Recommend"):
    names, posters = recommend(option)

    # Display recommendations
    col1, col2, col3, col4, col5 = st.columns(5)

    if posters[0]:
        with col1:
            st.text(names[0])
            st.image(posters[0])

    if posters[1]:
        with col2:
            st.text(names[1])
            st.image(posters[1])

    if posters[2]:
        with col3:
            st.text(names[2])
            st.image(posters[2])

    if posters[3]:
        with col4:
            st.text(names[3])
            st.image(posters[3])

    if posters[4]:
        with col5:
            st.text(names[4])
            st.image(posters[4])

    # Print movie names
    # st.write("Recommended Movies:")
    # for name in names:
    #     st.write(f"- {name}")
