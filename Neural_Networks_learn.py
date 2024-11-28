# One Weights Nural

# inputs = [1,2,3]

# weights = [0.2,0.8,-0.5]

# bias = 2

# output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

# print(output)

# ............................................................................................

# Three Weights Nural 

# inputs = [1,2,3,2.5]

# weights1 = [0.2,0.8,-0.5,1.0]
# weights2 = [0.5,-0.91,0.26,-0.5]
# weights3 = [-0.26,-0.27,0.17,0.87]

# bias1 = 2
# bias2 = 3
# bias3 = 0.5

# output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
#           inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
#           inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]
# print(output)

# ............................................................................................

# Three Weights Nural Dynamic 

# inputs = [1, 2, 3, 2.5]

# weight = [[0.2, 0.8, -0.5, 1.0],
#           [0.5, -0.91, 0.26, -0.5],
#           [-0.26, -0.27, 0.17, 0.87]]

# bias = [2, 3, 0.5]

# layer_output = []
# for neuron_weights, neuron_bias in zip(weight, bias):
#     neuron_output = 0
    
# print(neuron_weights)
# print(neuron_bias)

#     for n_input, w in zip(inputs, neuron_weights):
#         neuron_output += n_input * w
#     neuron_output += neuron_bias
#     layer_output.append(neuron_output)

# print (layer_output)

# ............................................................................................


# # Softmax Activation
# import math
# import numpy as np

# layer_output = [4.8, 1.21, 2.385]
# E = math.e

# # exp_values = []
# # for outout in layer_output:
# #     exp_values.append(E**outout)

# exp_values = np.exp(layer_output)

# # norm_base = sum(exp_values)
# # norm_values = []

# # for value in exp_values:
# #     norm_values.append (value / norm_base)

# norm_values = exp_values / np.sum(exp_values)

# print(norm_values)
# print(sum(norm_values))

# ............................................................................................

# Softmax Activation
# import numpy as np

# layer_output = [[4.8, 1.21, 2.385],
#                 [8.9, -1.81, 0.2],
#                 [1.41, 1.051, 0.026]]

# exp_values = np.exp(layer_output)
# norm_values = exp_values / np.sum(exp_values, axis= 1, keepdims= True)

# print(norm_values)

# ............................................................................................

import math

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

print(loss)

print(-math.log(0.7))
print(-math.log(0.5))