from collections import Counter

input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# Split the input text into words
words = input_text.split()

# Count the frequency of each word
word_frequency = Counter(words)

# Sort the words alphabetically
sorted_words = sorted(word_frequency.keys())

# Display the frequency of each word
for word in sorted_words:
    print(f"{word}: {word_frequency[word]}")
