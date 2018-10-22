
from variable_finder import find_variables, symbols
from function_finder import find_more_or_less


class HotelProblem:
    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)

        self.total_hotels = self.variables.pop(0).value

        self.variable_dict = {}

        # assigning variable to hotels
        for i in range(self.total_hotels):
            self.variable_dict[i+1] = symbols[i]

        formula_functions = find_more_or_less(sentence, nlp)

        self.formatted_formulas = []

        # create formula's of the 8 more in a than b
        for i in range(len(formula_functions)):
            formula = formula_functions[i]

            # filter on sentence
            current_variables = self.variables[i*3:(i+1)*3]

            tourist_var = [x for x in current_variables if x.name == 'tourists'][0]
            hotel_vars = [x for x in current_variables if x.name == 'hotel']

            hotelvar1 = self.variable_dict[hotel_vars[0].value]
            hotelvar2 = self.variable_dict[hotel_vars[1].value]

            formatted_formula = formula(hotelvar1, hotelvar2, tourist_var.value)

            self.formatted_formulas.append(formatted_formula)

        # format the final result
        self.format_result_formulas()

    def print_problem(self):
        for sentence in self.formatted_formulas:
            print(sentence)

    def format_result_formulas(self):

        final_variable_name = symbols[self.total_hotels + 1]
        final_formula = f'{final_variable_name} = '

        total_tourist_variable = self.variables[-2]
        self.formatted_formulas.append(f'{final_variable_name} = {total_tourist_variable.value}')

        for i in range(self.total_hotels):

            hotel_var_name = self.variable_dict[i + 1]

            final_formula = f'{final_formula} {hotel_var_name}'

            if i < self.total_hotels - 1:
                final_formula = f'{final_formula} +'

        self.formatted_formulas.append(final_formula)
