from stanfordcorenlp import StanfordCoreNLP
import operator

current_symbol = 0
symbols = {0: 'x', 1: 'y', 2: 'z', 3: 'w', 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i'}

MATH_PROBLEM_KEYWORD_PATH = "mathProblemKeywords.csv"


class Variable:

    def __init__(self, symbol, name, value):
        self.symbol = symbol
        self.name = name
        self.value = value

    def __str__(self):
        return self.symbol + ': ' + str(self.value) + ' ' + self.name


def generate_keyword_dictionary(csv_path):
    keyword_dict = {}
    sentences = open(csv_path, "r", encoding='utf-8').read().split('\n')

    for sentence in sentences:
        words = sentence.split(',')
        for i in range(len(words))[1:]:
            keyword_dict[words[i]] = words[0]

    return keyword_dict


def extract_equation_type(sentence, keyword_dict):

    hits = dict.fromkeys(keyword_dict.values(), 0)

    words = sentence.split(' ')

    for word in words:
        if word in keyword_dict:
            print(f'{word}: {keyword_dict[word]}')
            hits[keyword_dict[word]] += 1

    print(hits)

    return max(hits.items(), key=operator.itemgetter(1))[0]


def get_symbol():
    global current_symbol
    current_symbol += 1
    return symbols[current_symbol - 1]


def reset_symbol_counter():
    global current_symbol
    current_symbol = 0


def sublist_in_list(subList, list, index=0):
    if len(subList) + index > len(list):
        return -1

    for i in range(len(subList)):
        a = subList[i]
        b = list[index + i]
        if a != b:
            return sublist_in_list(subList, list, index + 1)

    return index


def find_unknown_variable(sentence, nlp):
    # Shouldn't this find all unknown variables, instead of just one?
    # Therefore, here we create a list to include all.
    # Still need to find a way to detect all the unknown variables instead of only the first.

    variables = []
    words = nlp.word_tokenize(sentence)
    patterns = [(['how', 'many'], 1)]

    # try and find one of our patterns in the sentence
    for pattern, i in patterns:
        pattern_index = sublist_in_list(pattern, words)
        if pattern_index != -1:
            break

    # pattern: which pattern we found in the sentence
    # i: the index of the pattern we found in the sentence in the list
    # pattern_index: where in the sentence we found the pattern

    name = words[pattern_index + len(patterns[i - 1][0]) + patterns[i - 1][1] - 1]
    variables.append(Variable(get_symbol(), name, "?"))
    return variables


def find_variables(sentence: str = None, nlp=None, with_unit=False, with_percent=False):
    sentences = 'There are 1030 books in the library. We bought 67 more books for the library. How many books are there in the library now?'
    sentences = sentences.lower()
    variables = []
    if sentence is not None:
        sentences = sentence.lower()

    if nlp is None:
        nlp = StanfordCoreNLP('http://localhost', port=9000, lang='en')

    # Find the known variables
    for sentence in sentences.split('.'):
        words = nlp.word_tokenize(sentence)
        dependencies = nlp.dependency_parse(sentence)
        if with_unit or with_percent:
            pos_tag = nlp.pos_tag(sentence)
        nummods = [x for x in dependencies if x[0] == 'nummod']
        for nummod in nummods:
            symbol = get_symbol()

            # Find variables in problems with unit
            # (e.g., spades cost 16 € each, the variable is 'spades' instead of the unit '€')
            if with_unit and len([x for x in pos_tag if x[1] == '$']) > 0 and 'together' not in words:
                for x in reversed(pos_tag[:nummod[1]-1]):
                    if x[1] == 'NNS' or x[1] == 'NNP' or x[1] == 'NN':
                        name = f'{words[nummod[1] - 1]}/{x[0]}'
                        break
            elif with_unit and len([x for x in pos_tag if x[1] == '$']) > 0 and 'together' in words:
                name = words[nummod[1] - 1] + ' total'
            elif with_percent and len([x for x in pos_tag if x[0] == '%']) > 1: # Second sentence (with 2 %)
                for x in pos_tag[nummod[1]:]:
                    if x[1] == 'NNS' or x[1] == 'NNP' or x[1] == 'NN':
                        name = f'{words[nummod[1] - 1]} of {x[0]}'
                        break
            elif with_percent and len([x for x in pos_tag if x[0] == '%']) > 0: # Third sentence (with only one %)
                for x in reversed(pos_tag[:nummod[1]-1]):
                    if x[1] == 'NNS' or x[1] == 'NNP' or x[1] == 'NN':
                        name = f'{words[nummod[1] - 1]} of {x[0]}'
                        break
            else:
                name = words[nummod[1] - 1]
            if ',' in words[nummod[2] - 1]:
                value = float(words[nummod[2] - 1].replace(',','.'))
            else:
                value = int(words[nummod[2] - 1])
            variables.append(Variable(symbol, name, value))

    # Find the unknown variable
    # Now uses extend instead of append; find_unknown_variable returns a list
    variables.extend(find_unknown_variable(sentences.split('.')[-1], nlp))

    reset_symbol_counter()

    return variables

    # Log the results
    print("known variables: ")
    for v in variables[:-1]:
        print(v)
    print("unknown variable: ")
    print(variables[-1])


def extract_equation_type_from_sentence(sentence):
    keyword_dict = generate_keyword_dictionary(MATH_PROBLEM_KEYWORD_PATH)
    equation_type = extract_equation_type(sentence, keyword_dict)

    return equation_type


if __name__ == "__main__":
    find_variables()

    test_sentence = "What is the total cost of the three items?"
    keywordDict = generate_keyword_dictionary(MATH_PROBLEM_KEYWORD_PATH)
    equation_type = extract_equation_type(test_sentence, keywordDict)
    print(equation_type)
