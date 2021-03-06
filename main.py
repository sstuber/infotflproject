
from variable_finder import extract_equation_type_from_sentence, find_variables
from addition_problem import AdditionProblem
from division_problem import DivisionProblem
from hotel_problem import HotelProblem
from purchasing_problem import PurchasingProblem
from proportion_problem import ProportionProblem
from train_problem import TrainProblem
from stanfordcorenlp import StanfordCoreNLP
from function_finder import find_more_or_less
from substraction_problem import SubstractionProblem
from multiplication_problem import MultiplicationProblem

def main():
    input_sentence = input('Enter sentence\n')

    equation_type = extract_equation_type_from_sentence(input_sentence)

    nlp = StanfordCoreNLP('http://localhost', port=9000, lang='en')

    print(nlp.pos_tag(input_sentence))
    print(find_more_or_less(input_sentence,nlp))

    print(equation_type)

    # value = find_variables(input_sentence)
    # print(value)

    if equation_type == 'hotel':
        problem = HotelProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'addition':
        problem = AdditionProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'subtraction':
        problem = SubstractionProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'division':
        problem = DivisionProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'multiplication':
        problem = MultiplicationProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'purchasing':
        problem = PurchasingProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'proportion':
        problem = ProportionProblem(input_sentence, nlp)
        problem.print_problem()

    elif equation_type == 'train':
        problem = TrainProblem(input_sentence, nlp)
        problem.print_problem()

    else:
        print(f"The sentence is of type {equation_type} problem, but that is not yet supported by the system")



if __name__ == '__main__':
    main()
