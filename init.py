import time
import datetime

max_val = input("Max value : ")
start_t = time.time()
val_ls = [i+2 for i in range(max_val-1)]
for i in range(2, max_val):
    for val in val_ls:
        if val % i == 0 and val != i:
            del val_ls[val_ls.index(val)]

print(time.time() - start_t)
