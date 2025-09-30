#decorators 
#

import time
from functools import wraps
  

def log_time(func):


    @wraps(func)
    def wrapper (*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end= time.time()
        print(f"{func.__name__} excuted in {end - start:.2f} seconds")
        return result
    return wrapper