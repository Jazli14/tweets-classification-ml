# Scraping and Classifying Sports Tweets
Our project attempted to scrape sports tweets and classify tweets based on their sport through training a classification model.

## Scraping Tweets
After signing up for access to the Twitter API and generating user access tokens to utilize the API. We scraped over 2000 tweets that were related to the following sports: basketball 🏀 , soccer ⚽️ , American football 🏈 , baseball ⚾️ and hockey 🏒 via the context stream method in the API. This data is then stored into the SportsTweets.json.

##  Data Preprocessing
Once the data is gathered, it needs to be put through preprocessing before the model is trained. 

### Data Wrangling - Sport Classification 
To identify the sport, the data needed to be wrangled in order to classify the tweet. Using the context_annotations field from the json, each tweet was assigned a sport. SportClassification.py handled this.

### Data Cleaning
Features “Tweet”, “Name” and “Sport” were extracted from the json file and then the data was then converted to a csv file using the converter.py.
To clean the tweets, tweet_csv_cleaner.ipynb was used to remove @ handles, hashtags, urls etc.

## Model Training
Each label from the feature “Sport” was encoded. Since the data that will read by the model are strings, it will need to use Natural Language Processing or NLP where we used scikit-learn and its TF-IDF vectorizer.

### Model Selection
We split the model on an 80-20% split for training and testing data. 
After splitting the data, cross validation for the training set is performed on five models.
The best performing model was the Random Forest classification model.

### Training the Model
Once the Random Forest model was selected,   the hyperparameters were tuned to achieve the highest accuracy.
Using this classifier, it was trained on the 80% training set and tested with the 20% testing set.

### Results
The results were an achievement of an overall accuracy of 89%, a macro average of 87% and a weighted average of 88%.
![image](/resources/results_report.png)
