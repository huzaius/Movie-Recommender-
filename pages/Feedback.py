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
      <li class="nav-item active">
        <a class="nav-link" href="Feedback" target="_self">Feedback</a>
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



 #st.session_state;
with st.container():
    
    name = st.text_input('Name')
    mail = st.text_input('Email')
    phone = st.text_input('Phone Number')
    
    #radio buttons
    feed_radio = st.radio('Select an option',('Feedback','Contact Us','Other'),key='radio_option')         
    
    if feed_radio == 'Other':
        subject = st.text_input('Subject') 
    
    message = st.text_area('Message')
    
    if st.button('Submit'):
        if feed_radio == "Feedback":
            st.success('Thank you for your {}'.format(feed_radio))

        elif feed_radio == 'Contact Us':
            st.success('Thank you for contacting us')

        else:
            st.success('Thank you, Your {} has been logged'.format(subject))