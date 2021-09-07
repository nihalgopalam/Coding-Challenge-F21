import requests
import json

#open text file making sure the newlines are not inlcuded
with open('input.txt', 'r') as file:
    input = file.read().replace('\n', '')

#API for sentiment analysis
url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

#saving the text from the file as the input for the API
querystring = {"text":input}

#headers for API with Nihal Gopalam's API key
headers = {
    'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
    'x-rapidapi-key': "546a67c5f8msh17bb2e80c0d2defp1cd390jsn35c288779810"
    }

#call API with the url, headers, and text
sentiment_response = requests.request("GET", url, headers=headers, params=querystring)

#parse the json response
sentiment_parsed = json.loads(sentiment_response.text)

#saving the keywords used in another variable for ease of access
words_parsed = sentiment_parsed["keywords"]

#API for emotion analysis
url = "https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/"
#saving text from file as the input for the API
querystring = {"text":input}
#headers for API with Nihal Gopalam' API key
headers = {
    'x-rapidapi-host': "twinword-emotion-analysis-v1.p.rapidapi.com",
    'x-rapidapi-key': "546a67c5f8msh17bb2e80c0d2defp1cd390jsn35c288779810"
    }

#call API with the url, headers, and text
emotion_response = requests.request("GET", url, headers=headers, params=querystring)

#parse the json response
emotion_parsed = json.loads(emotion_response.text)
emotion_scores = emotion_parsed["emotion_scores"]
#output 
print("Overall this piece of text is " + sentiment_parsed["type"])
print("The text has a score of " + str(sentiment_parsed["score"]))
print("The text has a ratio of " + str(sentiment_parsed["ratio"]))
print("******************************")
print("These are the emotion scores of the text: ")
print(json.dumps(emotion_scores, indent=4, sort_keys=True))
print("******************************")
print("These are the words used to calculate the score and ratio in order from most positive to negative: ")
#pretty print the keywords since it is messy
print(json.dumps(words_parsed, indent=4, sort_keys=True))

