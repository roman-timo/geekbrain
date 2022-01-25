# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:

from functools import wraps

def val_checker(check):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if check(*args):
                return func(*args)
            else:
                raise ValueError(f'wrong val: {", ".join(map(str, args))}')
        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(3))


