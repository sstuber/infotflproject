
from variable_finder import find_variables


class SubstractionProblem:
    def __init__(self, sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)

    def print_problem(self):
        x = self.variables[0]
        y = self.variables[1]
        z = self.variables[2]

        if x.value < y.value:
            smaller_variable = x
            bigger_variable = y
        else:
            smaller_variable = y
            bigger_variable = x

        for variable in self.variables:
            print(variable)

        print(f'Solution: solve {bigger_variable.symbol} - {smaller_variable.symbol} = {z.symbol}')

