
from variable_finder import extract_equation_type_from_sentence
from addition_problem import AdditionProblem

def main():
    input_sentence = input('Enter senntence\n')

    equation_type = extract_equation_type_from_sentence(input_sentence)

    if equation_type == 'addition':
        problem = AdditionProblem(input_sentence)
        problem.printProblem()
        

if __name__ == '__main__':
    main()
