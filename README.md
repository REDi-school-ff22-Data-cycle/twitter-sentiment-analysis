Twitter Sentiment Analysis Climate Change

Data Circle Course - ReDI School Berlin 
Fall 2022

By Charles Emeka Onyi & Lucía Morales Lizárraga
Supervised by Nishtha Jain & Benjamin Feifke

Challenge and data adquired from: https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset?datasetId=413654

This repository contains the following files: 
  1. csv file with tweets. This dataset aggregates tweets pertaining to climate change collected between Apr 27, 2015 and Feb 21, 2018. In total, 43943 tweets were annotated. Each tweet is labelled independently by 3 reviewers. This dataset only contains tweets that all 3 reviewers agreed on (the rest were discarded).
  2. Colabfile of our work, codes and results for this project. 
  3. Pptx presentation of our project for the midterm demoday. 

About the sentiments on the tweets: 
Each tweet is labelled as one of the following classes:
 2(News): the tweet links to factual news about climate change
 1(Pro): the tweet supports the belief of man-made climate change
 0(Neutral: the tweet neither supports nor refutes the belief of man-made climate change
 -1(Anti): the tweet does not believe in man-made climate change


Outline of the project:
1. Create a code that loads and processes the data
2. Explore the dataset
3. Tweets preprosessing techniques
4. Prediction Models:
  4.1 Linear Regression
  
  4.2 Naive Bayes Classifier
  
  4.3 Random Forest Classifier
  
  4.4 K Nearest Neighbors Classification
  
5. Feature Engeneering Techniques
  5.1 Classification
  5.2 Oversampling


Phase 2: Productionize:  

- Deploy the model in FastAPI (run the model locally)
- Run the app in Heroku (28.11.22, no more free version). 
