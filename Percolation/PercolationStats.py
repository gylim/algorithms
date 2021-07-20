import Percolation
from random import randint as ri
from math import sqrt

def PercolationStats(n, trials):
    pc = Percolation.Percolation(n)
    threshold = []
    for i in range(trials):
        while pc.percolates() == False:
            pc.open(ri(1,n), ri(1,n))
        threshold.append(pc.numberOfOpenSites()/(n**2))
    print(" %-45s %-3s %-45s" % ("mean", "=", mean(threshold, trials)))
    print(" %-45s %-3s %-45s" % ("stddev", "=", stddev(threshold, trials)))
    print(" %-45s %-3s %-45s" % ("mean", "=", [confidenceLo(threshold, trials), confidenceHi(threshold, trials)]))

def mean(threshold, trials):
    return sum(threshold)/trials

def stddev(threshold, trials):
    return sqrt(sum([lambda x: (x-mean())**2 for x in threshold])/(trials-1))

def confidenceLo(threshold, trials):
    return mean(threshold, trials) - 1.96*stddev(threshold, trials)/sqrt(trials)

def confidenceHi(threshold, trials):
    return mean(threshold, trials) + 1.96*stddev(threshold, trials)/sqrt(trials)

if __name__ == "__main__":
    inputs = input("Key in size of grid and number of trials separated by space: ").split(" ")
    n, trials = int(inputs[0]), int(inputs[1])
    if n <= 0 or trials <= 0:
        print("The size of grid and number of trials must be greater than 0!")
        exit
    else:
        PercolationStats(n, trials)