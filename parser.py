
from stanfordcorenlp import StanfordCoreNLP


if __name__ == "__main__":
    nlp = StanfordCoreNLP('http://localhost', port=9000, lang='en')

    sentence = 'The tourists are accommodated in 3 hotels. There are 8 more tourists in the second hotel than in the first hotel and in the third hotel there are 14 more tourists than in the second one. If there is a total of 258 tourists, how many tourists are accommodated in each of the hotels ?'
    print(nlp.word_tokenize(sentence))

    nlp.close()
