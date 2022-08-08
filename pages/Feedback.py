import streamlit as st


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