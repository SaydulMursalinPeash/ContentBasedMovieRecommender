import streamlit as st
import pickle
import pandas as pd

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
movie_list=movies['title'].values

sim=pickle.load(open('sim.pkl','rb'))


def recom(movie):
    movie_i=movies[movies['title']==movie].index[0]
    distance=sim[movie_i]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    n=[]
    for i in movie_list:
        n.append(movies.iloc[i[0]].title)
    return n


st.title("Movie Recommender")
option = st.selectbox(
    'Choose Movie:',
    movie_list)

if st.button('Recommend'):
    l=recom(option)
    for i in l:
        st.write(i)

    