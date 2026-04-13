# Exercise time countdown

import time 

def count(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done")

count(0,10)