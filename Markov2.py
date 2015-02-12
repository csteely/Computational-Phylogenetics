##I had to utilize your example function from last class since my function from 
##last class was entirely example specific...
##I'm working on making mine more general now.
import scipy as sp

def discSamp(events,probs):

    ranNum = sp.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None

def dmcSim(n,st=("a","b"),allProbs=[[0.5,0.5],[0.5,0.5]]):
    """
    This function simulates the progression of a discrete-time, discrete-state
    Markov chain. It takes 3 arguments: (1) The number of steps (n), (2) the 
    state space, and (3) the transition matrix. It returns a list containing 
    the progression of states through time. This list should have length n.
    
    The chain will be initiated with a randomly drawn state.
    """
    
    # Define list to hold chain's states
    chain = []    
    aCount=0
    CCount=0

    # Draw a state to initiate the chain
    currState = discSamp(st,[1.0/len(st) for x in st])
    chain.extend(currState)

    # Simulate the chain over n-1 steps following the initial state
    for step in range(1,n):
        probs = allProbs[st.index(currState)] # Grabbing row associated with currState
        currState = discSamp(st,probs) # Sample new state
        chain.extend(currState)        
        
    if chain[99]=="a":
        aCount=aCount+1
        print("a was the last state in the list")
    else:
        CCount=CCount+1
        print("C was the last state in the list")
states=("a","C")

# ----> Try to finish the above lines before Tues, Feb. 10th <----

# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?

##This runs through the program 100 times, with 100 steps each. 
##The function above now has print functions at the end allowing the user
##To see what the last value in the series was each time.  
for i in range(100):

    dmcSim(100,states)

    


# Try defining a state space for nucleotides: A, C, G, and T. Now define a 
# transition matrix with equal probabilities of change between states.

ntStates=["A","T","C","G"]
probs=[[.25,.25,.25],[.25,.25,.25],[.25,.25,.25],[.25,.25,.25]]

         
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
for i in range(100):

    dmcSim(100,ntStates,probs)
