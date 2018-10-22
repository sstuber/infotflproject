
from variable_finder import find_variables, symbols, Variable, get_symbol
from function_finder import find_more_or_less

# The workshop purchased 40 pieces of garden tools. Spades cost 16 € each and hoes cost 18 € each. The price of all tools together was 690 €. Calculate how many spades and how many hoes did the workshop purchase?
# or (Caveman version):
# Purchased 40 things. Rocks cost 16 € each and cows cost 18 € each. Together 690 €. How many rocks how many cows purchase?
class PurchasingProblem:
    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp, with_unit=True)
        # Add last unknown manually because find_unknown_variable only finds one unknown:
        self.variables.append(Variable(symbols[len(self.variables)], self.variables[2].name[2:], '?'))

        self.total_objects = self.variables[0]
        self.total_price = self.variables[-3]
        self.unknown_variables = self.variables[-2:]
        self.prices = self.variables[1:-3]

        self.nlp = nlp

    def print_problem(self):
        for variable in self.variables:
            print(variable)

        print(self.unknown_variables[0].symbol + ' + ' + self.unknown_variables[1].symbol + ' = ' + self.total_objects.symbol)
        print(self.unknown_variables[0].symbol + ' * ' + self.prices[0].symbol + ' + ' + self.unknown_variables[1].symbol + ' * ' + self.prices[1].symbol + ' = ' + self.total_price.symbol)

        print('Hint:')
        print(self.unknown_variables[0].symbol + ' + ' + self.unknown_variables[1].symbol + ' = ' + str(self.total_objects.value))
        print(self.unknown_variables[0].symbol + ' * ' + str(self.prices[0].value) + ' + ' + self.unknown_variables[1].symbol + ' * ' + str(self.prices[1].value) + ' = ' + str(self.total_price.value))


