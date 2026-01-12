#Find_Duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates
print(find_duplicates(some_list))   #duplicate letters  ['b', 'n']
