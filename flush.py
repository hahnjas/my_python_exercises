import time

print("three", flush=True, end="\r")
time.sleep(1)

print("two  ", flush=True, end="\r")
time.sleep(1)

print("one  ", flush=True)
time.sleep(1)
