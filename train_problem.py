from variable_finder import find_variables, symbols

"""
A local train has departed from the station A at ten o'clock with the speed of 55 km/h. 1,5 h later an express has departed from the station B, which is 360 km far from the station A, and it went toward the local train with the speed of 130 km/h. At what time and how far from the station A will the trains meet ?
"""


class TrainProblem:
    def __init__(self, sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)
        self.nlp = nlp
        
        self.variable_dict = {}