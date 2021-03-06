
from variable_finder import find_variables, symbols
from function_finder import find_more_or_less

#  The tourists are accommodated in 3 hotels. There are 8 less tourists in hotel 2 than in hotel 1 and in hotel 3 there are 14 more tourists than in hotel 2. If there is a total of 258 tourists, how many tourists are accommodated in each of the hotels ?
class HotelProblem:
    def __init__(self,sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)
        self.nlp = nlp

        self.total_hotels = self.variables.pop(0).value

        self.variable_dict = {}

        # assigning variable to hotels
        for i in range(self.total_hotels):
            self.variable_dict[i+1] = symbols[i]

        first_plural_noun, first_singular_noun = self.get_variable_nouns()

        self.formatted_formulas = []
        formula_functions = find_more_or_less(sentence, nlp)

        # create formula's of the 8 more in a than b
        for i in range(len(formula_functions)):
            formula = formula_functions[i]

            # filter on sentence
            current_variables = self.variables[i*3:(i+1)*3]

            tourist_var = [x for x in current_variables if x.name == first_plural_noun][0]
            hotel_vars = [x for x in current_variables if x.name == first_singular_noun]

            hotelvar1 = self.variable_dict[hotel_vars[0].value]
            hotelvar2 = self.variable_dict[hotel_vars[1].value]

            formatted_formula = formula(hotelvar1, hotelvar2, tourist_var.value)

            self.formatted_formulas.append(formatted_formula)

        # format the final result
        self.format_result_formulas()

    def get_variable_nouns(self):

        pos_tags = self.nlp.pos_tag(self.sentence)

        nouns = list(filter(lambda x: x[1] == 'NNS' or x[1] == 'NN', pos_tags))

        first_plural_noun = None
        for noun in nouns:
            if noun[1] == 'NNS':
                first_plural_noun = noun[0]
                break

        first_singular_noun = None
        for noun in nouns:
            if noun[1] == 'NN':
                first_singular_noun = noun[0]
                break

        return first_plural_noun,first_singular_noun

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
