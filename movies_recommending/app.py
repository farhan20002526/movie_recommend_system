import streamlit as st 
import pickle
import pandas as pd

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('D:\python\movies_recommending\similarity.pkl','rb'))

def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    for i, score in movies_list:
        movie_id= i[0]
        recommend_movies.append(movies.iloc[i]['title'])
    return recommend_movies


st.title("Movie Recommender System")

Selected_movies=st.selectbox("How would you like to be contacted?",movies["title"].values)

if st.button("Recommend"):
    recommendation=recommend(Selected_movies)
    for i in recommendation:
        st.write(i)