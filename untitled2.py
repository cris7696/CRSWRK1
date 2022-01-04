# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YofM1cjC-SlHxdJxP84z2BGtFeuhfX3p
"""

# Commented out IPython magic to ensure Python compatibility.
 #  Import library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

final_data = pd.read_csv('bbc22.csv')
final_data.head()

"""<hr>

### **Merge the Dataset**
"""

final_data.tail()

# Information about the data
final_data.info()

# Check the shape of final data
final_data.shape

# check the Screen Name of Twitter user
final_data['screenname'].unique()

# check the ID of Twitter user
final_data['ID'].unique()

# #  Need only @AmericanAir Tweet

final_data = final_data[final_data['ID'] == '@BBC']

# Change the True / False to 1/0
final_data["Video"] = final_data["Video"].astype(int)

final_data["retweeted"] = final_data["retweeted"].astype(int)

final_data["pinned"] = final_data["pinned"].apply(bool)

final_data["pinned"] = final_data["pinned"].astype(int)

final_data['replies'].unique()

# Change the 1K to 1000 and 1m 
#final_data.likes = (final_data.likes.replace(r'[KM]+$', '', regex=True).astype(float) * \
 #                   final_data.likes.str.extract(r'[\d\.]+([KM]+)', expand=False)
  #                  .fillna(1)
   #                 .replace(['K','M'], [10**3, 10**6]).astype(int))

#final_data['retweets'].unique()

#final_data.retweets = (final_data.retweets.replace(r'[KM]+$', '', regex=True).astype(float) * \
   #                 final_data.retweets.str.extract(r'[\d\.]+([KM]+)', expand=False)
  #                  .fillna(1)
 #                    .replace(['K','M'], [10**3, 10**6]).astype(int))

#final_data.replies = (final_data.replies.replace(r'[KM]+$', '', regex=True).astype(float) * \
 #                   final_data.replies.str.extract(r'[\d\.]+([KM]+)', expand=False)
  #               .fillna(1)
 #                  .replace(['K','M'], [10**3, 10**6]).astype(int))

final_data.head()

final_data.time.dtype

final_data['time'] = pd.to_datetime(final_data.time, format='%Y-%m-%d')

final_data['time']

final_data.rename(columns = {'content':'Tweets'}, inplace = True)
 
final_data.head()

#  import
import re
from textblob import TextBlob

"""<hr>

 **Clean the text**
"""

final_data['Tweets']=final_data['Tweets'].apply(str)

# Create a function to clean the tweets
def cleanTxt(tweet):
  tweet = re.sub(r"@[\w]*", '', tweet)
  tweet = re.sub(r'#', '',tweet) # removing the symbol
  tweet = re.sub(r'RT[\s]+', '', tweet) # Removing RT
  tweet = re.sub(r'https?:\/\/\S+', '', tweet)# Remove the hyper link
  return tweet

final_data['Tweets'] = final_data['Tweets'].apply(cleanTxt)

# remove special characters, numbers, punctuations
final_data['Tweets'] = final_data['Tweets'].str.replace("[^a-zA-Z#]", " ")

# create a function to get the subjectivity
def getSubjectivity(tweet):
  return TextBlob(tweet).sentiment.subjectivity

# Create a funtion to get the polarity
def getPolarity(tweet):
  return TextBlob(tweet).sentiment.polarity

# Create two new columns
final_data['Subjectivity'] = final_data['Tweets'].apply(getSubjectivity)
final_data['Polarity'] = final_data['Tweets'].apply(getPolarity)

# Show the new dataframe with the new columns
final_data.head(10)

# Create a function to compute the negative, neutral and positive analysis
def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

final_data['Analysis'] = final_data['Polarity'].apply(getAnalysis)
# show the dataFrame
final_data.head()

final_data.to_csv('RESULT.csv')