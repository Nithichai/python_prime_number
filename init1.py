import time
import datetime
import math

n = input("Max value : ")
round = input("Round : ")
ls_time = []

def sieve_time(n, round):
	start_t = time.time()
	A = [True] * (n+1)
	for i in range(2, int(math.sqrt(n))+1):
		if A[i] is True:
			for j in range(i*i, n+1, i):
				A[j] = False
	return (time.time() - start_t) * 1000000

for i in range(round):
	ls_time.append(sieve_time(n, round))

print("Min of time : %f us." % min(ls_time))
print("Max of time : %f us." % max(ls_time))
print("Avg of time : %f us." % (max(ls_time) / len(ls_time)))