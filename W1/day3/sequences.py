#my_list = ['car',126,42, 'scisors', 'rock', 48]    #en python pueden ser un mix
#print(my_list[0])  #star counting in 0
#print(my_list[-1])  #star counting from the back
#print(my_list[:5])  #asume desde el ppo, mo cuenta el ultimo

#slicing: more than 1 value
#my_list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#print(my_list2[3:7])  # The result gives us [40, 50, 60, 70]  = range_index (último no inluido)

#slicing strings
#my_name = "Rick"
#print(my_name[0])
#print(my_name[2])
#print(my_name[-1])
#print(my_name[1:3])  # range_index

#my_hobbies = ["Eat", "Sleep", "Code"]
#print(my_hobbies[2])  #code   #acceder al item de acuerdo a su index_number
#print(my_hobbies[5])   #IndexError: list index out of range - busco algo fuera del rango
#modificar = aacedo x el index
#my_hobbies[1] = 'Meditate'
#print(my_hobbies)
#my_hobbies.append('Baseball')  #add (lo pone al final)
#print(my_hobbies)
#my_hobbies.remove('Baseball') #remove x descriptive
#print(my_hobbies)
#my_hobbies.pop(0)  #remove x posicion
#my_hobbies.pop()  #remueve el ultimo
#print(my_hobbies)

#my_hobbies = ["Food", "Code"]
#additional_hobbies = ["Sport", "More code"]
#my_hobbies + additional_hobbies 
#print (my_hobbies + additional_hobbies )  #junto 2 listas

#List functions

# len
#fruits = ["apple","pear", "banana", "melon"]
#print(len(fruits))

# sum
#numbers = [3, 12, 1, -4]
#print(sum(numbers))

#sort --> sorted ascendente o alfanumerico = devuelve una nueva lista
#print(sorted(numbers))
#print(sorted(fruits))
#y si quiero ordenar al reves?? buscar en chatgtp

#append es para 1 solo elemento
# #insert en una cierta posicion
#extend es para agregar al menos 2 elementos

#Exercise1
#list1 = [5, 10, 15, 20, 25, 50, 20]
#find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
#Hint : Look at the index method
#print(list1)
#print(list1.index(20))  #busco la 1° ocurrencia de 20, busca x descriptiva
#list1[3] = 200
#print(list1)
#expected = [5, 10, 15, 200, 25, 50, 20]

#tuple = lo mismo pero no sepuede modificar

#Exercise2
#Unpack the following tuple into 4 variables    
#a_tuple = (10, 20, 30, 40)
#a, b, c, d = a_tuple   #el proposito? unpack
#print (a)  #10
#print (b)  #20
#print (c)  #30
#print (d)  #40


#sets =  #like a list pero con unique values   {}

#de list a set y luego de set a list --> elimino duplicates
#my_set = set()
#my_set.add("Rick")
#my_set.add("Morty")
#my_set.add("Rick")   #no duplicates
#print(my_set)
#{"Rick", "Morty"}

#this_set = {"banana", "apple", "cherry", "apple"}
#print(this_set)
#{'banana', 'cherry', 'apple'}   #no duplicates y su propio orden
