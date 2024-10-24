import numpy as np

# Define the neuron computation function
def neuron_comp(x, y, bias):
    weighted_sum = np.dot(x, y) + bias  # Calculate weighted sum with bias
    if weighted_sum > 0:
        print("1")
    else:
        print("0")

# Input values
x = [0.2, 0.5]
y = [0.4, 0.5]
bias = 3

# Call the neuron function
neuron_comp(x, y, bias)
