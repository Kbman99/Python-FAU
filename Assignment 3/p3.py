def get_csv_data(p, str_pos_lst: list, sep: str):
    counter = 1
    try:
        data_lst = list()
        data_lst.append(p.readline().split(sep))
        for line in p:
            data_lst.append(line.split(sep))
            for i in range(len(data_lst[counter])):
                if i not in str_pos_lst:
                    # print(data_lst[counter][i])
                    data_lst[counter][i] = float(data_lst[counter][i])
            counter += 1
    except ValueError:
        # When attempting to parse '' ValueError is raised
        pass
    return data_lst


def get_columns(data_lst: list, cols_lst: list):
    column_indices = [index for index in range(len(data_lst)) if data_lst[0][index] in cols_lst]
    cols = [[data_lst[i][j] for i in range(1, len(data_lst)-1)] for j in column_indices]
    return cols


separator = ","
count = 0
bb_file = open('lb-james.csv', 'r')
# print(type(bb_file))
# input()
bb_lst = get_csv_data(bb_file, [0, 2, 3, 4], separator)
for i in range(len(bb_lst)):
    for j in range(len(bb_lst[i])):
        count += 1
bb_file.close()
get_columns(bb_lst, ["Age", "Season"])
