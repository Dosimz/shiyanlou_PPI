import PPI
import time


n = 50
flag = input('1~4: ')
if '1' in flag:
    print('='*79)
    bar = PPI.ProgBar(n,monitor = True)
    for i in range(n):
        time.sleep(0.1)
        bar.update(item_id='yuyi', force_flush=True)
    print(bar)

if '2' in flag:
    print('='*79)
    for i in PPI.prog_bar(range(n)):
        time.sleep(0.1)

if '3' in flag:
    print('='*79)
    bar = PPI.ProgPercent(n,monitor = True)
    for i in range(n):
        time.sleep(0.1)
        bar.update(iterations=1, item_id='yuyi', force_flush=True)
    print(bar)

if '4' in flag:
    print('='*79)
    for i in PPI.prog_percent(range(n)):
        time.sleep(0.1)