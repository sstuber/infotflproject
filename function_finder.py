from stanfordcorenlp import StanfordCoreNLP


def find_more_or_less(sentence, nlp = None):

    if nlp is None:
        StanfordCoreNLP('http://localhost', port=9000, lang='en')

    pos_tags = nlp.pos_tag(sentence)

    addition_functions_name_tuples = filter(lambda x: x[1] == 'JJR', pos_tags)

    addition_functions_name = list(map(lambda x: x[0], addition_functions_name_tuples))

    print(list(addition_functions_name))

    variable_dict = {
        'more': more_than_function,
        'less': less_than_function
    }

    variable_function_funcitons = []

    for name  in addition_functions_name:
        if name in variable_dict:
            selected_function = variable_dict[name]
            variable_function_funcitons.append(selected_function)

        else:
            print('function miss spelled used addition')
            selected_function = variable_dict['more']
            variable_function_funcitons.append(selected_function)

    return variable_function_funcitons


def more_than_function(variable_name1, variable_name2, value):

    return f'{variable_name1} = {variable_name2} + {value}'


def less_than_function(variable_name1 , variable_name2, value):
    return f'{variable_name1} = {variable_name2} - {value}'
