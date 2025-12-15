#Check what is the type of each value, then change it:
# if it is a string, make it an integer and vice-versa:

bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))   #string
print(type(phone_number))  #int

bank_balance= int(bank_balance) #convert to int
print(type(bank_balance)) #verfication

phone_number= str(phone_number)   #convert to str
print(type(phone_number))   #verfication