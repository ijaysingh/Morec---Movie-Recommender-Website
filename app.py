import streamlit as st
import pickle
import pandas as pd
import requests

def fetchPoster(movieId):
    # api key = 2aa77818d02727e64938dbb44051164e
    # api url = https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
    url = "https://api.themoviedb.org/3/movie/" + str(movieId) + "?api_key=2aa77818d02727e64938dbb44051164e&language=en-US"
    res = requests.get(url)
    data = res.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieIndex]
    movieList = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommendedMovies = []
    recommendedMoviesPoster = []
    for item in movieList:
        movieId = movies.iloc[item[0]].movie_id
        recommendedMovies.append(movies.iloc[item[0]].title)
        # fetch poster from api
        recommendedMoviesPoster.append(fetchPoster(movieId))
    return recommendedMovies, recommendedMoviesPoster

movieDict = pickle.load(open('movieDict.pkl', 'rb'))
movies = pd.DataFrame(movieDict)
st.title("Morec - A Movie Recommendor")

similarity = pickle.load(open('similarity.pkl', 'rb'))

selectedMovie = st.selectbox(
'Select your movie', movies['title'].values)

if st.button('Recommend'):
    names, poster = recommend(selectedMovie)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
        
    with col4:
        st.text(names[3])
        st.image(poster[3])
        
    with col5:
        st.text(names[4])
        st.image(poster[4])

        # 77


