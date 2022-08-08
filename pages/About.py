import streamlit as st
        
st.markdown("""<h3 style='text-align: center; color: magenta; background: cyan; margin: 3px'>Screen Lot</h1>""", unsafe_allow_html=True)
st.markdown(""" <p style='text-align: justify >Before now, it was near impossible to process these large swaths of data in order to reveal these insights. With the developments in the field of data science and through the expertise which we seek to express, we will show how data can be processed to not only reveal the insight hidden in them but also to present the discoveries made in the process in a form that is digestible by non-technical audiences. Here at **Data Port Inc.** our team is made up of 5  professionals who excel in the fields of Business Management, marketing and promotions, technical data science, IT communications, and Administration.</p>""",unsafe_allow_html=True)
st.write("Data collection and analysis are increasingly becoming very useful in industries and economies worldwide. With advances in science and technology (particularly information technology), we are in an age where an astounding quantity of data in many different forms is generated every second. This data usually has hidden insights on trends, habits, developments, changes, etc that may not be immediately identified, but are very valuable to companies and other entities for the purpose of making informed decisions.")
st.write("Before now, it was near impossible to process these large swaths of data in order to reveal these insights. With the developments in the field of data science and through the expertise which we seek to express, we will show how data can be processed to not only reveal the insight hidden in them but also to present the discoveries made in the process in a form that is digestible by non-technical audiences. Here at **Data Port Inc.** our team is made up of 5  professionals who excel in the fields of Business Management, marketing and promotions, technical data science, IT communications, and Administration. ")
#st.write('Before now, it was near impossible to process these large swaths of data in order to reveal these insights. With the developments in the field of data science and through the expertise which we seek to express, we will show how data can be processed to not only reveal the insight hidden in them but also to present the discoveries made in the process in a form that is digestible by non-technical audiences. Our team is made up of 5  professionals who excel in the fields of Business Management, marketing and promotions, technical data science, IT communications, and Administration. Please refer to this link to access the full profiles of all team members.')

from PIL import Image
prince,huzaifa = st.columns(2)

dan,jerry,izu =  st.columns(3)

dan_img = Image.open('resources/imgs/Daniel.png')
jerry_img = Image.open('resources/imgs/Jerry.png')
huzaifa_img = Image.open('resources/imgs/Huzaius.png')
prince_img = Image.open('resources/imgs/Prince.png')
izu_img = Image.open('resources/imgs/Izunna.png')

with prince:
    st.image(prince_img,caption='Prince Okon- Team lead')
    with st.expander("View Profile"):
        st.write('Okon Prince is the team lead of Data port Inc. He is a Data scientist with years of experience in Data sourcing, data management, and model building / Optimization. He has participated in several open competitions in model building and emerged at the top range of a number of them. He is versed in the design and creation of functional models that aim to solve real-life problems.')
        st.write('With a sound background in the Python programing language, expert-level skills in SQL, and a wealth of soft skills gathered from years of experience working both as a private consultant and in teams in both the private and public sectors, he processes the requisite skills required to lead any world-class organization in his field.')
        st.write('Screenlot is one of many ML products whose development he has led and the quality of these ML  products and the consistency with which they are updated testifies to the competence of the teams he led to build them')

with huzaifa:
    st.image(huzaifa_img,caption='Huzaifa Abu - Technical Lead')
    with st.expander("View Profile"):
        st.write('Huzaifa Abu is  the Tech lead at Data port Inc. He is skilled in Server and Database Administration with strong skills in python,sql (T-SQL,Oracle etc.), Visualizations like PowerBI and Tableau and design and implementation of ML models. I enjoy swimming , playing football and making friends at my leasure time. ')

with dan:
    st.image(dan_img,caption='Odukoya Daniel - Administrator')
    with st.expander("View Profile"):
        st.write(' Odukoya Adewale Daniel is the Administrator of Data port inc. He is a progressive minded fellow who has proven to be effective and collaborative with strong team-building  talents. I enjoy collective brainstorming sessions which all me to coordinate activities to achieve a common goal.')

with jerry:
    st.image(jerry_img,caption='Jerry Iriri - Chief Designer')
    with st.expander("View Profile"):
        st.write('Iriri Jerry is a Data Scientist at Data Port Inc, specialized in system design, database administration, Development, and cloud-based services. When I\'m not working, I like to read psychology and listen to music. I am a voracious reader who loves to travel and meet new people.')

with izu:
    st.image(izu_img,caption='Izunna Eneude - Quality Control')
    with st.expander("View Profile"):
        st.write('Izunna Eneude is the Quality Control Lead of Data port Inc., a unique data scientist with an innate drive for continuous learning and improvement. Coming from a quality control perspective and the mantra that there is always room for improvement, he strives through effective collaborations to deliver solutions such as the Screenlot App. Over time he has built up relevant skills and use of tools including PowerBi, Python and SQL. He is a telecom expert who loves reading, poetry and mixed martial arts.')
        

    
