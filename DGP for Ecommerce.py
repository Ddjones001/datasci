#Import Packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Instantiate Variables


#Initiallize Click-Through Rate And Signup Rate Cost Dictionaries
ct_rate = {'low': 0.01, 'high':np.random.uniform(low=0.01, high= 1.2*0.01)}
su_rate={'low':0.2, 'high':np.random.uniform(low=0.2, high=1.2*0.2)}

#Define a function that simulates the Sign Ups
def get_signups(cost, ct_rate,su_rate,sims):
    lam = np.random.normal(loc=100000,scale=2000,size= sims)
    #Simulate Impressions(poisson), clicks and sign-ups(binomial)
    impressions = np.random.poisson(lam=lam)

    #Feed Impressions into Clicks
    clicks = np.random.binomial(n=impressions,p=ct_rate[cost],size=sims)
    #Feed Clicks into Signups
    signups = np.random.binomial(n=clicks,p=su_rate[cost],size=sims)
    return signups
print("Simulated Sign Ups = {}".format(get_signups('high',ct_rate,su_rate,1)))

#Revenue Flow
def get_revenue(signups):
    rev = []
    np.random.seed(123)
    for s in signups:
        #Model purchases as a binomial, purchase values as an exponential
        purchases = np.random.binomial(s, p=0.1)
        #Uses the outcomes of Signups to determine who will purchase after signing up
        purchase_values = np.random.exponential(scale=1000,size=purchases)
        rev.append(np.sum(purchase_values))
    return rev

print("Simulated Revenue = ${}".format(get_revenue(get_signups('low',ct_rate,su_rate,1))[0]))

#Probability of Losing Money Being the difference of the High and Low Cost Rates Revenue Stream being less that the $3k spent
sims, cost_diff = 10000, 3000

#Get Revenues for both options
rev_low = get_revenue(get_signups('low',ct_rate,su_rate,sims))
rev_high = get_revenue(get_signups('high',ct_rate,su_rate,sims))

#Calculate the fraction of amount of times the rev_high - rev_low is less than the cost diff
frac = sum((np.subtract(rev_high,rev_low)< cost_diff))/sims
print(frac)

randomnum = np.random.binomial(n=8, p=0.8,size=5)
print(randomnum)