import time
import datetime
import math

max_val = input("Max value : ")
start_t = time.time()

val_set = set([i+2 for i in range(1,max_val-1)])

for i in range(2, int(math.sqrt(max_val-1))):
    val_ls = list(val_set)
    for val in val_ls:
        if val % i == 0 and val != i:
            val_set.remove(val)

print(time.time() - start_t)
