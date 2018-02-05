import time
import datetime
import math

n = input("Max value : ")
start_t = time.time()
A = [True] * (n+1)
for i in range(2, int(math.sqrt(n))+1):
	if A[i] is True:
		for j in range(i*i, n+1, i):
			A[j] = False

print(time.time() - start_t)
# print([i for i in range(len(A)) if A[i] and i > 1])