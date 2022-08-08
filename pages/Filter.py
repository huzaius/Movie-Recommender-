import streamlit as st
import pandas as pd
from eda.mymodules import *


train_df = pd.read_csv('resources/data/train.csv')
eda_df = train_df[train_df['userId']!=72315]
mov_df = pd.read_csv('resources/data/movies.csv')
rate_df = pd.read_csv('resources/data/ratings.csv')



#movie and rating dataframe 

movie_rating_df = pd.merge(left=mov_df,right=rate_df,how='inner',left_on='movieId',right_on='movieId')
movie_rating_df.drop(['movieId','timestamp','userId'],axis=1,inplace=True)
#delete dataframes to save memory

del rate_df


gp_mov = movie_rating_df.groupby(by=['title','genres']).mean()

gp_mov.reset_index(inplace=True)
pattern = '\((\d{4})\)'
gp_mov['year'] = gp_mov.title.str.extract(pattern,expand=False).fillna(2016).astype('int64')

#Showing dataframe
st.subheader('Movie Dataset')

if st.checkbox('Filter Dataset'):

    message = 'Move sliders to filter dataframe'
    year_slide = ''
    slider_1, slider_2 = st.slider('%s' % (message),0,len(gp_mov[:1000])-1,[0,len(gp_mov[:1000])-1],1)
    yslider_1,y_slider_2 = st.slider('%s' % (message),1900,2020,(1902,2016))
    
    st.success('Starts from {} to {} '.format(slider_1,slider_2))
    
    st.dataframe(gp_mov.loc[slider_1:slider_2])
    st.write(download_csv('Filtered Data Frame',gp_mov.iloc[:][slider_1:slider_2]),unsafe_allow_html=True)
    
    

#Searching movie  with Details
if st.checkbox('Show movie details'):
    movie_title = gp_mov.title.unique()
    st.write(movie_title.shape)
    movie_sel = st.selectbox('Select a Movie',movie_title)
    
    if (movie_sel in movie_title):
        selected_movie = gp_mov[gp_mov.title == movie_sel]
        df_columns = {'Title':[movie_sel],
                        'Year': selected_movie.year,
                        'Genre':[selected_movie.genres.unique()[0]],
                        'Highest Rating':[round(selected_movie.rating.max(),1)],
                        'Lowest Ratings':[round(selected_movie.rating.min(),1)],
                        'Average Rating':[round(selected_movie.rating.mean(),1)],
                        'User Review':[selected_movie.shape[0]]}

        st.dataframe(df_columns)    
        st.success('{} has been rated {} time(s) with an average IMDB rating  of {}'.format(movie_sel,selected_movie.shape[0],round(selected_movie.rating.mean(),2)))

    else:
        st.warning('Movie not present in database')

#Movies by Genre
if st.checkbox('Show movies by Genre'):
    
    genres = genre_extractor(movie_rating_df,'genres')
    genres_sel = st.selectbox('Search movies by Genre',genres[1:])

    if genres_sel in genres:
        gp_mov['genres_clean'] = gp_mov.genres.apply(lambda x: ' '.join(x.split('|')))
        gp_mov['genreclass'] = gp_mov.genres_clean.str.find(genres_sel)
        st.dataframe(gp_mov[gp_mov.genreclass >=0][['title','genres','rating','year']])
        gp_mov.drop(['genres_clean','genreclass'],inplace=True,axis=1)


# Displaying charts

if st.checkbox('User Rating'):

    ratings_selected = st.selectbox('Select a type of rating',['Count Plot','Mean Plot','Distplot','Plot Rating'])
    if ratings_selected == 'Count Plot':

        user_count = st.number_input('Insert a number',min_value=3,max_value=20,value=8,step=1,key='user_count')
        user_ratings_count(eda_df,int(user_count))
        
    elif ratings_selected == 'Mean Plot':
        color_pic = st.color_picker('Pick a color','#4D17A0')
        mean_ratings_scatter(eda_df,color=color_pic)
        
    elif ratings_selected == 'Distplot':
        st.image('resources/imgs/displot.png')

    
    elif ratings_selected == 'Plot Rating':
        st.image('resources/imgs/plot_rating.png')