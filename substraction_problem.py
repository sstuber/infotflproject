
from collections import OrderedDict


class SubstractionProblem:
    def __init__(self, pos_tag_list):
        self.pos_tag = pos_tag_list

        self.objects = [x[0] for x in pos_tag_list if x[1] == 'NNS' or x[1] == 'NN']
        self.numbers = [float(y[0]) for y in pos_tag_list if y[1] == 'CD']

        self.objects = list(OrderedDict.fromkeys(self.objects))
        dictionary = {}

        for i in range(len(self.objects)):
            dictionary[self.objects[i]] = self.numbers[i]

        self.object_to_number_dict = dictionary

    def solve_problem(self):

        result = None
        index = [self.pos_tag.index(x) for x in self.pos_tag if x[0] == 'less'][0]
        smaller_one = None
        for i in reversed(range(0, index)):
            if self.pos_tag[i][1] == 'NNS' or self.pos_tag[i][1] == 'NN':
                smaller_one = self.pos_tag[i][0]
                break

        bigger_one = None
        for i in range(index, len(self.pos_tag)):
            if self.pos_tag[i][1] == 'NNS' or self.pos_tag[i][1] == 'NN':
                bigger_one = self.pos_tag[i][0]
                break

        last_key = self.objects[-1]

        if smaller_one is not None:
            # A is $42. A is $14 less than B. How much is B?
            # Jane spent $42 for shoes.  This was $14 less than what she spent for a blouse.  How much was the blouse?
            # e.g., operand is 14 here
            operand = self.object_to_number_dict[last_key]



            if last_key != smaller_one:
                result = operand + self.object_to_number_dict[smaller_one]
            else:
                result = self.object_to_number_dict[bigger_one] - operand

            # Jane spent $42 for shoes.  The blouse was $14 less than what she spent for the shoes.  How much was the blouse?
            # A is $42. B is $14 less than A. How much is B?

        return result
