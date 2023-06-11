import timeit


def time(function):
    return timeit.timeit(function, number=15)
