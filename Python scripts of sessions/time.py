import time

current_time = time.time()
print("Current time in seconds since the epoch:", current_time)

print("This is printed immediately.")
time.sleep(2)  # Pause the program execution for 2 seconds
print("This is printed after a 2-second delay.")



current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("Formatted time:", formatted_time)


# Measure Code block execution time 

start_time = time.time()

for _ in range(1000000):
    pass

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")


timestamp = 1628379223  # Example timestamp
utc_time = time.gmtime(timestamp)
print("UTC time:", utc_time)

local_time = time.localtime(timestamp)
print("Local time:", local_time)