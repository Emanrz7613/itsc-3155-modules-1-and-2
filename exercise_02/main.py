import time 
import random

def fib(num):
    if num < 2:
        return num
    else:
        return (fib(num-1) + fib(num-2))

num = random.randrange(15,35)
print('fib(' + str(num) +')=' + str(fib(num)))
print('fib(' + str(num) + ') took ' + str(time.process_time()) + 'seconds')

