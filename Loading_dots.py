import time

print("Loading", end='')
for _ in range(3):
    time.sleep(1)
    print('.', end='', flush=True)

print(" Done!")
