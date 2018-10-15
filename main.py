
from variable_finder import extract_equation_type_from_sentence
from addition_problem import AdditionProblem
from division_problem import DivisionProblem

def main():
    input_sentence = input('Enter senntence\n')

    equation_type = extract_equation_type_from_sentence(input_sentence)

    print(equation_type)

    if equation_type == 'addition':
        problem = AdditionProblem(input_sentence)
        problem.print_problem()

    if equation_type == 'division':
        problem = DivisionProblem(input_sentence)
        problem.print_problem()


if __name__ == '__main__':
    main()
