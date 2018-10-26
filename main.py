
from variable_finder import extract_equation_type_from_sentence, find_variables
from addition_problem import AdditionProblem
from division_problem import DivisionProblem
from hotel_problem import HotelProblem
from purchasing_problem import PurchasingProblem
from proportion_problem import ProportionProblem
from stanfordcorenlp import StanfordCoreNLP
from function_finder import find_more_or_less
from substraction_problem import SubstractionProblem
from multiplication_problem import MultiplicationProblem

# The tourists are accommodated in 3 hotels. There are 8 less tourists in hotel 2 than in hotel 1 and in hotel 3 there are 14 more tourists than in hotel 2. If there is a total of 258 tourists, how many tourists are accommodated in each of the hotels ?

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

    if equation_type == 'addition':
        problem = AdditionProblem(input_sentence, nlp)
        problem.print_problem()

    if equation_type == 'subtraction':
        problem = SubstractionProblem(input_sentence, nlp)
        problem.print_problem()

    if equation_type == 'division':
        problem = DivisionProblem(input_sentence, nlp)
        problem.print_problem()

    if equation_type == 'multiplication':
        problem = MultiplicationProblem(input_sentence, nlp)
        problem.print_problem()

    if equation_type == 'purchasing':
        problem = PurchasingProblem(input_sentence, nlp)
        problem.print_problem()

    if equation_type == 'proportion':
        problem = ProportionProblem(input_sentence, nlp)
        problem.print_problem()


if __name__ == '__main__':
    main()
