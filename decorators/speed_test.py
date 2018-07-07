# Let's define a speed_test decorator
from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(100000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(1000000)])


result_gen = sum_nums_gen()
result_list = sum_nums_list()
