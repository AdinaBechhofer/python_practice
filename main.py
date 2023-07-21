import numpy as np
import matplotlib.pyplot as plt

## put function definitions here 
def readin_data(filename):
    """
    TODO: implement this function to read in the data from filename and return it as a 2D array of floats
    hint: look at documentation for numpy.loadtxt
    """
    pass 

def plot_data_with_smoothing(x, y):
    """
    TODO: implement this function to plot the noisy signal with x array along the x axis and y along the y axis. 
    Find a smoothing method and plot the smooth signal ontop of the noisy one
    """
    pass

if __name__=="__main__":
    ## call functions here
    filename = "data1.txt"
    data = readin_data(filename)
    x = data[0, :]
    y = data[1, :]
    plot_data_with_smoothing(x, y)