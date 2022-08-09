import streamlit as st


#Page Aestheticization
st.set_page_config(initial_sidebar_state='collapsed',
                    layout='centered',
                    menu_items=None)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
# <a class="navbar-brand" href="#">Navbar</a>
st.markdown("""
<nav class="navbar navbar-expand-lg navbar-dark " style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://huzaius.github.io" target="_blank">Huzaifa</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item ">
        <a class="nav-link" href="Home" target="_self">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="EDA" target="_self">EDA</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="Filter" target="_self">Filter</a>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="Feedback" target="_self">Feedback</a>
      </li>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="Documentation" target="_self">Documentation</a>
      </li>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="About" target="_self">About</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown("""
<style>
 .css-1k0ckh2{
        visibility:hidden
    }

</style>
""", unsafe_allow_html=True)



st.header('Exploratory Data Analysis')
st.write('Exploratory Data Analysis shows the distribution of the Data used in the creation of the recommender system model. This distributions are available after the cleaning and the preprocessing of the data. The graphs below shows the various distribution plots gained after cleaning the data.')

st.image('resources/imgs/movie_release_year.png')
st.info('This shows the movie ratings going back to the 1950\'s./n A significant increase in movie prodution was perceived from 1990 to 2000') 

st.subheader('Rating Distribution Charts')
st.image('resources/imgs/movie rating dist.png')
st.info('Show the distribution of movies in relation to their ratings.') 
st.image('resources/imgs/users_per_rating.png')
st.info('This shows that a significant number of movies are rated between 3 and 4, with the largest number being 4. Conversely, we can say that a good number of movies produced are of good quality.') 
st.image('resources/imgs/shawshank_rating.png')
st.info('Amongs all the higest rated movies, Shawshank redemption was the highest rated.') 

st.subheader('Genre Distribution Charts ')
st.image('resources/imgs/movies per genres.png') 
st.success('The graph shows 19 distinct genres with majority of the movies being Drama with 23 percent for all movies. Comedy was the second count for genres with thriller being the third.')
st.image('resources/imgs/mean rating per enre.png') 
st.success('The highest average ratings is documentaries, while the lowest user mean ratings are  horror movies.The ratings are almost evenly distributed With the exception of Documentaries, War, Drama, Musicals, and Romance and Thriller, Action, Sci-Fi, and Horror, which score above average and significantly below average.')

st.subheader('Director Distribution Charts ')
st.write('A film director is in charge of the artistic and dramatic aspects of a film, as well as visualizing the screenplay and directing the technical crew and actors in carrying out that vision. The director is responsible for casting, production design, and all creative aspects of filmmaking.')
st.image('resources/imgs/movies per director.png') 
st.success('Illustrates the distribution of Directors') 
st.image('resources/imgs/mean rating per director.png')
st.image('resources/imgs/mean rating per director2.png')
st.info('Unsurprisingly, Stephen King and Quentin Tarantino are at the top of the list. The directors with the lowest ratings is Charles Robert Band is well-known for his work on horror comedies which score the least based on user ratings.') 

st.subheader('Word Clouds')
st.write('Word cloud shows the prequently used words in the data.')
st.image('resources/imgs/wordcloud.png')
st.success('We can get a good idea of the most common themes in movies from these wordclouds. Keywords like sex, nudity, woman, and murder are common. This is because sex and murder seem to be present in the majority of movies, regardless of their genre.')
st.image('resources/imgs/wordcloud2.png')
st.success('The most frequent word in movie titles is "love." Among the words that appear the most frequently are Girl, Night,Life, and Man. This, in my opinion, pretty effectively captures the notion of romance\'s prevalance in movies.')

st.image('resources/imgs/3d distribution.png') 
st.success('Show are 3D scatter plot')
st.image('resources/imgs/boxplot of scaleed features.png') 

st.image('resources/imgs/boxplot of unscaleed features.png') 

