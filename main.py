# Floyd's Cycle Detection
# def detect_cycle(n):
#     r = 1
#     slow = (1 * 10) % n
#     fast = (((1 * 10) % n) * 10) % n
#     # Floyd's cycle detection algorithm
#     while 1:
#         if fast == 0: return 0 # our termination condition
#         if slow == fast:
#             # we know cycle exists
#             c = 1
#             slow = (slow * 10) % n
#             while slow != fast:
#                 slow = (slow * 10) % n
#                 c += 1

#             return c
#         slow = (slow * 10) % n
#         fast = (((fast * 10) % n) * 10) % n
#     return 0

def detect_cycle(n):
    len = 1
    multi = 1

    slow = 1
    fast = 10 % n
    while slow != fast:
        if len == multi:
            slow = fast
            multi *= 2
            len = 0
        fast = (fast * 10) % n
        len += 1
    return len

from time import perf_counter
n = perf_counter()

m = 0
mi = 1
for i in range(3, 1000, 2): # You can iterate over only primes as well
    if i % 5 == 0: continue

    k = detect_cycle(i)
    if m < k:
        m = k
        mi = i

print(mi, perf_counter() - n)
