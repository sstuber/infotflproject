
from variable_finder import find_variables


class AdditionProblem:

    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)

    def printProblem(self):
        x = self.variables[0]
        y = self.variables[1]
        z = self.variables[2]

        for variable in self.variables:
            print(variable)

        print(f'Solution: solve {x.symbol} + {y.symbol} = {z.symbol}')

