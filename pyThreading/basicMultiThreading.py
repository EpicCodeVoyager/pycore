import threading
import time

t_start = time.perf_counter()


def do_something(seconds):
    time.sleep(seconds)
    print(f'Done sleeping for {seconds}')
    return f'Done sleeping for {seconds}'

threads = []

for i in range(5):
    t = threading.Thread(target=do_something, args=[i+1])
    t.start()
    threads.append(t)
    #t.join()


for thread in threads:
    thread.join()


t_end = time.perf_counter()
print(f'Time taken: {round(t_end - t_start, 5)}')
