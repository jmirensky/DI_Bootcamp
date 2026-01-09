
#Daily challenge Gold: Solve the Matrix

#You are given a “Matrix” string:
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM#
$a 
#t%''' 
#This represents a grid of characters, and your task is to decode the hidden message within.

'''Understanding the Matrix: 
    * Imagine this string arranged in rows and columns, forming a grid. 
    * To work with it in Python, you will need to transform this string into a 2D list (a list of lists), 
where each inner list represents a row.'''

# Step 1: Transforming the String into a 2D List
matrix = [list(row) for row in MATRIX_STR.strip().splitlines()]
print(matrix)
    #strip() → Cleans borders: Removes spaces and line breaks ONLY from the beginning and end of the string.
    #splitlines() → Splits into rows: Splits the string every time there is a line break (\n) and returns a list.
    #list(row) → Splits into letters

#quick check
for row in matrix:
    print(row)


#Step 2: Processing Columns
#Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
#You’ll need to write code that iterates through the columns of your 2D list.
#Think about how you can access the elements of a 2D list by column.


#Step 3: Filtering Alpha Characters
#only select alpha characters (letters).
#For each character in a column, check if it’s an alpha character.
#If it is, add it to a temporary string.
#Think about how you can check if a character is an alphabet letter.
#Logic --> You take each character, If it's a letter, you store it, If not, you ignore it

result = ""    #empty string

rows = len(matrix)  #7 rows
cols = len(matrix[0])   #3 columns

for col in range(cols):     # Traverse the columns of the matrix, from left to right
    for row in range(rows):   # For each column, go down through all the rows (from top to bottom)
        char = matrix[row][col]   #character at position [row][column]
        result += char           #send each character to the empty string

#quick check
print(f'result: {result}')

#Step 4:
# Replacing Symbols with Spaces Replace every group of symbols (non-alpha characters)
# between two alpha characters with a space. After you have gathered the alpha characters,
#  you will need to iterate through them, and where there are non alpha characters between them,
#  you will insert a space. Think about how you can keep track of when you encounter an alphabet character,
# and when you encounter a non alphabet character.

decoded_message = ""      #empty string
previous_was_alpha = False

rows = len(matrix)    #7 rows
cols = len(matrix[0])   #3 columns

for col in range(cols):   # Traverse the columns of the matrix, from left to right
    for row in range(rows):    # For each column, go down through all the rows (from top to bottom)
        char = matrix[row][col]   #character at position [row][column]

        if char.isalpha():
            decoded_message += char    #add each "valid" character to the empty string
            previous_was_alpha = True
        else:
            if previous_was_alpha:
                decoded_message += " "   # replace symbols with spaces & send it to the empty string if before there  is a a letter
                previous_was_alpha = False


#Step 5: Constructing the Secret Message
#Combine the filtered and processed characters to form the decoded message.
#Print the decoded message.

decoded_message = decoded_message.strip()
print(f'The hidden message is: {decoded_message}')