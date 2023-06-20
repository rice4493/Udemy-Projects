grades = [9.6, 9.2, 9.7]


def get_max():
    maximum = grades[0]
    for item in grades:
        if item > maximum:
            maximum = item
    return maximum


def get_min():
    minimum = grades[0]
    for item in grades:
        if item < minimum:
            minimum = item
    return minimum


print(f"Max: {get_max()}, Min: {get_min()}")
