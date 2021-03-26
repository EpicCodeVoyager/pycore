import threading
import time

def do_something():
    time.sleep(1)
    print("Did something.")

tm1 = time.perf_counter()
do_something()
do_something()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

tm2 = time.perf_counter()

print(f'Total time taken: {round(tm2-tm1, 3)}')
