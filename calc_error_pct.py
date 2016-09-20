__author__ = 'stas'


def calculate_error_percentage(y_vector, predicted_y_vector):
    """Gets a vector y of results, and vector y_prediction of predictions, compares, and calculates error percentage
    """

    # Make sure both vectors are of the same size
    assert(len(y_vector) == len(predicted_y_vector))

    # Calculate how many errors occurred
    error_count = 0
    total_samples = len(y_vector)
    for i in xrange(total_samples):
        if y_vector[i] != predicted_y_vector[i]:
            error_count += 1

    # Return error percentage
    return (float(error_count) / total_samples) * 100

