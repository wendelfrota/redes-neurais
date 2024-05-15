from math import inf


def activation(sum):
    return 1 if sum >= 0 else 0


def train_perceptron(input, output_desire, learning_rate, input_weight, bias_weight, bias):
    error = inf
    iteration = 0

    while not error == 0:
        iteration += 1

        sum = (input * input_weight) + (bias * bias_weight)
        output = activation(sum)

        # Calculate error
        error = output_desire - output

        # Show information
        print('input: ', input)
        print('output_desire: ', output_desire)
        print('weight: ', input_weight)
        print('output: ', output)
        print('error: ', error, '\n')

        # Update weights
        if not error == 0:
            input_weight = input_weight + (learning_rate * input * error)
            bias_weight = bias_weight + (learning_rate * bias * error)

    print('iteration: ', iteration)


# Parameters
input = 1
output_desire = 0
learning_rate = 0.01
input_weight = 0.5

bias = 1
bias_weight = 0.5

train_perceptron(input, output_desire, learning_rate, input_weight, bias_weight, bias)