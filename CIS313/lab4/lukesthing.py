from __future__ import print_function
import sys
import time

# status generator


def range_with_status(total):
    n = 0
    while n < total:
        done = '#'*(n+1)
        todo = '-'*(total-n-1)
        s = '<{0}>'.format(done+todo)
        if not todo:
            s += '\n'
        if n > 0:
            s = '\r'+s
        sys.stdout.write(s)
        sys.stdout.flush()
        yield n
        n += 1


print('doing something ...')
for i in range_with_status(3):
    time.sleep(0.1)

print('ready')
time.sleep(0.4)


print('And now for something completely different ...')
time.sleep(0.5)
msg = 'I am going to erase this line from the console window.'
sys.stdout.write(msg)
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\r' + ' '*len(msg))
sys.stdout.flush()
time.sleep(0.5)
print('\rdid I succeed?')
time.sleep(4)
