import time

message = "Learning Python is fun!"
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)
