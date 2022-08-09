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
      <li class="nav-item">
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
      <li class="nav-item active">
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

#st.markdown("""<h3 style='text-align: center; color: magenta; background: cyan; margin: 3px'>Screen Lot</h1>""", unsafe_allow_html=True)
st.markdown(""" <p style='text-align: justify >Before now, it was near impossible to process these large swaths of data in order to reveal these insights. With the developments in the field of data science and through the expertise which we seek to express, we will show how data can be processed to not only reveal the insight hidden in them but also to present the discoveries made in the process in a form that is digestible by non-technical audiences. Here at **Data Port Inc.** our team is made up of 5  professionals who excel in the fields of Business Management, marketing and promotions, technical data science, IT communications, and Administration.</p>""",unsafe_allow_html=True)
st.write("Data collection and analysis are increasingly becoming very useful in industries and economies worldwide. With advances in science and technology (particularly information technology), we are in an age where an astounding quantity of data in many different forms is generated every second. This data usually has hidden insights on trends, habits, developments, changes, etc that may not be immediately identified, but are very valuable to companies and other entities for the purpose of making informed decisions.")
st.write("Before now, it was near impossible to process these large swaths of data in order to reveal these insights. With the developments in the field of data science and through the expertise which we seek to express, we will show how data can be processed to not only reveal the insight hidden in them but also to present the discoveries made in the process in a form that is digestible by non-technical audiences.")
#st.write('Before now, it was near impossible to process these large swaths of data in order to reveal these insights. With the developments in the field of data science and through the expertise which we seek to express, we will show how data can be processed to not only reveal the insight hidden in them but also to present the discoveries made in the process in a form that is digestible by non-technical audiences. Our team is made up of 5  professionals who excel in the fields of Business Management, marketing and promotions, technical data science, IT communications, and Administration. Please refer to this link to access the full profiles of all team members.')
st.markdown(f'''Having been given a sourced and clean data set, (the MovieLens dataset) which has been pre-enriched with additional data, and resampled for fair evaluation purposes, We have a task to use this raw data to build a Recommendation system algorithm (Screen lot) based on content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed, based on their historical preferences. The idea of this algorithm is to predict the movies that would be enjoyed by a viewer based on their reactions to the movies that they have already watched. For more information on how Screenlot works and the technical details of the App, please check out the ***documentation*** page.''')



st.image('resources/imgs/Huzaius.png',caption='Huzaifa Abu')
with st.expander("View Profile"):
    st.write('Huzaifa Abu is  the Tech lead at Data port Inc. He is skilled in Server and Database Administration with strong skills in python,sql (T-SQL,Oracle etc.), Visualizations like PowerBI and Tableau and design and implementation of ML models. I enjoy swimming , playing football and making friends at my leasure time.')