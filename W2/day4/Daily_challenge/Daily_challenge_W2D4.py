#W2 D4 24 y 25Dic
#Daily challenge: Challenges

#Challenge 1: Sorting
#Write a Python program that takes a single string of words as input,
#  where the words are separated by commas (e.g., ‘apple,banana,cherry’).
#  The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

def sort_words(string):
    words = string.split(',')   #convert string to list
    words.sort()                #sort the list
    return ', '.join(words)     #convert list to string

user_string = input('Enter some words, separated by comma: ')   #request words
print('Sorted words:', sort_words(user_string))   #show results


#Challenge 2: Longest Word
def longest_word(sentence):
   '''Receives a sentence and returns the longest word.
   If there are several with the same length, it returns the first one.'''
   words = sentence.split()   # Split the sentence into words using spaces as separators
    
   # Initialize variables to store the longest word and its length
   max_length = 0            # Stores the maximum length found            
   longest = ""              # Stores the word with the greatest length 

   # Iterate through each word and compare its length to the current maximum length                          
   for word in words:
        if len(word) > max_length:
            max_length = len(word)   # Update the maximum length
            longest = word           # Update the longest word               
    
   return longest     # Return the longest word found

user_sentence = input('Enter a sentence: ')   #request the sentence to the user
print('The longest word in the sentence is:', longest_word(user_sentence))   #show result