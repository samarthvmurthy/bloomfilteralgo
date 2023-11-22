from pybloom_live import BloomFilter
import csv

# Create a Bloom filter with an estimated number of elements and a desired false positive rate.
capacity = 1000000  
false_positive_rate = 0.8  
bloom_filter = BloomFilter(capacity, false_positive_rate)

# Load your Twitter dataset (e.g., comments.csv)
with open('comments.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        comment = row[2] 

        words = comment.split()
        for word in words:
            bloom_filter.add(word)

# Function to check if a word is present in the Bloom filter
def word_in_bloom(word):
    return word in bloom_filter

while True:
             word_to_check = input("Enter a word to check in the comments: ")

             if word_to_check.lower()=='stop':
                  break
             
             if word_in_bloom(word_to_check):
               print(f"The word '{word_to_check}' is probably in the comments.")
               
             else:
                  print(f"The word '{word_to_check}' is not in the comments.")
