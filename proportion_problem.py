
from variable_finder import find_variables, symbols, Variable, get_symbol
from function_finder import find_more_or_less
'''
The factory has 1440 employees (men and women). For above-average results 18,75 % of all men and 22,5 % of all women received the bonus. The total amount of awarded employees is 20 % . How many men and how many women are employed in the factory ?
'''
class ProportionProblem:
    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp, with_percent=True)
        # Add last unknown manually because find_unknown_variable only finds one unknown:
        self.variables.append(Variable(symbols[len(self.variables)], self.variables[2].name[5:], '?'))

        self.total_amount = self.variables[0]
        self.total_proportion = self.variables[-3]
        self.unknown_variables = self.variables[-2:]
        self.proportions = self.variables[1:-len(self.unknown_variables)-1]

        self.nlp = nlp

    def print_problem(self):
        for variable in self.variables:
            print(variable)

        print(self.unknown_variables[0].symbol + ' + ' + self.unknown_variables[1].symbol + ' = ' + self.total_amount.symbol)
        print(self.proportions[0].symbol + '% * ' + self.unknown_variables[0].symbol + ' + ' + self.proportions[1].symbol + '% * ' + self.unknown_variables[1].symbol + ' = ' + self.total_proportion.symbol + '% * ' + self.total_amount.symbol)

        print('Hint:')
        print(self.unknown_variables[0].symbol + ' + ' + self.unknown_variables[1].symbol + ' = ' + str(self.total_amount.value))
        print(str(self.proportions[0].value) + '% * ' + self.unknown_variables[0].symbol + ' + ' + str(self.proportions[1].value) + '% * ' + self.unknown_variables[1].symbol + ' = ' + str(self.total_proportion.value) + '% * ' + str(self.total_amount.value))


