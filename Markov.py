# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 20:34:05 2015

@author: Cody
"""

"""
In this exercise, we will explore Markov chains that have discrete state spaces
and occur in discrete time steps. To set up a Markov chain, we first need to 
define the states that the chain can take over time, known as its state space.
To start, let's restrict ourselves to the case where our chain takes only two
states. We'll call them A and B.
"""

# Create a tuple that contains the names of the chain's states
chain=("A","B");



"""
The behavior of the chain with respect to these states will be determined by 
the probabilities of taking state A or B, given that the chain is currently in 
A and B. Remember that these are called conditional probabilities (e.g., the 
probability of going to B, given that the chain is currently in state A is 
P(B|A).)
We record all of these probabilities in a transition matrix. Each row
of the matrix records the conditional probabilities of moving to the other
states, given that we're in the state associated with that row. In our example
row 1 will be A and row 2 will be B. So, row 1, column 1 is P(A|A); row 1, 
column 2 is P(B|A); row 2, column 1 is P(A|B); and row 2, column 2 is P(B|B). 
All of the probabilities in a ROW need to sum to 1 (i.e., the total probability
associated with all possibilities for the next step must sum to 1, conditional
on the chain's current state).
In Python, we often store matrices as "lists of lists". So, one list will be 
the container for the whole matrix and each element of that list will be 
another list corresponding to a row, like this: mat = [[r1c1,r1c2],[r2c1,r2c2]]. 
We can then access individual elements use two indices in a row. For instance,
mat[0][0] would return r1c1. Using just one index returns the whole row, like
this: mat[0] would return [r1c1,r1c2].
Define a transition matrix for your chain below. For now, keep the probabilties
moderate (between 0.2 and 0.8).
"""

# Define a transition probability matrix for the chain with states A and B
mat=[[0.4,0.6],[0.5,0.5]]


# Try accessing a individual element or an individual row 
##For an individual element
print(mat[1][0])

##For a row
print(mat[1])


"""
Now, write a function that simulates the behavior of this chain over n time
steps. To do this, you'll need to return to our earlier exercise on drawing 
values from a discrete distribution. You'll need to be able to draw a random
number between 0 and 1 (built in to scipy), then use your discrete sampling 
function to draw one of your states based on this random number.
"""

# Import scipy U(0,1) random number generator

import numpy

random=numpy.random.uniform(0,1)

print(random)




# Paste or import your discrete sampling function



# Write your Markov chain simulator below. Record the states of your chain in 
# a list. Draw a random state to initiate the chain.

def MarkoPolo(trials):
    
#Get it? Like MarcoPolo, but more random.
    
    import numpy
    valueList=[]
    random=numpy.random.uniform(0,1)
    if random <= 0.5:
        value="A"
    else:
        value="B"
    valueList.append(value)
    for v in range(trials):
        
        value=value        
        if value=="A":
            x=numpy.random.uniform(0,1)
            if x<=.4:
                value="A"
                valueList.append(value)

            else:
                value="B"
                valueList.append(value)
                
        elif value=="B":
            x=numpy.random.uniform(0,1)
            if x<=.5:
                value="A"
                valueList.append(value)
                
            else:
                value="B"
                valueList.append(value)
                
                
    print(valueList)


# Run a simulation of 10 steps and print the output.

MarkoPolo(10)
