#Exercise  -> Access the value of key history
sample_dict ={ 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

history = sample_dict["class"]["student"]["marks"]["history"]    
print (history)  #outcome 80  


#Exercise
#Delete set of keys from Python Dictionary
sample_dict = {
  "name": "Kelly",       #remove
  "age":25,
  "salary": 8000,        #remove
  "city": "New york"
}
keys_to_remove = ["name", "salary"]

#Delete an entry in a dictionary using loop
for key in keys_to_remove:
    del sample_dict[key]
print(f'result is: {sample_dict}')

# result is: {'age': 25, 'city': 'New york'}