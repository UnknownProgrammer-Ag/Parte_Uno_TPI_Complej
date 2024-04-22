def delta_time(func):
    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Funcion {func.__name__!r} ejecutada en {(end-start):.4f}s')
        return result
    return wrap_func
