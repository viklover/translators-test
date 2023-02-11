
import time

def with_timer(func):

    def timer(*args, **kwargs):
        start = time.time()
        translation = func(*args, **kwargs)
        end = time.time()
        return translation, end - start

    return timer
