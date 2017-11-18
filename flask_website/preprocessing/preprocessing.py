import re

def preprocess(text):
  filtered = removeNoise(text)
  spaced = correctSpacing(filtered)
  return spaced.lower()

def removeNoise(text):
  """ Removes reply, weblinks, hashtags and newline segments
  """
  # Remove twitter weblinks
  sub_weblinks = re.sub(r'https?:\/\/\S+', '', text)

  # Replacing '\n' symbols with single spaces
  sub_newline = re.sub(r'\n', ' ', sub_weblinks)

  # Remove 'RT'
  sub_RT = re.sub(r'RT', '', sub_newline)

  # Remove '@someuser'
  sub_replies = re.sub(r'@\w+', '', sub_RT)

  # Remove '#' from hashtags converting it to words
  # sub_hashtag = re.sub(r'#', '', sub_replies)

  # Remove alphanumeric characters
  sub_non_an = re.sub(r'[^a-zA-Z0-9]+', ' ', sub_replies);

  # Remove excessive whitespace at the start and end
  final_string = sub_non_an.strip()

  return final_string

def correctSpacing(text):
  """ Removes multiple spaces and replaces it with a single space
  """
  words = [word.strip() for word in text.split()]
  return ' '.join(words)