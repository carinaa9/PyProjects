import time

input_time = int(input('Please enter the time in seconds: '))

for x in range(input_time, 0, -1):
    hours = int(x / 3600) # 1h has 3600s
    minutes = int((x / 60) % 60) #1min has 60s
    seconds = x % 60
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print('Time is up!')
