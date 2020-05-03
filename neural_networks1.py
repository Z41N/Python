'''
# Creating a neural network
# Creating neurons with a connection to each (parameters)
# Layer 1 = Inputs
# Layer X = Last layer = Output layer

# These are our unique inputs (FOR ONLY ONE NEURON!)
# These can be values from the input layer OR could be just the one neuron
# Ex. Predicting failure or pass of a computer network
# Each unique value from these inputs could be a value from a different sensor in a group

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

# This tells us we have 3 neurons (since 3 sets of weights). That's why we do weights in dot product first below.
weights = [[0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# Adding another set of weights and biases = another layer!
weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]

# Put weights as the first argument as it is a matrix (list of lists[lol]).
# This is also the INPUTS for LAYER 2!
layer_1_outputs = np.dot(inputs, np.array(weights).T) + biases

layer_2_outputs = np.dot(layer_1_outputs, np.array(weights2).T) + biases2
print(layer_2_outputs)
'''

# Now, we made 2 layers in a long way. We should do it as OBJECT instead.

import numpy as np

np.random.seed(0)
# We can give the computer inputs. But the hidden layers we're about to make are up to the computer.
X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer_1 = Layer_Dense(4, 5)
layer_2 = Layer_Dense(5, 2)
layer_1.forward(X)
# print(layer_1.output)
layer_2.forward(layer_1.output)
# print(layer_2.output)


# We are just passing data (inputs, weights, biases) and create a class to handle this. 
# Now we know how these values work with numpy, and about the shape of our values.
