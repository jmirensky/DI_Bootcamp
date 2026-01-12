
#W2 D3
#Daily challenge: Advanced Algorithm

#BASE CODE --> list of 10000 random numbers, called list_of_numbers, and a target number = 3728.

#1st function
def find_pairs(numbers, target):   #Receives the numbers's list & the target
    '''1st find the pairs:
    Iterate through the list, calculate the number needed to reach the target, 
    and check if it has already appeared, thus avoiding repeating pairs.'''

    seen = set()         # to store the numbers we've already seen (since it's a set, it doesn't allow duplicates)
    pairs = []            # to store the pairs founded

    for n in numbers:                 # traverse the list only once, for each number:
        complement = target- n        # calculate the required number to reach the target 
        
        # If the complement has already been seen,
        # It means we found a valid pair
        if complement in seen:        # check if that number (complement) has already appeared
            pairs.append((n, complement))    #If it has already appeared → we found a pair! Save it without repeating them
        
         # to add the current number to the seen list
        seen.add(n)
        
    return pairs  #returns a list of tuples (n, complement)

#2nd function
def print_pairs(pairs, target):
    '''To display the pairs'''

    for a, b in pairs:
        print(f"{a} and {b} sums he target_number: {target}")

#3° function: Use the provided code
''' list of 10000 random numbers, called list_of_numbers, and a target number = 3728'''

import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728


#Finally, we invoke both functions
pairs = find_pairs(list_of_numbers, target_number)       #f. find the pairs
print_pairs(pairs, target_number)    #f. display the pairs

print(f"Total pairs found: {len(pairs)}")     #how many pairs meet the criteria
