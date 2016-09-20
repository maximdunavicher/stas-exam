from single_point import parse
__author__ = 'stas'


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
        Handling the missing data by skipping people with missing feature data
        (feature=? or len of feature vector!=15)
    """
    unknown = "?"
    max_row_len = 15
    final_x_matrix = list()
    final_y_vector = list()
    with open(data_file_full_path) as f:
        for line in f:
            row = [x.strip() for x in line.split(',')]
            if unknown not in row and len(row) == max_row_len:
                x, y = parse(row)
                final_x_matrix.append(x)
                final_y_vector.append(y)

    return final_x_matrix, final_y_vector
