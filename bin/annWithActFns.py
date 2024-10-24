import numpy as np
def neuron_comp(x, y, bias, activation_function):
    weighted_sum = np.dot(x, y) + bias  

    if activation_function == 'sigmoid':
        output = 1 / (1 + np.exp(-weighted_sum))
    elif activation_function == 'relu':
        output = max(0, weighted_sum)
    elif activation_function == 'tanh':
        output = np.tanh(weighted_sum)
    elif activation_function == 'linear':
        output = weighted_sum
    else:
        raise ValueError("Unknown activation function")

    return output


x = [0.2, 0.5]
y = [0.4, 0.5]
bias = 3


print("Sigmoid Value:", neuron_comp(x, y, bias, "sigmoid"))
print("ReLU Value:", neuron_comp(x, y, bias, "relu"))
print("Tanh Value:", neuron_comp(x, y, bias, "tanh"))
print("Linear Value:", neuron_comp(x, y, bias, "linear"))

