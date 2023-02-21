"""
Contains the function `rm_punct` which removes the
punctuations from a given text.
"""

import string

def rm_punct(text: str) -> str:
	"""
	Removes all the punctuations from the given text.
	"""
    return text.translate(str.maketrans('', '', string.punctuation))