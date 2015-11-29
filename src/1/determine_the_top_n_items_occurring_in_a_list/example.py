# example.py
#
# Determine the most common words in a list

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

# This module implements specialized container datatypes providing alternatives
# to Python’s general purpose built-in containers, dict, list, set, and tuple.
# Reference: https://docs.python.org/2/library/collections.html
import collections

word_counts = collections.Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]

# Example of merging in more words
morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))
