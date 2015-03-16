# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:25:12 2015

@author: Cody
"""

"""
Object oriented continuous markov chain. 
Should take variables, and allow for some flexibility within the program. 
Should have an initiation point, simulation, and hillclimber function
"""

import numpy
import random

##Creating the object and defining the initial variables. 
class ContMarkov (object):
    def __init__(self, v=10.0, stateSpace= ["A","C","G","T"],freq=[.25,.25,.25,.25],R=[.35,.28,.44,.36,.41,.29], Q=None, QNorm=None, nsims=1, MProbs=None):
        self.v=v
        self.stateSpace=stateSpace
        self.freq=freq
        self.R=R
        self.nsims=nsims
        self.stateList=[]
        self.times=[]
        if Q==None:
            self.Q=[]
        if QNorm==None:
            self.QNorm=self.normalize()
        if MProbs==None:
            self.MProbs=self.marginalize()

  ##Setting up the Q matrix and normalizing the values     
    def normalize(self):
        self.Q=numpy.array([[-1*(self.R[0]*self.freq[1]+self.R[1]*self.freq[2]+self.R[2]*self.freq[3]),self.R[0]*self.freq[1],self.R[1]*self.freq[2],self.R[2]*self.freq[3]],
        [self.R[0]*self.freq[0],-1*(self.R[0]*self.freq[0]+self.R[3]*self.freq[2]+self.R[4]*self.freq[3]),self.R[3]*self.freq[2],self.R[4]*self.freq[3]],
        [self.R[1]*self.freq[0],self.R[3]*self.freq[1],-1*(self.R[1]*self.freq[0]+self.R[3]*self.freq[1]+self.R[5]*self.freq[3]),self.R[5]*self.freq[3]],
        [self.R[2]*self.freq[0],self.R[4]*self.freq[1],self.R[5]*self.freq[2],-1*(self.R[2]*self.freq[0]+self.R[4]*self.freq[1]+self.R[5]*self.freq[2])]])
        
        ##Finding the weighted average of these values
        self.weightedAvg=(self.freq[0]*-self.Q[0][0])+(self.freq[1]*-self.Q[1][1])+(self.freq[2]*-self.Q[2][2])+(self.freq[3]*-self.Q[3][3])
        
        ##Normalizing the matrix by dividing by the weighted average
        
        self.QNorm=(self.Q/self.weightedAvg)
        print(self.QNorm)
        return(self.QNorm)
        
    ##Marginalizing the values 
    def marginalize(self):
        print(self.QNorm)
        
        ##Setting up a matrix with the probabilities by dividing each value in the matrix by the absolute value of the diagonal.
        
        self.MProbs=[[self.QNorm[0][1]/-self.QNorm[0][0],self.QNorm[0][2]/-self.QNorm[0][0],self.QNorm[0][3]/-self.QNorm[0][0]],
                    [self.QNorm[1][0]/-self.QNorm[1][1],self.QNorm[1][2]/-self.QNorm[1][1],self.QNorm[1][3]/-self.QNorm[1][1]],
                    [self.QNorm[2][0]/-self.QNorm[2][2],self.QNorm[2][1]/-self.QNorm[2][2],self.QNorm[2][3]/-self.QNorm[2][2]],
                    [self.QNorm[3][0]/-self.QNorm[3][3],self.QNorm[3][1]/-self.QNorm[3][3],self.QNorm[3][2]/-self.QNorm[3][3]]]
       ## print(self.MProbs)
        return(self.MProbs)
        
        
        ##Setting up the simulation
    def simulate(self):
        
        self.firstState=[]
        
        #Changing the list of freqs to floats
        self.freq=list(map(float, self.freq))
        
        ##Turns out it's pretty difficult to make a list of lists into
        ##floats. So I had to divide them up into individual lists,
        ##change them into floats, then concatonate them back into one list.
        
        self.a=self.MProbs[0]
        self.b=self.MProbs[1]
        self.c=self.MProbs[2]
        self.d=self.MProbs[3]
        self.MProbs=list(map(float,self.a))
        self.MProbs=list(map(float,self.b))
        self.MProbs=list(map(float,self.c))
        self.MProbs=list(map(float,self.d))
        self.MProbs=list([self.a]+[self.b]+[self.c]+[self.d])
        
    ##drawing a random number        
        x=random.random()
    ##determines the starting state based on the random number
        if x < self.freq[0]:
            self.firstState.append(self.stateSpace[0])
        elif x > self.freq[0] and x < self.freq[0]+self.freq[1]:
            self.firstState.append(self.stateSpace[1])
        elif x > self.freq[0]+self.freq[1] and x < self.freq[0]+self.freq[1]+self.freq[2]:
            self.firstState.append(self.stateSpace[2])
        else:
            self.firstState.append(self.stateSpace[3])
        self.stateList=self.firstState
        
    ##Cool, we have the first state, now to do the rest.
    ##Should continue to loop until the sum of the times is greater than v
    ##, the branch length.
        while sum(self.times) < self.v:
    ##So if the last item in the list is an A, it uses this part of the loop
    ##All of these below work in a similar way as the starting state
    ##They use random.expovariate to determine the waiting time
    ##Then they draw a new state based on the marginal probabilities of each 
    ##of the possible new states.
            if self.stateList[-1]==self.stateSpace[0]:
                self.waitTime=random.expovariate(-self.QNorm[0][0])
                self.times.append(self.waitTime)
                x=random.random()
                if x < self.MProbs[0][1]:
                    self.stateList.append(self.stateSpace[1])
                elif x > self.MProbs[0][1] and x < self.MProbs[0][1]+self.MProbs[0][2]:
                    self.stateList.append(self.stateSpace[2])
                else:
                    self.stateList.append(self.stateSpace[3])
     ##This is for C                   
                    
            if self.stateList[-1]==self.stateSpace[1]:
                self.waitTime=random.expovariate(-self.QNorm[1][1])
                self.times.append(self.waitTime)
               
                x=random.random()
                if x < self.MProbs[1][0]:
                   self.stateList.append(self.stateSpace[0])
                elif x > self.MProbs[1][0] and x < self.MProbs[1][0]+self.MProbs[1][2]:
                   self.stateList.append(self.stateSpace[2])
                else:
                   self.stateList.append(self.stateSpace[3])
                   
        ##This is for G
            if self.stateList[-1]==self.stateSpace[2]:
                self.waitTime=random.expovariate(-self.QNorm[2][2])
                self.times.append(self.waitTime)
                x=random.random()
                if x < self.MProbs[2][0]:
                    self.stateList.append(self.stateSpace[0])
                elif x > self.MProbs[2][0] and x < self.MProbs[2][0]+self.MProbs[2][1]:
                    self.stateList.append(self.stateSpace[1])
                else:
                    self.stateList.append(self.stateSpace[3])
         
        ##This is for T           
                        
            if self.stateList[-1]==self.stateSpace[3]:
                self.waitTime=random.expovariate(-self.QNorm[3][3])
                self.times.append(self.waitTime)
                x=random.random()
                if x < self.MProbs[3][0]:
                    self.stateList.append(self.stateSpace[0])
                elif x > self.MProbs[3][0] and x < self.MProbs[3][0]+self.MProbs[3][1]:
                    self.stateList.append(self.stateSpace[1])
                else:
                    self.stateList.append(self.stateSpace[2])
                      
                        
            return self.stateList, self.times
 
