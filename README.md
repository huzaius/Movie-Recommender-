# Streamlit-based Recommender System

## 1) Overview

![Movie_Recommendations](resources/imgs/Image_header.png)

This repository forms the basis of an **Unsupervised learning Model** . It hosts code that deploy a  recommender engine based upon the [Streamlit](https://www.streamlit.io/) web application framework.


#### 1.1) What is a Recommender System?

[![What is an API](resources/imgs/What_is_a_recommender_system.png)](https://youtu.be/Eeg1DEeWUjA)

Recommender systems are the unsung heroes of our modern technological world. Search engines, online shopping, streaming multimedia platforms, news-feeds - all of these services depend on recommendation algorithms in order to provide users the content they want to interact with.

At a fundamental level, these systems operate using similarity, where we try to match people (users) to things (items). Two primary approaches are used in recommender systems are content-based and collaborative-based filtering.  In content-based filtering this similarity is measured between items based on their properties, while collaborative filtering uses similarities amongst users to drive recommendations.



#### 2.0) Running the recommender system locally

As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine.

To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

 1. Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
 pip install -U streamlit numpy pandas scikit-learn
 conda install -c conda-forge scikit-surprise
 ```

 2. Clone the *forked* repo to your local machine.

 ```bash
 git clone https://github.com/{your-account-name}/unsupervised-predict-streamlit-template.git
 ```  

 3. Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd unsupervised-predict-streamlit-template/
 streamlit run edsa_recommender.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```

You should also be automatically directed to the base page of your web app. This should look something like:

![Streamlit base page](resources/imgs/landing_page_sample.png)

Congratulations! You've now officially deployed your web-based recommender engine!
