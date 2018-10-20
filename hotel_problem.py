
from variable_finder import find_variables, symbols


class HotelProblem:
    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)

        self.total_hotels = self.variables.pop(0).value

        self.variable_dict = {}

        # assigning variable to hotels
        for i in range(self.total_hotels):
            self.variable_dict[i+1] = symbols[i]

        times_of_formulas = int(len(self.variables) / 3)

        self.total_formulas = []

        # create formula's of the 8 more in a than b
        for i in range(times_of_formulas):

            current_variables = self.variables[i*3:(i+1)*3]

            tourist_var = [x for x in current_variables if x.name == 'tourists'][0]
            hotel_vars = [x for x in current_variables if x.name == 'hotel']

            hotelvar1 = self.variable_dict[hotel_vars[0].value]
            hotelvar2 = self.variable_dict[hotel_vars[1].value]

            self.total_formulas.append(f'{hotelvar1} = {hotelvar2} + {tourist_var.value}')

        final_variable_name = symbols[self.total_hotels + 1]

        # last one is "unknown" and second to last is last indication of total
        total_tourist_variable = self.variables[-2]

        self.total_formulas.append(f'{final_variable_name} = {total_tourist_variable.value}')

        final_formula = f'{final_variable_name} = '

        for i in range(self.total_hotels):

            hotel_var_name = self.variable_dict[i+1]

            final_formula = f'{final_formula} {hotel_var_name}'

            if i < self.total_hotels - 1:
                final_formula = f'{final_formula} +'

        self.total_formulas.append(final_formula)

    def print_problem(self):
        for sentence in self.total_formulas:
            print(sentence)


