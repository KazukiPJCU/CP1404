"""
CP1404/CP5632 Practical
Word occurrences
Estimate: 30
Actual:
"""

word_to_count = {}
text = input("TEXT: ")
words = text.split()
for word in words:
    word_occurrence = word_to_count.get(word, 0)
    word_to_count[word] = word_occurrence + 1
words = list(word_to_count.keys())
words.sort()
for word in words:
    print(f"{word}, {word_to_count[word]}")
    print("{:{}},{}".format(word, 10, word_to_count[word]))
