import timeit
import os
ex_path     = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ex_path,"day9.py")) as f:
    print (timeit.timeit(stmt = f.read(), number = 100) / 100 ) 