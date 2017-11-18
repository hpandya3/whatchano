from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def getSentiment(text):
  return analyser.polarity_scores(text)