#Given the following values:

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"
#1. Check if x is less than y and y is greater than z
print ((x < y) and (y > z))   #True
#2. Verify if word1 is not equal to word2
print (word1 != word2)        #True
print (word1 is not word2)
#3. Use bool() to check the boolean value of z and word1
print(bool(z))         #False 
print(bool(word1))  #True