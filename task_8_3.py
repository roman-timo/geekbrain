from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}: arg - {arg}: {type(arg)}', end=', ')
            print(f'val - {func(arg)}: {type(*func(arg))}')
        return func(*args)
    return wrapper

@type_logger
def calc_cube(*args):
    out_lst = [i ** 3 for i in args]
    return out_lst

a = calc_cube(5, 6.1)

