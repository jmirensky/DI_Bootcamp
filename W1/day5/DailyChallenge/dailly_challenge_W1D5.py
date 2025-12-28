#Challenge 1: Letter Index Dictionary  (HARD EXCERCISE, I used ChatGPT)

#1. User Input:
    #Ask the user to enter a word.
    #Store the input word in a variable.
#2. Creating the Dictionary:
    #Iterate through each character of the input word using a loop.
    #And check if the character is already a key in the dictionary.
    #    * If it is, append the current index to the list associated with that key.
    #    * If it is not, create a new key-value pair in the dictionary.
    #Ensure that the characters (keys) are strings.
    #Ensure that the indices (values) are stored in lists.
#3. Expected Output, example “dodo” {"d": [0, 2], "o": [1, 3]}. 

while True:
    word = input('Enter only one word (letters only): ').lower()    #conversion to lower
                                                                    #default string, but...

    if not word.isalpha():   #validation against numbers, symbols ans spaces
        print("Error: only letters are allowed. Try again.\n")
    else:
        print("Input válido")  #input ok
        break   # get out of the while because input is valide.
    
my_dict = {} #creation empty dict to keep something (fo example lists)

for i, letter in enumerate(word):   # connect index and letter
        if letter not in my_dict:
            my_dict[letter] = []  #each "new" letter is a key + I assign it an empty list as a value
        my_dict[letter].append(i)  #For each letter, add its index to the list, without replacing what was before,
                                    #but accumulating positions.

print(my_dict)


# Challenge 2: Affordable Items
#Goal: Create a program that prints a list of items that can be purchased with a given amount of money.
#1. Store Data:
    #You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
    #You will also be given a string (wallet) representing the amount of money you have.
#2. Data Cleaning:
    #You need to clean the dollar sign and the commas using python. Don’t hard code it.
#3. Determining Affordable Items:
    #create a list called basket and add there the items that you can buy with the money you have on the wallet
    #Don’t forget to update the wallet after buying an item.
    #If the basket is empty (no items can be afforded), return the string “Nothing”.
#Otherwise, print the basket list in alphabetical order.
#4. Examples:   {key is item: price is value}

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}    
wallet = '$300'  #str

#items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
#wallet = "$100"

#items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
#wallet = "$1"


#Cleaning wallet
clean_wallet = int(wallet.replace("$", "").replace(",", ""))  #remove $ and commas, and convert it to int

basket = [] #List of items we can really buy

for item, price in items_purchase.items():  # through the items in order of priority (dictionary order)
    clean_price = int(price.replace("$", "").replace(",", ""))  #remove $ and commas, and convert price of item to int

    if clean_wallet >= clean_price:   # If we have enough money, we'll buy
        basket.append(item)  #add item to basket list
        clean_wallet -= clean_price  #and update the available money

# Final basket
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
