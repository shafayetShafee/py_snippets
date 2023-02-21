"""
Contains the function `expand_chatspeak_slang_words` which 
expands the slang words like IMHO, AFAIK etc.

Require the `slang.txt` file
"""

import re

# open the slang.txt file
with open('slang.txt') as sf:
    slines = sf.readlines()

# create the dictionary
slangs = {
    re.match("\w+(?=\=)", line).group(0).lower(): re.match("\w+=(.*?)\n", line).group(1) 
    for line in slines
}


def expand_chatspeak_slang_words(text: str) -> str:
	"""
	Returns the text with chatspeak slang words in expanded form
	given a input text string.
	"""
    expanded_text = []
    for word in text.split():
        if word.lower() in slangs:
            word = slangs[word.lower()]
        expanded_text.append(word)
    return " ".join(expanded_text)
