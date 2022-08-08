from turtle import st
import streamlit as st

st.title('Documentation')
        
st.header("Overview")
st.write("In order to maximize profit and  guarantee a personalized experience for customers, we have built a movie recommendation app that iterates through a viewer's previous viewing preferences and movie viewer ratings and uses the information contained therein to predict what unseen movie the viewer is likely to enjoy. most online content providers rely on recommendation systems such as this to maximally exploit the long tail. The long tail is a business strategy that allows companies to realize significant profits by selling low volumes of hard-to-find items to many customers, instead of only selling large volumes of a reduced number of popular items (For more on long tail, please click [*here*](https://medium.com/@kyasar.mail/recommender-systems-what-long-tail-tells-91680f10a5b2)).")
st.image('https://media.wired.com/photos/5a5957cf2bbf59566d73366b/master/w_1600%2Cc_limit/FF_170_tail6_f.gif',caption='Long Tail')
st.write("Our recommendation system allows the client to achieve this by actively recommending products based on the app's built-in algorithm rather than relying on the customers to scan through potentially millions of options in order to find these products themselves. A broad base of consumer sentiment, spanning multiple demographic and geographic categories is used as input to train the algorithm, hence increasing the accuracy of the app, and providing sound insights that convert into sound matches as regards movies that unique viewers are likely to enjoy. ")


st.subheader('Featured  Recommendation Engines')
st.write("Of the three main types of recommendation engines that exist, Our app features two main recommendation engines as detailed below.")

st.subheader("Collaborative filtering")  
st.write("Collaborative filtering focuses on collecting and analyzing data on user behavior, activities, and preferences, to predict what a person will like, based on their similarity to other users. To plot and calculate these similarities, collaborative filtering uses a matrix-style formula. An advantage of collaborative filtering is that it doesn’t need to analyze or understand the content (products, films, books). It simply picks items to recommend based on what they know about the user.")

st.subheader("Content-based filtering")
st.write("Content-based filtering works on the principle that if you like a particular item, you will also like this other item. To make recommendations, algorithms use a profile of the customer’s preferences and a description of an item (genre, product type, color, word length etc) to work out the similarity of items using cosine and Euclidean distances. The downside of content-based filtering is that the system is limited to recommending products or content similar to what the person is already buying or using. It can’t go beyond this to recommend other types of products or content. For example, it couldn’t recommend products beyond")

st.subheader("Data Details")
st.write("This dataset consists of several million 5-star ratings obtained from users of the online [MovieLens](http://movielens.org/) movie recommendation service. The MovieLens dataset has long been used by the industry. For this project, we'll be using a special version of the MovieLens dataset which has been enriched with additional data and resampled for fair evaluation purposes. The data for the MovieLens dataset is maintained by the [GroupLens](http://grouplens.org/) research group in the Department of Computer Science and Engineering at the University of Minnesota. Additional movie content data was legally scraped from [IMDB](https://www.imdb.com/).")

st.subheader("Model performance")
st.write("The evaluation metric for this competition is [Root Mean Square Error](https://surprise.readthedocs.io/en/stable/accuracy.html). Root Mean Square Error (RMSE) is commonly used in regression analysis and forecasting and measures the standard deviation of the residuals arising between predicted and actual observed values for a modeling process. For our task of generating user movie ratings via recommendation algorithms, the formula is given by:")
st.image("resources/imgs/rsme.jpg",caption="Root Mean Squared Error")
st.write('''Where R is the total number of recommendations generated for users and movies, with $r_{ui} $ and $\hat{r_{ui}}$ being the true, and predicted ratings for user ***u*** watching movie ***i***, respectively.''')
