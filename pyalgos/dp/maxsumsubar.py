import time
import random


# a = [1, 2, 4, 5, 8, 9, 2, 5, 2, 7]

def find_max_sub_sum_by_slice(a):
    ts1 = time.perf_counter()
    k = 3
    m_sum = 0
    for i in range(len(a) - k + 1):
        t_sum = sum(a[i:i + k])
        m_sum = max(t_sum, m_sum)
        # print(f'SubArray: {a[i:i+k]}, Sum: {t_sum}, Max_Now: {m_sum}')
    te1 = time.perf_counter()
    print(f"Max sum is: {m_sum}, Time taken: {te1 - ts1:6f}")


# Doing it the probable efficient way:

def find_max_sub_sum_by_loop(a):
    ts2 = time.perf_counter()
    k = 3
    m_sum = 0
    for i in range(len(a) - k + 1):
        t_sum = 0
        for j in range(i, i + k):
            t_sum += a[j]
        #t_sum=a[i]+a[i+1]+a[i+2]
        m_sum = max(t_sum, m_sum)
    te2 = time.perf_counter()
    print(f"Max sum by 2nd method:{m_sum}, Time taken: {te2 - ts2:6f}")
    

def find_max_sub_sum_by_loop_new(a):
    ts2 = time.perf_counter()
    k = 3
    m_sum = 0
    for i in range(len(a) - k + 1):
        t_sum = 0
        #for j in range(i, i + k):
        #    t_sum += a[j]
        t_sum=a[i]+a[i+1]+a[i+2]
        m_sum = max(t_sum, m_sum)
    te2 = time.perf_counter()
    print(f"Max sum by 3rd method:{m_sum}, Time taken: {te2 - ts2:6f}")



a = [random.randrange(1, 50, 1) for i in range(10000000)]
for i in range(20):
    find_max_sub_sum_by_slice(a)
    find_max_sub_sum_by_loop(a)
    find_max_sub_sum_by_loop_new(a)
