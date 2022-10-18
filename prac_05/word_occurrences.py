"""
CP1404/CP5632 Practical
Word occurrences
Estimate: 30
Actual:
"""

word_to_count = {}
text = input("TEXT: ")
example_text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    word_occurrence = word_to_count.get(word, 0)
    word_to_count[word] = word_occurrence + 1
words = list(word_to_count.keys())
words.sort()
max_word_length = max(len(word) for word in words)
for word in words:
    print("{:{}}, {}".format(word, max_word_length, word_to_count[word]))
