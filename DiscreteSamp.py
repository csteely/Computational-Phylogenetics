
import matplotlib.pyplot as plt


## 1)Essentially a function for factorials, allowing for the user to set
##a minimum and maximum value

def semifactorial(maximum,minimum):


#creating a placeholder for the values
    ans=1
    
#Looping through the numbers, subtracting one from the max each time through
#until the maximum value is equal to the minimum. Each of these numbers is
#multiplied by the placeholder value.
    
    while int(maximum) >= int(minimum) and int(maximum) > 1:
        ans=int(ans*maximum)
        maximum=maximum-1
    return(ans)
    
##2a)create a function to find binomial coefficient
#Function follows the equation given in the reading

def binomial(n,k):
    answer=int((semifactorial(n,1))//(semifactorial(n-k,1)*semifactorial(k,1)))

    
    return(answer)
    

##2b)Create a more efficient function for the same purpose

def binomialb(n,k):
    answer=int(semifactorial(n,n-k+1)//semifactorial(k,1))
    
        
    return(answer)


##3) 2b seems slightly faster, by a few seconds (depending on the numbers). 

##4)Binomial PMF..supply n,k, and p and the equation does the rest.

def pmf(n,k,p):
    answer=binomial(n,k)*pow(p,k)*pow((1-p),(n-k))
    
    return(answer)


##5) Function to sample from discrete distribution
#allows input of event list and probability list
def discreteSamp(events,probs):
    import random
#random.choice takes a random item from a list
    event=random.choice(events)
#finds the index of the chosen item, and picks out the corresponding item in the probability list.
    index=events.index(event)
    prob=probs[index]

    return(events.index(event))



##6) Function to look at probability with replacement for any number of sites
##and repetitions. Prints values to screen as lists.
#allows input of repetitions and sample size
#There's about to be a billion variables and things happening. Prepare for your mind to explode.

def randomSamp(repetitions,sampSize):
#event list, probability list, and empty lists for later variables.
    listEvents=[1,2]
    listProbs=[.5,.5]
    x=[]
    y=[]
    listPropx=[]
    listPropy=[]
    listPmfx=[]

#blank counters for later.
#repetitions go here, too. 
    for events in range(repetitions):
        n=0
        m=0

#calculate the proportion of x and y
#If event one is called, adding 1 to list n.
#if event two is called, adding 1 to list m.
        
        for events in range(sampSize):
            if discreteSamp(listEvents,listProbs)==0:
                m=m+1
            else:
                n=n+1
#appending back to list
        x.append(m)
        y.append(n)

#calculating the proportion of event 1 and event 2. calculating pmf.
#adding these values to different lists above.
        
        xprop=m/sampSize
        
        yprop=n/sampSize
        listPropx.append(xprop)
        listPropy.append(yprop)

        pmfx= pmf(400,m,.5)
        
        listPmfx.append(pmfx)

#using the matplotlib histogram function to plot the frequencies of the values added to the list
##added a try and except loop since you can't get graphs for only 1 repetition
##Prints the number of occurrences for x and y if the graphs can't be made.

#Probability of x
    try:
        plt.hist(listPropx)
        plt.title("Proportion of event 1 occurrences for " + str(repetitions) + " iterations")
        plt.xlabel("Proportion of event 1")
        plt.ylabel("Frequency")
        plt.show()
    
#probability of y
        plt.hist(listPropy)
        plt.title("Proportion of event 2 occurrences for " + str(repetitions) + " iterations")
        plt.xlabel("Proportion of event 2")
        plt.ylabel("Frequency")
        plt.show()

#PMF values for the success of event 1
    
        plt.hist(listPmfx)
        plt.title("Pmf Event 1 for occurrences for " + str(repetitions) + " iterations")
        plt.xlabel("Pmf values")
        plt.ylabel("Frequency")
        plt.show()

    except:
        print("The number of occurrences of event 1: ", x)
        print("The number of occurrences of event 2: ", y)
        
#iterating once over the 400 picks
randomSamp(1,400)

#iterating 100 times
randomSamp(100,400)

#iterating 10000 times
randomSamp(10000,400)

##Comparisons were just done based on the graphs.
##Proportions of x and y graphs are always similar, with most values near the .50 mark.

#PMF seams to gradually climb to .040
