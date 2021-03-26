import concurrent.futures
import time

t_start = time.perf_counter()


def do_something(seconds):
    time.sleep(seconds)
    #print(f'Done sleeping for {seconds}')
    return f'Done sleeping for {seconds}'



secs = [3, 5, 7, 1, 2]
future_threads = []

with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    fths = [executor.submit(do_something, i) for i in secs]
    for f in concurrent.futures.as_completed(fths):
        print(f.result())

t_end = time.perf_counter()
print(f'Time taken: {round(t_end - t_start, 5)}')
