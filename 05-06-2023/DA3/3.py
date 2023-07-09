from collections import Counter
import re

input_str = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = re.findall(r'\w+', input_str)
word_freq = Counter(words)
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[0])
for word, freq in sorted_word_freq:
    print(word + ":" + str(freq))
