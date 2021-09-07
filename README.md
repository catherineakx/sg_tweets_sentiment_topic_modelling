# Capstone Project: Life in the "New Normal"

##### By: Catherine Ang

---

### Background
It has been more than a year since the COVID-19 pandemic started. The Ministry of Health (MOH) announced the first imported case of "novel coronavirus" infection in Singapore on 23 January 2020 (source: [Yong, Jan 2021](https://www.channelnewsasia.com/singapore/covid-19-pandemic-singapore-one-year-on-coronavirus-419301)). Since then, there have been changes to several aspects of the country, such as the economy, working lifestyle and social fabric. In a bid to curb the rising number of confirmed COVID-19 cases in the community, some measures introduced by the government of Singapore include: 

* Travel restrictions, i.e. unable to travel overseas for leisure.
* Going into isolation, i.e. circuit breaker, Phases 1 and 2 where dining in at coffee shops/restaurants is not allowed.
* Working from home and online home-based learning.
* Rollout of COVID-19 vaccinations.

In the same timeframe, an increasing number of people in Singapore has sought help for mental health issues (source: [Ang & Phua, Apr 2020](https://www.channelnewsasia.com/singapore/covid-19-fear-toll-mental-health-hotline-anxiety-singapore-763336)). Concerns over the rising number of COVID-19 cases in the community, loss of employment, reduction in income, burnout from work, separation from loved ones, etc. have resulted in some feeling more anxious and uneasy. Concurrently, there are other groups of people who are seemingly unaffected by the COVID-19 pandemic – life goes on normally for them, with great work-life balance and indulging in luxurious experiences (source: [Warren, Mar 2021](https://www.insider.com/singapore-rich-spending-travel-luxury-hotels-pandemic-2021-3)).

---

### Problem Statement
With social media becoming more prevalent in our daily lives, more and more people are turning to social media to share about their lives and express their opinions. While there have been studies on how people are reacting to COVID-19 at the height of the pandemic, there is limited understanding on how people in Singapore are adapting to life in the "new normal" – a pandemic-filled era.

Therefore, this project aims to leverage on tweets in Singapore from 1 January 2021 to 31 July 2021, to achieve the following objectives:
* What is the sentiment expressed in Singapore tweets?  
* What are the common topics of discussion on Twitter?
* How have the sentiments and topics of discussion changed over the past seven months in Singapore? 
* What can the government of Singapore do to help members of the public to better cope with the pandemic?

---

### Executive Summary

*INTRODUCTION*
When the first COVID-19 case in Singapore was announced on 23 January 2020, most people expected the COVID-19 pandemic to last for a couple of months, given its resemblance to the SARS (Severe Acute Respiratory Syndrome) virus outbreak in 2003. Fast forward to July 2021, the media is still reporting new COVID-19 cases in the community as well as new variants of COVID-19, constantly reminding us to take precaution when carrying out our day-to-day activities. 

With our lives becoming more intertwined with social media (where we are openly expressing our opinions on online platforms to people whom we have never met before), I'm keen to understand how people are reacting and adapting to life in the "new normal". The social media site that will be explored in this project is Twitter, which is a 'microblogging' platform that allows users to send and receive short posts (usually less than 280 characters) called tweets (source: [UKRI, Aug 2021](https://www.ukri.org/councils/esrc/impact-toolkit-for-economic-and-social-sciences/how-to-use-social-media/choosing-what-social-media-you-use/)).

*METHODOLOGY*
A data science workflow was introduced to conduct this analysis. Firstly, the problem statement was defined — I would like to understand the sentiment expressed in Singapore tweets, the common topics of discussion, how these aspects changed over the past seven months and what the government of Singapore could do to help members of the public better cope with the pandemic. 

Next, tweets from 1 January 2021 to 31 July 2021 located near Singapore were extracted via webscraping using Twint API. An exploratory data analysis was conducted to understand the distribution of the tweets over the seven months as well as any patterns and trends associated with the number of likes, replies, retweets, mentions, hashtags, etc. New features such as the character length and word count of the tweets were engineered, and relationships were visualized with a series of bar charts, histograms and boxplots. Commonly occurring one-word, two-word and three-word phrases were also identified and visualized using bar charts and word cloud.

To conduct a sentiment analysis for determining the sentiment of the tweets, Natural Language Processing (NLP) techniques and various packages were utilised, such as VADER (Valence Aware Dictionary for sEntiment Reasoning), TextBlob and a pre-trained Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) model. As the tweets were unlabelled, VADER and TextBlob could be employed to predict the tweets' sentiment without any training data. For LSTM RNN, it was slightly trickier as the model was first trained on labelled tweets from Sentiment140 (source: [Sentiment140, 2021](http://help.sentiment140.com/for-students)) and obtained an accuracy score of 79.6%. The model was then used to predict the sentiment for Singapore tweets in the odd months (January, March, May and July), in which a new LSTM RNN model was created from these predictions and achieved a higher accuracy score of 86.4%. This new model was then employed in the prediction of the sentiment for Singapore tweets in the even months (February, April and June). 

For topic modelling, Latent Dirichlet Allocation (LDA) from Gensim was employed to identify the optimal number of topics from the tweets and contents surrounding them, to understand the commonly discussed pointers on Twitter. Relationships between the topics and their keywords, as well as between the topics and their sentiment, were visualized. Concurrently, external research about announcements and events that occurred in Singapore and notable events around the world in the past seven months was carried out, to understand factors that could have affected the sentiment labels. 
Last but not the least, a dashboard featuring some of the visualizations was created using Plotly and Dash, allowing for easier reference to trends, sentiment and topics of Singapore tweets from January to July 2021. 

*FINDINGS*
In the first seven months of 2021, it can be observed that overall, the proportion of positive tweets (64.9%) is close to 2x that of negative tweets (35.1%). This indicates that despite the prevalence of COVID-19 virus and various social issues, the community seems to have remained positive.

As for the dominant topics present in the tweets, they include discussions related to COVID-19 cases, clusters and vaccinations, recreational activities in Singapore, military coup in Myanmar, and even political affairs in the United States of America.

---

### Contents

There are a total of five main notebooks in this project, namely:
1. Problem Statement & Webscraping
2. Data Cleaning & Exploratory Data Analysis
3. Preprocessing & Modelling (consists of Part 1: Preprocessing & Sentiment Analysis, and Part 2: Building Pre-trained LSTM RNN Model for Sentiment Analysis)
4. Topic Modelling & Conclusion
5. Plotly & Dash Visualization

---

### Data Dictionary & Datasets

| Feature | Type | Dataset | Description  |
|:--------|:----:|:-------:|:-------------|
|id|integer|all tweets datasets|id of each tweet
|date|object|all tweets datasets|date and time each tweet is created
|tweet|object|all tweets datasets|content of each tweet 
|language|object|all tweets datasets|language of the tweet 
|hashtags|object|all tweets datasets|hashtags present in each tweet 
|user_id|integer|all tweets datasets|user id of each Twitter user
|username|object|all tweets datasets|username of each Twitter user
|nlikes|integer|all tweets datasets|number of likes that each tweet receives
|nreplies|integer|all tweets datasets|number of replies that each tweet receives
|nretweets|integer|all tweets datasets|number of retweets that each tweet receives
|near|object|all tweets datasets|location detected from each tweet posting

Note: 'all tweets datasets' refers to the following datasets used in this analysis:*
* [sg_tweets_jan_2021.csv](../datasets/sg_tweets_jan_2021.csv) — Singapore tweets in January 2021
* [sg_tweets_feb_2021.csv](../datasets/sg_tweets_feb_2021.csv) — Singapore tweets in February 2021
* [sg_tweets_mar_2021.csv](../datasets/sg_tweets_mar_2021.csv) — Singapore tweets in March 2021
* [sg_tweets_apr_2021.csv](../datasets/sg_tweets_apr_2021.csv) — Singapore tweets in April 2021
* [sg_tweets_may_2021.csv](../datasets/sg_tweets_may_2021.csv) — Singapore tweets in May 2021
* [sg_tweets_jun_2021.csv](../datasets/sg_tweets_jun_2021.csv) — Singapore tweets in June 2021
* [sg_tweets_jul_2021.csv](../datasets/sg_tweets_jul_2021.csv) — Singapore tweets in July 2021

---

### Conclusion & Recommendations

From the Sentiment Analysis, it can be observed that 64.9% of the tweets (close to two thirds) have positive sentiment, whereas the remaining 35.1% of them (slightly more than one third) have negative sentiment. This seems to indicate that people are generally positive about adapting to life in the "new normal", as the proportion of positive to negative sentiment for tweets remains relatively consistent over the first seven months in 2021.

For Topic Modelling, it has highlighted the dominant topics that people are discussing frequently on Twitter, from matters in Singapore such as the COVID-19 cases, clusters, vaccinations and new restrictions imposed by the government of Singapore to curb of the spread of COVID-19 cases in the community, to global issues such as the political affairs in the United States of America and military coup in Myanmar. Definitely, there are also topics related to day-to-day life, such as recreational places to explore, food places to visit, results from the Premier League games and even latest celebrity news. 

When comparing the sentiment to the dominant topics, it can be observed that the polarity scores vary from topic to topic, indicating the importance to analyse the sentiment for each topic for obtaining a thorough understanding of the tweets. For instance, topics which have more positive sentiment are related to how people are looking forward to participating in recreational activities such as exploring nature and food places, going on staycations, etc. in spite of the COVID-19 pandemic. On the other hand, topics with more negative sentiment seem to be stemming from tweets related to global events such as the military coup in Myanmar and political affairs in the United States of America, which have the potential to disrupt worldwide peace and security. 

Essentially, this serves as feedback for the government of Singapore to consider when introducing new measures or policies, such as: 

* **For implementation in Singapore:**
    * Ensuring timely and concise communication about new COVID-19 cases and clusters outbreak in Singapore, without inducing further anxiety and fear.
    * Easing COVID-19 restrictions imposed in the country whenever the situation permits, so that people are able to engage in activities which can boost their emotional health while abiding by the measures. 
    * Providing a range of resources, i.e. financial help, social support helplines, etc. to help people who may be struggling during the pandemic.

* **For handling global affairs:** 
    * Providing humanitarian aid for people affected in the military coup in Myanmar.
    * Partaking in discussions with global leaders to resolve issues surrounding humanity.

---

### Limitations & Further Explorations

Some of the **limitations** for this project include: 
* As there is a lack of labelled tweets from Singapore online, I have utilised labelled tweets from Sentiment140, which may not be the most appropriate for predicting the sentiment of tweets in Singapore, as it does not take into consideration special words and slangs used by the local, i.e. Singlish. 
    * Besides, the labelled tweets only consist of positive and negative sentiment labels – tweets that are neutral in sentiment may be incorrectly classified as positive and negative.

Moving forward, these are some of the **exploration opportunities**:
* Building a pre-trained LSTM RNN model for Sentiment Analysis with all 1,600,000 labelled tweets from Sentiment140, and with hypertuning the parameters used in the model. 
* Conducting an Emotion Recognition Analysis, using a pre-trained emotion recognition RNN model from Colnerič & Demšar (source: [Colnerič & Demšar, 2018](https://github.com/nikicc/twitter-emotion-recognition)), to prediction emotions from the tweets. The six emotions that can be classified include anger, disgust, fear, joy, sadness and surprise.
* Understanding the correlation between the hashtags used in the tweets and the corresponding sentiment and emotion.
* Correlating the COVID-19 cases/death and COVID-19 vaccination status in Singapore with this analysis to monitor how attitudes are changing overtime. 
* Creating a Twitter user network analysis to identify Twitter users who are more influential in driving the topics of discussion on Twitter. 
* Expanding the datasets to include texts from other social media platforms such as Facebook and Reddit. 

---

### Python Library Used
* Pandas
* Numpy
* Seaborn
* Matplotlib
* Sklearn
* Twint
* Datetime
* Word Cloud
* NLTK
* Tensorflow
* Gensim
* pyLDAvis
* Plotly
* Dash