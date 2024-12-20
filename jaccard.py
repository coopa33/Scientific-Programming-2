"""
In this assignment, the goal is to reduce the computational complexity of the Jaccard function to such a degree that the computation of the Jaccard index is under 1 second for the following files:
- holmes.txt
- shakespear.txt
See: https://en.wikipedia.org/wiki/Jaccard_index

This code is an edited version of the original code provided by supervisor called original-jaccard.py.
"""


import sys
import string
import time



def read_as_list(file):
    """
    Opens a file and outputs a list of the words contained in the file.
    The words are converted using the clean function.
    """
    data = file.read()
    list_of_words = []
    for word in data.split(' '):
        clean_word = clean(word)
        list_of_words.append(clean_word)
    return list_of_words


def clean(word):
    """
    Cleans a word: remove punctuation and whitespace and convert to
    lower case.
    """
    return word.lower().strip(string.punctuation + string.whitespace)


#########################################33


# Complexity before optimization: O(n^2)
# Complexity after optimization: O(n)
def unique_items(collection):
    """
    Removes duplicate elements from the collection.
    """

    return set(collection)


# Complexity before optimization: O(n^2)
# Complexity after optimization: O(n)
def intersection(collection1, collection2):
    """
    Return the intersection of the two collections
    (so a set containing all the elements that are in both collections).
    """
    intersection_list = set(collection1) & set(collection2)
    return intersection_list




# Complexity before optimization: O(n^2)
# Complexity after optimization: O(n)
def union(collection1, collection2):
    """
    Return the union of the two collections
    (so a set containing all the elements that are in either collection).
    """
    return set(collection1 + collection2)


# Complexity before optimization: O(n^2)
# Complexity after optimization: O(n)
def main():

    start = time.time()
    # Check command line args
    if len(sys.argv) < 3:
        sys.exit(f'Usage python {sys.argv[0]} file1 file2')

    # Open both text files and convert to list of words
    with open(sys.argv[1], 'r', encoding = 'ISO-8859-1') as file1:
        list1 = set(read_as_list(file1))

    with open(sys.argv[2], 'r', encoding = 'ISO-8859-1') as file2:
        list2 = set(read_as_list(file2))

    # Compute jaccard
    jaccard_index = len(list1&list2)/len(list1 | list2)
    
    print(f'Jaccard index of {sys.argv[1]} and {sys.argv[2]}: {jaccard_index:.3f}')
    end = time.time()
    print(end-start)



main()
