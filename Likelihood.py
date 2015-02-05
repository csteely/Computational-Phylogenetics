"""
Created on Mon Feb  2 15:20:07 2015

@author: Cody
"""



from scipy.stats import binom
import matplotlib.pyplot as plt

n = 5
p = 0.5 # Change this and repeat

data = binom.rvs(n,p)

"""
For the in-class version of this exercise, I'm going to perform a manual draw from a binomial using colored marbles in a cup. We'll arbitrarily define dark marbles as successes and light marbles as failures.
Record the outcomes here:
Draw 1:Dark
Draw 2:Dark
Draw 3:Dark
Draw 4:Dark
Draw 5:Light
Number of 'successes': 
Now record the observed number of succeses as in the data variable below.
"""

data = 4
numTrials = 5

"""
Since we are trying to learn about p, we define the likelihood function as;
L(p;data) = P(data|p)
If data is a binomially distributed random variable [data ~ Binom(5,p)]
P(data=k|p) = (5 choose k) * p^k * (1-p)^(n-k)
So, we need a function to calculate the binomial PMF. Luckily, you should have just written one and posted it to GitHub for your last exercise. Copy and paste your binomial PMF code below. For now, I will refer to this function as binomPMF(). 
"""

def semifactorial(maximum,minimum):

    import numpy
#creating a placeholder for the values
    ans=1
    
#Looping through the numbers, subtracting one from the max each time through
#until the maximum value is equal to the minimum. Each of these numbers is
#multiplied by the placeholder value.
    
    while int(maximum) >= int(minimum) and int(maximum) > 1:
        ans=int(ans*maximum)
        maximum=maximum-1
    return(ans)


def binomial(n,k):
    
    answer=int((semifactorial(n,1))/(semifactorial(n-k,1)*semifactorial(k,1)))
    
    return(answer)


def pmf(n,k,p):
    answer=binomial(n,k)*pow(p,k)*pow((1-p),(n-k))
    
    return(answer)
    



"""
Now we need to calculate likelihoods for a series of different values for p to compare likelihoods. There are an infinite number of possible values for p, so let's confine ourselves to steps of 0.05 between 0 and 1.
"""

pValueList=[0,.5,.10,.15,.20,.25,.30,.35,.40,.45,.50,.55,.60,.65,.70,.75,.80,.85,.90,.95,1]

LikelihoodList=[]

for x in pValueList:
    result=pmf(5,4,x)
    LikelihoodList.append(result)
print(LikelihoodList)


# Calculate the likelihood scores for these values of p, in light of the data you've collected



# Find the maximum likelihood value of p (at least, the max in this set)

Maxlike=LikelihoodList.index(max(LikelihoodList))

print("The p value with the maximum likelihood is", pValueList[Maxlike])

plt.scatter(pValueList,LikelihoodList)
plt.xlabel("P Values")
plt.ylabel("Likelihood Values")
