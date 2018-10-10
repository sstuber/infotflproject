from stanfordcorenlp import StanfordCoreNLP

current_symbol = 0
symbols = {0: 'x', 1: 'y', 2: 'z', 3: 'w'}


class Variable:

    def __init__(self, symbol, name, value):
        self.symbol = symbol
        self.name = name
        self.value = value

    def __str__(self):
        return self.symbol + ': ' + str(self.value) + ' ' + self.name


def get_symbol():

    global current_symbol
    current_symbol += 1
    return symbols[current_symbol - 1]


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
    return Variable(get_symbol(), name, "?")


def find_variables():
    sentences = 'There are 1030 books in the library. We bought 67 more books for the library. How many books are there in the library now?'
    sentences = sentences.lower()
    variables = []

    nlp = StanfordCoreNLP('http://localhost', port=9000, lang='en')

    # Find the known variables
    for sentence in sentences.split('.'):
        words = nlp.word_tokenize(sentence)
        dependencies = nlp.dependency_parse(sentence)
        nummods = [x for x in dependencies if x[0] == 'nummod']
        for nummod in nummods:
            symbol = get_symbol()
            name = words[nummod[1] - 1]
            value = int(words[nummod[2] - 1])
            variables.append(Variable(symbol, name, value))


    # Find the unknown variable
    variables.append(find_unknown_variable(sentences.split('.')[-1], nlp))

    # Log the results
    print("known variables: ")
    for v in variables[:-1]:
        print(v)
    print("unknown variable: ")
    print(variables[-1])


find_variables()