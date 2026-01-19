
#Daily challenge GOLD: DNA [with chatGPT]

# This challenge is about Biology & classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 5 Genes. It also can mutate, meaning a random number of genes
#  can randomly flip ( With ~1/3 probability (30%), the gene flips)
# A DNA is a series of 3 chromosomes, and it can also mutate the same way Chromosomes can mutate.
# Implement these classes.

# Create a new class called Organism that accepts a DNA object and an environment parameter
#  that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s ("perfect DNA").
# Then stop and record the number of generations (iterations) it took.

#     [In this simplified model, perfect DNA is not always achieved within the generation limit]



#We keep it simple: 3 chromosomes of 5 genes each and a maximum of 1000 generations.

 # To generate random numbers
import random

# -------- Gene --------
class Gene:
    def __init__(self, value=None):
         # by default None, since no value is passed, 0 or 1 is chosen randomly
        self.value = value if value is not None else random.choice([0, 1])   #Value: 0 o 1

    def mutate(self):
        # With a 30% probability, the gene changes its value from 0 to 1 and vice versa
        if random.random() < 0.3:
            # It can mutate → it flips
            self.value = 1 - self.value    

    def __repr__(self):
        # Allows displaying the gene as text (0 or 1))
        return str(self.value)


# -------- Chromosome --------
class Chromosome:
    # A chromosome is a list of 5 genes
    def __init__(self):
        self.genes = [Gene() for _ in range(5)]   

    def mutate(self):
        # Attempt to mutate each gene on the chromosome (remember that we set the probability to 30%)
        for gene in self.genes:      
            gene.mutate()            

    def is_all_ones(self):
        # Check if all genes are 1
        return all(g.value == 1 for g in self.genes)  

    def __repr__(self):
        # Display the chromosome as a sequence of 0s and 1s
        return "".join(str(g) for g in self.genes)  


# -------- DNA --------
class DNA:
    # DNA is made up of 3 chromosomes
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(3)]   

    def mutate(self):
        # Attempt to mutate each chromosome
        for chromo in self.chromosomes:          
            chromo.mutate()

    def is_all_ones(self):
        #Checks if all chromosomes are 1
        return all(c.is_all_ones() for c in self.chromosomes) 

    def __repr__(self):
        # Displays DNA by separating chromosomes with |
        return " | ".join(str(c) for c in self.chromosomes) 


# -------- Organism --------
class Organism:      
    def __init__(self, environment=0.5):             
        self.dna = DNA()      #New DNA is created for the organism (3 chromosomes of 5 genes each)                  
        self.environment = environment     # The probability of mutation is defined    

    def mutate(self):
        #Mutate only if the environment allows it
        if random.random() < self.environment:
            self.dna.mutate()


# -------- Simulation --------

#Generations are limited
def evolve(max_generations=1000):  
    organism = Organism(environment=0.6)

    # The process is repeated for each generation
    for generation in range(1, max_generations + 1):
        organism.mutate()

         # If the DNA is all ones, it ends
        if organism.dna.is_all_ones():
            print("Perfect DNA found")
            print("Generation:", generation)
            print("DNA:", organism.dna)
            return
    
    # If perfect DNA is not achieved
    print("Perfect DNA not reached in Generation:", generation)
    print("Last DNA:", organism.dna)


# -------- Run the code --------
evolve()


#Conclusion [with chatGPT]

'''In this exercise, an organism with DNA that mutates depending on the environment was simulated.
Mutations occur randomly and can change individual genes.

The experiment shows that mutation alone creates genetic variation, but does not always lead to a perfect DNA.
This reflects a real biological principle: mutation introduces changes, but without natural selection, improvement is not guaranteed.

When mutation happens too often, previous progress can be lost.
Therefore, evolution depends on a balance between mutation and stability.'''