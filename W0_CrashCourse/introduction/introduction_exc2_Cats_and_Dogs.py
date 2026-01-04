#Exercise 2 : cat's and dog's years
#Write a program that will calculate cat’s and dog’s years based on human years:
#I have a cat and a dog. I got them at the same time as kitten/puppy. 
# That was humanYears years ago. 
# Print their respective ages now as [humanYears,catYears,dogYears]

#NOTES:
#humanYears >= 1 humanYears are whole numbers only
#Cat Years 15 cat years for first year +9 cat years for second year +4 cat years for each year after that
#Dog Years 15 dog years for first year +9 dog years for second year +5 dog years for each year after that

#human_years = 10
#output: [10, 56, 64]

#human_years = 1
#output: [1, 15, 15]

#human_years = 2
#output [2, 24, 24]

#test the program with the following values:
#human_years = 10
#human_years = 1
#human_years = 2


def calculate_pet_years(humanYears):

    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]

#if human_years = 10
print(calculate_pet_years(10))
#output --> [10, 56, 64]

#if human_years = 1
print(calculate_pet_years(1))
#output --> [1, 15, 15]

#if human_years = 2
print(calculate_pet_years(2))
#output --> [2, 24, 24]
