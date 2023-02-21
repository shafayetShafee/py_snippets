"""
Contains the function `rm_stopwords` which remove stopwords
from the a text.
"""

from collections import Counter

import nltk
from nltk.corpus import stopwords

# download the stopwords 
nltk.download('stopwords')
stop_words = stopwords.words('english')

def rm_stopwords(text: str) -> str:
	"""
	Removes the stopwords (stopword from ntlk library)
	from the given text.
	"""
    stop_words_dict = Counter(stop_words)
    return " ".join([word for word in text.split() if word not in stop_words_dict])

