import pylab


def get_csv_data(p, str_pos_lst: list, sep: str):
    counter = 1  # holds the line to search through
    try:
        data_lst = list()
        data_lst.append(p.readline().split(sep))  # add first line (headers) to the list
        for line in p:
            data_lst.append(line.split(sep))  # append remaining lines to list and split them
            for i in range(len(data_lst[counter])):
                if i not in str_pos_lst:  # check if we need to convert item at current index to float
                    data_lst[counter][i] = float(data_lst[counter][i])
            counter += 1
    except ValueError:
        # When attempting to parse '' ValueError is raised
        pass
    return data_lst


def get_columns(data_lst: list, cols_lst: list):
    column_indices = [index for index in range(len(data_lst[0])) if data_lst[0][index] in cols_lst]
    cols = [[data_lst[i][j] for i in range(1, len(data_lst)-1)] for j in column_indices]
    return cols


def stats_graph(stats_list: list, data_points: int):
    pylab.xlabel("Year in NBA")
    pylab.ylabel("Percentage")
    pylab.title("LeBron over the years")
    for i in range(len(stats_list)):
        for j in range(len(stats_list[i])):
            stats_list[i][j] = 100 * stats_list[i][j]
    pylab.plot(data_points, stats_list[0], '-bo', label="3 point shooting")
    pylab.plot(data_points, stats_list[1], '-go', label="2 point shooting")
    pylab.plot(data_points, stats_list[2], '-ro', label="Free throws")
    pylab.legend(loc="upper left")
    pylab.ylim(0, 100)
    pylab.grid()
    pylab.show()

separator = ","
count = 0
bb_file = open('lb-james.csv', 'r')
bb_lst = get_csv_data(bb_file, [0, 2, 3, 4], separator)
for i in range(len(bb_lst)):
    for j in range(len(bb_lst[i])):
        count += 1
years = list(range(1,15))
lb_stats = get_columns(bb_lst, ["2P%", "3P%", "FT%"])
print(len(lb_stats))
stats_graph(lb_stats, years)
bb_file.close()