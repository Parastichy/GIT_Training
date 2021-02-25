def lazy(n):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            if n == 0:
                return None
            if n > 0:
                if (wrapper.count - 1) % n == 0:
                    return_value = func(*args, **kwargs)
                else:
                    return_value = None
                return return_value
            if n < 0:
                if wrapper.count % n != 0:
                    return_value = func(*args, **kwargs)
                else:
                    return_value = None
                return return_value

        wrapper.count = 0
        return wrapper

    return actual_decorator


if __name__ == '__main__':
    @lazy(4)
    def half(x):
        return x / 2


    print(half(10))  # 5  <- Remember, First run should be normal
    print(half(77))  # None
    print(half(63))  # None
    print(half(2))  # None
    print(half(38))  # 19 <- Every nth run (in this case 4) after the first should also be normal


    @lazy(-3)
    def output_str(s):
        print(s)


    output_str('Foo')  # Foo <- Starts normal
    output_str('Bar')  # Bar
    output_str('Pikachu')  # Nothing printed <- Every nth run is lazy
    output_str('Gla')  # Gla
