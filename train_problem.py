from variable_finder import find_variables, symbols, sublist_in_list, Variable, get_symbol

"""
Restrictions:
    * only 2 objects
    * object speed expressed in km/h
    * 1 distance between them expressed in km  TODO make optional
    * (optional) 1 time difference between them expressed in h
    * (to improve) assumes that the starting point is the first object mentioned

Example:
    A local train has departed from the station A at ten o'clock with the speed of 55 km/h. 1,5 h later an express has departed from the station B, which is 360 km far from the station A, and it went toward the local train with the speed of 130 km/h. At what time and how far from the station A will the trains meet ?
    Variation: A local train has departed from the station A at ten o'clock with the speed of 55 km/h. An express has departed from the station B, which is 360 km far from the station A, and it went toward the local train with the speed of 130 km/h. At what time and how far from the station A will the trains meet ?
    Variation: A local train has departed from the station A at ten o'clock with the speed of 55 km/h. 1,5 h later an express has departed from the station B, and it went toward the local train with the speed of 130 km/h. At what time and how far from the station A will the trains meet ?
    Variation: A local train has departed from the station A at ten o'clock with the speed of 55 km/h. An express has departed from the station B, which is 360 km far from the station A, and it went toward the local train with the speed of 130 km/h. How far from the station A will the trains meet ?
    Variation: A local train has departed from the station A at ten o'clock with the speed of 55 km/h. An express has departed from the station B, which is 360 km far from the station A, and it went toward the local train with the speed of 130 km/h. At what time will the trains meet ?
    DOESN'T WORK YET: The distance between towns A and B is 42 km. A pedestrian leaves town A with a speed of 6 km/h, to the opposite direction from town B. A cyclist leaves town B 0,5 h later than the pedestrian with a speed of 24 km/h. In how many hours is the cyclist going to reach the pedestrian and what is going to be his distance from town B ?
        # Issues:
            Detect "what is going to be his distance" as a question (too long)
            Detect town B as point of reference
    
"""


class TrainProblem:
    def __init__(self, sentence, nlp=None):
        self.sentence = sentence
        self.variables = find_variables(sentence, nlp)
        self.nlp = nlp
        
        # Data
        trains = []
        time_difference = None
        initial_distance = None
        # Questions
        time_meeting = None
        distance_meeting = None
        
        questions = self.find_questions()
        assert len(questions) > 0
        
        self.variables += questions
        for variable in self.variables:
            name = variable.name
            if name == "km/h":
                trains.append(variable)
            elif name == "h":
                time_difference = variable
            elif name == "km":
                initial_distance = variable
            elif name == "time":
                time_meeting = variable
            elif name == "distance":
                distance_meeting = variable
        assert len(trains) == 2
        assert time_difference or initial_distance
       

        self.formatted_formulas = []
        self.formatted_formulas.append("# Data #")
        self.formatted_formulas.append(
                f"trains: {trains[0]} and {trains[1]}")
        if initial_distance:
            self.formatted_formulas.append(
                f"initial distance: {initial_distance}")
        if time_difference:
            self.formatted_formulas.append(
                f"time difference: {time_difference}")
        
        if not time_meeting:
            time_meeting = Variable(get_symbol(), "time", "(auxiliar)")
#        if not distance_meeting:
#            distance_meeting = Variable(get_symbol(), "distance", "(auxiliar)")

        self.formatted_formulas.append(str(time_meeting))
        if distance_meeting:
            self.formatted_formulas.append(str(distance_meeting))


        self.formatted_formulas.append("# Solution #")        
        t1_meeting_distance = f"{trains[0].symbol} * {time_meeting.symbol}"
        e1 = t1_meeting_distance
        t1_initial_distance = None
        if time_difference:
            t1_initial_distance = f"{trains[0].symbol} * {time_difference.symbol}"
            e1 += f" + {t1_initial_distance}"
        
        t2_symbol = f"{trains[1].symbol}"
        t2_symbol_neg = f"(-{t2_symbol})"
        t2_initial_distance = None
        if initial_distance:
            t2_symbol = t2_symbol_neg
            t2_symbol_neg = f"{trains[1].symbol}"
            t2_initial_distance = f"{initial_distance.symbol}"
            
        t2_meeting_distance = f"{t2_symbol} * {time_meeting.symbol}"
        e2 = t2_meeting_distance
        if initial_distance:
            e2 += f" + {t2_initial_distance}"

        if distance_meeting:
            self.formatted_formulas.append(f"{distance_meeting.symbol} = {e1}")
            self.formatted_formulas.append(f"{distance_meeting.symbol} = {e2}")
        
        # The trains meet when they are at the same position    
        self.formatted_formulas.append(f"{e1} = {e2}")
        
        
        """
        # Isolate time
        t2_symbol_neg = f"{trains[1].symbol}"
        e1 = f"{t1_meeting_distance} - ({t2_meeting_distance})"
        e2 = ""
        if t2_initial_distance:
            e2 += f"{t2_initial_distance}"
        if t1_initial_distance:
            if t2_initial_distance:
                e2 += " "
            e2 += f"- ({t1_initial_distance})"
        self.formatted_formulas.append(f"{e1} = {e2}")
        
        #TODO Make initial_distance optional
        sum_speeds = f"{trains[0].symbol} + {trains[1].symbol}"
        e1 = f"{time_meeting.symbol} * ({sum_speeds})"
        self.formatted_formulas.append(f"{e1} = {e2}")
        e1 = f"{time_meeting.symbol}"
        e2 = f"({e2})/({sum_speeds})"
        self.formatted_formulas.append(f"{e1} = {e2}")
        """
        
    def print_problem(self):
        for sentence in self.formatted_formulas:
            print(sentence)

    def find_questions(self):
        words = self.nlp.word_tokenize(self.sentence.lower())
        
        for variable in self.variables:
            # Advance symbol counter (TODO find questions together with variables)
            get_symbol()
            
        # Accepted questions
        patterns = {
                'what time' : "time",
                'how far' : "distance"
                }
        
        questions = []
        for pattern in patterns:
            pattern_index = sublist_in_list(pattern.split(" "), words)
            if pattern_index != -1:
                questions.append(Variable(get_symbol(), patterns[pattern], "?"))
        return questions
        
        
