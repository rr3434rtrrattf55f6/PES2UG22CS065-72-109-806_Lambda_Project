import time

start = time.time()

total = 0
for i in range(10**6):
    total += i

end = time.time()

print("Benchmark test completed")
print(f"Total: {total}")
print(f"Execution Time: {end - start:.4f} seconds")
