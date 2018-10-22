
from variable_finder import find_variables, symbols, Variable, get_symbol
from function_finder import find_more_or_less


class PurchasingProblem:
    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp, with_unit=True)
        # Add last unknown manually because find_unknown_variable only finds one unknown:
        self.variables.append(Variable(symbols[len(self.variables)-1], 'hoes', '?'))

        self.nlp = nlp

    def print_problem(self):
        print('TODO')
