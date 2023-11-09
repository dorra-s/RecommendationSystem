# Netflix Recommendation System

## Overview

This project implements a recommendation system for Netflix movies and TV shows based on user preferences. The system leverages key features such as type, directors, and actors to generate personalized recommendations using a combination of collaborative filtering and content-based filtering algorithms. The collaborative filtering aspect considers user interactions and behaviors to identify patterns and similarities among users. 

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Features](#features)
- [Similarity Calculation](#similarity-calculation)
- [Recommendation Generation](#recommendation-generation)
- [Evaluation](#evaluation)
- [User Interaction](#user-interaction)
- [Future Improvements](#future-improvements)


## Introduction

This project aims to enhance the Netflix viewing experience by providing users with personalized recommendations tailored to their preferences. The recommendation system takes into account various factors such as type, directors, and actors  to generate accurate and relevant suggestions.

## Installation

1. Clone the repository :

git clone https://github.com/dorra-s/netflix-recommendation-system.git

2. Usage :
   
To use the Netflix Recommendation System, click on this link [https://recommendationsystem-ux3zg2up9nnqygmev6lkw2.streamlit.app/].

3. Data :
   
The dataset used for this recommendation system consists of Netflix movies and TV shows. You can obtain the dataset [https://www.kaggle.com/datasets/shivamb/netflix-shows] or preprocess it based on your needs.

4. Features :
   
Key features for recommendation include genres, directors, actors, and descriptions. The system creates feature vectors to represent each item in the dataset.

5. Similarity Calculation :
   
The recommendation system uses [insert chosen similarity metric] to calculate the similarity between items based on their feature vectors.

6. Recommendation Generation :
    
Recommendations are generated using a blend of intricate algorithms tailored to your viewing preferences. The system selects the top N items with the highest similarity scores as recommendations.

7. Evaluation :
    
Evaluation metrics, such as Mean Average Precision, Recall, and Precision, are employed to assess the recommendation system's performance. The dataset is split for evaluation purposes.

8. User Interaction :
    
User interaction data is collected and utilized for personalized recommendations through a Streamlit web application. Users can interact with the system, providing explicit or implicit feedback on their preferences. This data is then used to enhance the accuracy of recommendations.

9. Future Improvements :
    
Thinknig about delving into the user's Preferences: Explore collaborative filtering techniques to fine-tune recommendations that align perfectly with his/her tastes. Uncover hidden gems based on his/her unique viewing habits.
