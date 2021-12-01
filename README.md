# Intro
simple\_threadpool: a simple threadpool


# Install

```bash
pip install simple_threadpool
```

# Usage

```python
from __future__ import print_function

import random, time
from threading import current_thread
from simple_threadpool import ThreadPool


def my_worker(arg):
    '''
    custom worker
    '''
    print('%s: ' % current_thread().name, arg + 1)
    time.sleep(random.random())


def large_iterable(size):
    for i in range(size):
        print('getting %s' % i)
        yield i


# create a ThreadPool instance with 2 threads
tp = ThreadPool(my_worker, max_workers=2)
print('max_workers: %d' % tp.max_workers)
print('chunksize: %d' % tp.queue.maxsize)

# produce and send some data to the pool
print('First round:')
tp.feed([1, 2, 3, 4, 5])

print('Second round:')
tp.feed([6, 7, 8, 9, 0])

print('Large jobs:')
tp.feed(large_iterable(15))

# close the queue
tp.close()
```
