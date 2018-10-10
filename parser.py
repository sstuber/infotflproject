# What is a 'pattern'?
# This code is for solving problems phrased in the following two exact forms:
# A is $42. A is $14 less than B. How much is B?
# A is $42. B is $14 less than A. How much is B?

from stanfordcorenlp import StanfordCoreNLP
import pickle
from collections import OrderedDict
import sys


def first_run(sentence):
    print("loading NLP")
    nlp = StanfordCoreNLP('http://localhost', port=9000, lang='en')
    print("tokenizing")
    tokenized = nlp.word_tokenize(sentence)
    print(tokenized)
    pickle.dump(tokenized, open("tokenized.p", "wb"))
    print("tagging")
    pos_tags = nlp.pos_tag(sentence)
    print(pos_tags)
    pickle.dump(pos_tags, open("pos_tags.p", "wb"))

    ner = nlp.ner(sentence)
    print(ner)
    pickle.dump(ner, open("ner.p", "wb"))

    # print(nlp.parse(sentence))
    # print(nlp.dependency_parse(sentence))

    problem = nlp.pos_tag(sentence)
    pickle.dump(problem, open("problem.p", "wb"))
    nlp.close()

    return tokenized, pos_tags, ner, problem


def load_from_pickle(sentence):
    tokenized = pickle.load(open("tokenized.p", "rb"))
    pos_tags = pickle.load(open("pos_tags.p", "rb"))
    ner = pickle.load(open("ner.p", "rb"))
    problem = pickle.load(open("problem.p", "rb"))

    return tokenized, pos_tags, ner, problem


if __name__ == "__main__":

    if len(sys.argv) > 1:
        sentence = sys.argv[1]
        print(sys.argv)
        pickle.dump(sentence, open("sentence.p", "wb"))
        first_run(sentence)

    sentence = pickle.load(open("sentence.p", "rb"))

    # sentence = 'Jane spent $42 for shoes.  This was $14 less than what she spent for a blouse.  How much was the blouse?'
    # tokenized, pos_tags, ner, problem = first_run(sentence)


    tokenized, pos_tags, ner, problem = load_from_pickle(sentence)
    print(tokenized)
    print(pos_tags)
    print(ner)
    print(problem)

    objects = [x[0] for x in problem if x[1] == 'NNS' or x[1] == 'NN']
    prices = [float(y[0]) for y in problem if y[1] == 'CD']
    print(objects)
    print(prices)

    last_key = objects[-1]

    dictionary = {}

    objects = list(OrderedDict.fromkeys(objects))
    print(objects)
    for i in range(len(objects)):
        dictionary[objects[i]] = prices[i]

    if 'less' in tokenized:
        # get position of less
        index = [problem.index(x) for x in problem if x[0] == 'less'][0]
        smaller_one = None
        for i in reversed(range(0, index)):
            if problem[i][1] == 'NNS' or problem[i][1] == 'NN':
                smaller_one = problem[i][0]
                break

        bigger_one = None
        for i in range(index, len(problem)):
            if problem[i][1] == 'NNS' or problem[i][1] == 'NN':
                bigger_one = problem[i][0]
                break

        if smaller_one is not None:
            # A is $42. A is $14 less than B. How much is B?
            # Jane spent $42 for shoes.  This was $14 less than what she spent for a blouse.  How much was the blouse?
            # e.g., operand is 14 here
            operand = dictionary[last_key]

            if last_key != smaller_one:
                dictionary[last_key] = operand + dictionary[smaller_one]
            else:
                dictionary[last_key] = dictionary[bigger_one] - operand

            # Jane spent $42 for shoes.  The blouse was $14 less than what she spent for the shoes.  How much was the blouse?
            # A is $42. B is $14 less than A. How much is B?

    print(dictionary)


