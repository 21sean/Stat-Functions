from math import sqrt
from random import *
L = [65,25,100,85,68]


def computeAvg(list):
    """compute the average of a list.
       # >>> computeAvg (L)
        The average of my list is: 3.5
        Params: a (list)
        Returns: (float)
    """
    n = sum(list)
    m = len(list)
    return n/m


def variance(a):
    """compute the variance of a list by computing the sum of the difference of each
            element and the mean.
           # >>> variance (L)
            The variance of my list is: 2.9166666666666665
            Params: a (list)
            Returns: (float)
    """
    var = []
    for i in a:
        var.append((i - computeAvg(a)) ** 2)
    return computeAvg(var)


def standardDeviation (a):
    """compute the standard Deviation of a list by taking the sqrt of the variance.
           # >>> standardDeviation (L)
            The Standard Deviation of my list is: 1.707825127659933
            Params: a (list)
            Returns: (float)
    """
    return sqrt(variance(a))


print("The average of my list is:", computeAvg(L))
print("The variance of my list is:",  variance(L))
print("The Standard Deviation of my list is:", standardDeviation(L))


#--------------------------------------------------------------------------------------
def coinExperiment (a):
    """Simulate an experiment of a coin flips.
        Params:
        n (int): # coin flips
        p (float): probability of heads
        Returns: (int) # heads
        """
    nh = 0
    for i in range(100):
        nh += random() < a
    return nh

def repeatExperiment(a):
    """Simulate an experiment of n coin flips.
    Params:
    n (int): # coin flips
    p (float): probability of heads
    Returns: (int) # heads
    """
    heads = []
    for i in range(1000):
        heads.append(coinExperiment(a))
    return heads


normalSim = repeatExperiment(.5)
print("----------------------------------------------------------------------------------------")
print("For this trial: 1000 simulations, and 100 coin flips per sim.")
print("The coin had a weight of 0.5")
print("The average result from the trials was:", computeAvg(normalSim))
print("The variance was:", variance(normalSim))
print("The Standard Deviation of your trial is:", standardDeviation(normalSim))
rigged = repeatExperiment(.7)
print("----------------------------------------------------------------------------------------")
print("For this trial: 1000 simulations, and 100 coin flips per sim.")
print("The coin had a weight of 0.7 ~ Rigged")
print("The average result from the trials was:", computeAvg(rigged))
print("The variance was:", variance(rigged))
print("The Standard Deviation of your trial is:", standardDeviation(rigged))
