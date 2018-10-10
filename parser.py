# What is a 'pattern'?
# This code is for solving problems phrased in the following two exact forms:
# A is $42. A is $14 less than B. How much is B?
# A is $42. B is $14 less than A. How much is B?

from stanfordcorenlp import StanfordCoreNLP
import pickle
from collections import OrderedDict
import sys
from substraction_problem import SubstractionProblem


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




def  main():
    if len(sys.argv) > 1:
        sentence = sys.argv[1]
        print(sys.argv)
        pickle.dump(sentence, open("sentence.p", "wb"))
        first_run(sentence)

    sentence = pickle.load(open("sentence.p", "rb"))

    # sentence = 'Jane spent $42 for shoes.  This was $14 less than what she spent for a blouse.  How much was the blouse?'
    # tokenized, pos_tags, ner, problem = first_run(sentence)


    tokenized, pos_tags, ner, problem = load_from_pickle(sentence)
    # print(tokenized)
    # print(pos_tags)
    # print(ner)
    # print(problem)
    substract = SubstractionProblem(problem)

    print(substract.solve_problem())


if __name__ == "__main__":
    main()


