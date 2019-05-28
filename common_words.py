#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
from re import search

# Reading the texts from the data files and storing them in variables
DATA_F0 = open("data_f0.txt")
DATA_F1 = open("data_f1.txt")
TEXT0 = DATA_F0.readlines()
TEXT1 = DATA_F1.readlines()
DATA_F0.close()
DATA_F1.close()

def make_list(text):
    '''
    A function to create a list of strings from a text.
    It takes the input text and splits it into words.
    '''
    wordlist = []
    for line in text:
        wordlist = wordlist + (line.split())
    return wordlist

# Making lists of words from the text files using the defined function.
W_LIST0 = make_list(TEXT0)
W_LIST1 = make_list(TEXT1)

def conv_list(wordlist):
    '''
    A function to convert all strings in a list.
    It takes the words and first removes all non-alphabetic characters,
    and then converts the words into lower case.
    '''
    new_list = []
    for word in wordlist:
#        wordlist.remove(word)
        word = re.sub("[^a-zA-Z]+", "", word)
        word = word.lower()
        new_list.append(word)
    return new_list

# Converting the words of the list.
C_LIST0 = conv_list(W_LIST0)
C_LIST1 = conv_list(W_LIST1)

def find_common(wordlist0, wordlist1):
    '''
    A function to find the common entries in two lists.
    It takes two lists of words and outputs all the words that appear in both.
    '''
    common_words = list(set(wordlist0).intersection(wordlist1))
    return common_words

# Finding common words in both lists.
COMMON_WORDS = find_common(C_LIST0, C_LIST1)
COMMON_WORDS.sort()

# Creating an output file to store the data in.
OUTPUT_F = open("output_f.csv", "w+")
OUTPUT_F.write("word,frequency_doc1,frequency_doc2,frequency_total\n")

def count_words(wordlist0, wordlist1, wordlist2, file):
    '''
    A function to count how many times an element appears in two lists.
    It counts the number of appearances in one list and in another lists, adds
    them up and then prints all three values to an output file.
    '''
    for word in wordlist0:
        n_list1 = wordlist1.count(word)
        n_list2 = wordlist2.count(word)
        n_total = n_list1 + n_list2
        file.write(word
                   + ","
                   + str(n_list1)
                   + ","
                   + str(n_list2)
                   + ","
                   + str(n_total)
                   + "\n")

# Counting the words and writing the data to the file
count_words(COMMON_WORDS, C_LIST0, C_LIST1, OUTPUT_F)

OUTPUT_F.close()
