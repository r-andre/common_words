This is a simple program to find the common words of two text files.

It takes the texts in `data_f0.txt' and `data_f1.txt` and generates a list of words that appear in both documents. The list of words is then converted to lower case, filtered to only contain letters and no numbers or special characters, and sorted alphabetically.

The program also calculates the word frequency distribution and provides the output as `output_f.csv`, containing the word, its frequency in the first text, its frequency in the second text, and its total frequency (`word,frequency_doc1,frequency_doc2,frequency_total`).