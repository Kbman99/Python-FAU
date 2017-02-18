def input_tuple_lc(prompt: str, types: tuple, sep: str):
    print("**Using list comprehension**\n")
    answers = input(prompt + "\n**Please use '" + sep + "' to separate your responses**: ")
    answers_list = list(answers.split(sep))
    try:
        answer_objects = check_tokens_lc(types, answers_list)
    except TypeError as err:
        print(err)
        return ()
    except ValueError as err:
        print(err)
        return ()
    return answer_objects


def check_tokens_lc(types: tuple, answers: list):
    if len(types) == len(answers):
        # This works unless a bool
        answers_list = [types[i](answers[i]) if types[i] != bool else str_to_bool(answers[i])
                        for i in range(len(types))]
    else:
        raise ValueError("Value Error! Incorrect amount of answers submitted!")
    return tuple(answers_list)


def input_tuple(prompt: str, types: tuple, sep: str):
    print("**Not using list comprehension**")
    answers = input(prompt + "\n**Please use '" + sep + "' to separate your responses**: ")
    answers_list = answers.split(sep)
    try:
        answer_objects = check_tokens(types, answers_list)
    except IndexError as err:
        print(err)
        return ()
    except TypeError as err:
        print(err)
        return ()
    except ValueError as err:
        print(err)
        return ()
    return answer_objects


def check_tokens(types: tuple, answers: list):
    if len(types) == len(answers):
        for i in range(len(types)):
            if types[i] != bool:
                answers[i] = types[i](answers[i])  # int("3")
            else:
                answers[i] = str_to_bool(answers[i])
    else:
        raise IndexError("Index Error! Incorrect amount of answers submitted!")
    return tuple(answers)


def str_to_bool(str_to_convert: str):
    if str_to_convert in false_dict:
        return bool(0)
    else:
        return bool(1)


def read_tuple(types: tuple, sep: str, file):
    try:
        car_info = file.readline().split(sep)
        if len(types) == len(car_info):
            car_info = [types[i](car_info[i]) if types[i] != bool else str_to_bool(car_info[i])
                        for i in range(len(types))]
        else:
            raise ValueError("Not enough answers submitted!")
    except ValueError as err:
        print(err)
        return ()
    return tuple(car_info)


false_dict = ['False', 'false', 'FALSE', '0']

while True:
    prompt_for_user = "Enter the first name, last name, age (float), ID (int), full-time (bool)"
    types_required = (str, str, float, int, bool)
    separator = ","
    # print("Without list comprehension: " + str(input_tuple(prompt_for_user, types_required, separator)) + "\n")
    # print("With list comprehension: " + str(input_tuple_lc(prompt_for_user, types_required, separator)) + "\n")
    cars_file = open("cars.csv", "r")
    lol = read_tuple(types_required, separator, cars_file)
    lol2 = read_tuple(types_required, separator, cars_file)
    print(lol)
    print(lol2)
    input()
