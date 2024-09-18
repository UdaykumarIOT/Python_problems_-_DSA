import timeit

def print_this(func) -> None:
    def wrapper(*args,**kw) -> None:
        print()
        start_time=timeit.default_timer()
        print(func(*args,**kw),sep="\t",flush=True)
        end_time=timeit.default_timer()
        total_time = end_time-start_time
        print(f"Time ({func.__name__}) : {total_time * 1000:.2f} ms")
        print("___________________________________")

    return wrapper

def avg_time(func) -> None:
    def wrapper(*args,**kw) -> None:
        print(f'{func.__name__} function started execution \n')
        total_time : int=0
        for i in range(5):
            start_time=timeit.default_timer()
            func(*args,**kw)
            end_time=timeit.default_timer()
            total_time += (end_time-start_time)
        print(f'\n{func.__name__} function ended its execution in {total_time / 5 : .5f} seconds')
        
    return wrapper

def get_time(func) -> None:
    def wrapper(*args,**kw) -> None:
        print(f'{func.__name__} function started execution \n')
        start_time=timeit.default_timer()
        func(*args,**kw)
        end_time=timeit.default_timer()
        total_time = end_time-start_time
        print(f'\n{func.__name__} function ended its execution in {total_time : .5f} seconds')
        
    return wrapper

