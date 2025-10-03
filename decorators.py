#decorators  used in the project
import time

#Import to keep the metadata like name ,docstring
from functools import wraps
  

def log_time(func):
    """Created to measure ans show the execution time of function"""

    # Preserve function name and docstring
    @wraps(func)
    def wrapper (*args, **kwargs):
        #Capture start time before function ececuation
        start=time.time()
        #calling the orginal funcitons with arguments
        result=func(*args, **kwargs)
        #Capture the end time after execution
        end= time.time()
        #print the duration of execuation
        print(f"{func.__name__} excuted in {end - start:.2f} seconds")
        #Return the orogonal funciton's result
        return result
    return wrapper #Return the wrapped funciton