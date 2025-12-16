#Predict the output of the following code snippets:
#Coment what is your guess, then run the code and compare

#Predictions
# 5 < 3 #False
# 3 == 3  #True
# 3 == "3"  #False
# "3" > 3 #Error   (not possible > or < for string)
# "Hello" == "hello"  #True --> is False, case sensitive

#Verification
print(5 < 3) #False
print(3 == 3)  #True
print(3 == "3")  #False
print("3" > 3) #Error  --> '>' not supported between instances of 'str' and 'int'
print("Hello" == "hello")  #True --> is False