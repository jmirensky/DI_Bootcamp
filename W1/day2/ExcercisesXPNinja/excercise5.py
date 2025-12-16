#Longest word without a specific character
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.

#with ChatGTP

longest_sentence = ""

while True:
    sentence = input("Write the longest sentence you can without the letter 'A': ")

    if "a" in sentence.lower():
        print("Oops! The letter 'A' is not allowed.")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! New longest sentence")
