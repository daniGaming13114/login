import time

load = '#'
count = 0

for x in range(101):
    time.sleep(0.001)
    print(f'\rLoading {x}% [{load}]', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '#'
print('\n')
print('\033[1;32m[ PROSES SELESAI ]')

