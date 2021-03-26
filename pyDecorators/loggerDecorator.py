from functools import wraps


def log_it(ofunc):
    import logging
    logging.basicConfig(filename="log_it_function.log", level=logging.INFO)

    @wraps(ofunc)
    def wrapper(*args, **kwargs):
        print("Wrapping the custom function")
        logging.info(f'Function call: {ofunc.__name__}{args},{kwargs}')
        ofunc(*args, **kwargs)

    return wrapper


def time_it(ofunc):
    import time
    import logging
    logging.basicConfig(filename="log_it_function.log", level=logging.INFO)

    @wraps(ofunc)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ofunc(*args, **kwargs)
        t2 = time.time()
        logging.info(f'Time taken to execute {ofunc.__name__} is {t2 - t1} seconds.')

    return wrapper


import time


@time_it
@log_it
def greet_person(person, greeting):
    time.sleep(1)
    print(f"{person} {greeting}")


@time_it
@log_it
def harami_person(person: str, gali: str):
    time.sleep(1)
    print(f"{person} gali {gali}")


if __name__ == '__main__':
    greet_person("Saurabh", "Hello")
    harami_person("Chu", "pagal")
