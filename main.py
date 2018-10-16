
from variable_finder import extract_equation_type_from_sentence, find_variables
from addition_problem import AdditionProblem
from division_problem import DivisionProblem
from hotel_problem import HotelProblem

# The tourists are accommodated in 3 hotels. There are 8 more tourists in hotel 2 than in hotel 1 and in hotel 3 there are 14 more tourists than in hotel 2. If there is a total of 258 tourists, how many tourists are accommodated in each of the hotels ?

def main():
    input_sentence = input('Enter senntence\n')

    equation_type = extract_equation_type_from_sentence(input_sentence)

    print(equation_type)

    # value = find_variables(input_sentence)
    # print(value)

    hotel_problem = HotelProblem(input_sentence)

    hotel_problem.print()

    return


    if equation_type == 'addition':
        problem = AdditionProblem(input_sentence)
        problem.print_problem()

    if equation_type == 'division':
        problem = DivisionProblem(input_sentence)
        problem.print_problem()


if __name__ == '__main__':
    main()